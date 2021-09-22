import time
import numpy as np
import scipy.special
import re

import numpy as np
from scipy.spatial import distance
from paddlehub.reader.tokenization import load_vocab
import paddle.fluid as fluid
import paddlehub as hub

# 这是把 中文词语 转化为 词表 中对应 ID 的函数
def convert_tokens_to_ids(vocab, words):  # 输入为词表，和要转化的 text
    wids = []  # 初始化一个空的集合，用于存放输出
    tokens = words  # 将传入的 text 用 空格 做分割，变成 词语字符串 的列表
    for token in tokens:  # 每次从列表里取出一个 词语
        wid = vocab.get(token, None)
        if not wid:
            wid = vocab["unknown"]
        wids.append(wid)
    return wids


# def convert_tokens_to_ids(vocab, words):  # 输入为词表，和要转化的 text
#     wids = []  # 初始化一个空的集合，用于存放输出
#     tokens = text.split(" ")  # 将传入的 text 用 空格 做分割，变成 词语字符串 的列表
#     for token in tokens:  # 每次从列表里取出一个 词语
#         wid = vocab.get(token, None)
#         if not wid:
#             wid = vocab["unknown"]
#         wids.append(wid)
#     return wids


class ASUMGibbs:
    """
    Aspect and Sentiment Unification Model for Online Review Analysis
    Yohan Jo, Alice Oh, 2011
    """

    def __init__(
        self,
        num_topics,
        senti_words,
        doc_file_path,
        vocas,
        alpha=0.1,
        beta=0.01,
        gamma=0.1,
        high_beta=0.7,
    ):
        """
        Constructor method
        Constructor method
        :param num_topics: the number of topics
        :param doc_file_path: BOW document file path
        :param vocas: vocabulary list
        :param alpha: alpha value in ASUM
        :param beta: beta value in ASUM
        :param gamma: gamma value in ASUM
        :param high_beta: beta value in ASUM for sentiment words
        :return: void
        :return: void
        """
        self.docs = self.read_bow(doc_file_path)
        # self.words = vocas
        self.words = list(vocas.keys())
        print(self.words[0:100], "#-#" * 10)
        self.K = num_topics
        self.D = len(self.docs)
        self.W = len(vocas)
        self.S = len(senti_words)
        print("#" * 30, len(self.words), "#" * 5, self.words[19696])
        word_idx = 0
        self.words_to_idx = dict()
        for word in self.words:
            self.words_to_idx[word] = word_idx
            word_idx += 1

        # Hyper-parameters
        self.alpha = alpha
        self.beta = np.zeros((self.S, self.W)) + beta
        for senti_idx, one_senti_words in enumerate(senti_words):
            for one_senti_word in one_senti_words:
                try:
                    self.beta[senti_idx, self.words_to_idx[one_senti_word]] = high_beta
                except KeyError:
                    pass
        self.gamma = gamma

        self.DST = np.zeros((self.D, self.S, self.K), dtype=np.int64)
        self.STW = np.zeros((self.S, self.K, self.W), dtype=np.int64)

        # Random initialization of topics
        self.doc_topics = list()

        for di in range(self.D):
            doc = self.docs[di]

            topics = np.random.randint(self.S * self.K, size=len(doc))
            self.doc_topics.append(topics)

            for senti_topic, sentence in zip(topics, doc):
                senti = senti_topic // self.K
                topic = senti_topic % self.K
                self.DST[di, senti, topic] += 1

                target_mat = self.STW[senti, topic, :]
                for word_idx, word_cnt in sentence:
                    target_mat[word_idx] += word_cnt

    def run(self, max_iter=2000, do_optimize=False, do_print_log=False):
        """
        Run Collapsed Gibbs sampling for ASUM
        :param max_iter: Maximum number of gibbs sampling iteration
        :param do_optimize: Do run optimize hyper-parameters
        :param do_print_log: Do print loglikelihood and run time
        :return: void
        """
        if do_optimize and do_print_log:
            prev = time.process_time()
            for iteration in range(max_iter):
                print(iteration, time.process_time() - prev, self.loglikelihood())
                prev = time.process_time()
                self._gibbs_sampling()
                if 99 == iteration % 100:
                    self._optimize()
        elif do_optimize and not do_print_log:
            for iteration in range(max_iter):
                self._gibbs_sampling()
                if 99 == iteration % 100:
                    self._optimize()
        elif not do_optimize and do_print_log:
            prev = time.process_time()
            for iteration in range(max_iter):
                print(iteration, time.process_time() - prev, self.loglikelihood())
                prev = time.process_time()
                self._gibbs_sampling()
        else:
            prev = time.process_time()
            for iteration in range(max_iter):
                print(iteration, time.process_time() - prev)
                prev = time.process_time()
                self._gibbs_sampling()

    def _gibbs_sampling(self):
        """
        Run Gibbs Sampling
        :return: void
        """
        for di in range(self.D):
            doc = self.docs[di]
            cur_doc_senti_topics = self.doc_topics[di]

            for sentence_idx, sentence in enumerate(doc):
                # Old one
                old_senti_topic = cur_doc_senti_topics[sentence_idx]
                senti = old_senti_topic // self.K
                topic = old_senti_topic % self.K

                self.DST[di, senti, topic] -= 1
                target_mat = self.STW[senti, topic, :]
                for word_idx, word_cnt in sentence:
                    target_mat[word_idx] -= word_cnt

                first_term = (
                    np.sum(self.DST[di, :, :], axis=1, keepdims=True) + self.gamma
                )
                second_term_part = self.DST[di, :, :] + self.alpha
                second_term = second_term_part / (
                    np.sum(second_term_part, axis=1, keepdims=True)
                )
                third_term_part = np.sum(self.STW, axis=2) + np.sum(
                    self.beta, axis=1, keepdims=True
                )
                forth_term = 1
                words_in_doc = 0
                for word_idx, word_cnt in sentence:
                    words_in_doc += word_cnt
                    forth_term_part = self.STW[:, :, word_idx] + self.beta[:, word_idx]
                    temp_prod = 1
                    for cnt_idx in range(word_cnt):
                        temp_prod *= forth_term_part + cnt_idx
                    forth_term *= temp_prod
                third_term = scipy.special.gamma(third_term_part) / (
                    scipy.special.gamma(third_term_part + words_in_doc)
                )

                # Sampling
                prob = first_term * second_term * third_term * forth_term
                prob = prob.flatten()

                # New one
                new_senti_topic = self._sampling_from_dist(prob)
                senti = new_senti_topic // self.K
                topic = new_senti_topic % self.K

                cur_doc_senti_topics[sentence_idx] = new_senti_topic

                self.DST[di, senti, topic] += 1
                target_mat = self.STW[senti, topic, :]
                for word_idx, word_cnt in sentence:
                    target_mat[word_idx] += word_cnt

    @staticmethod
    def _sampling_from_dist(prob):
        """
        Multinomial sampling with probability vector
        :param prob: probability vector
        :return: a new sample (In this class, it is new topic index)
        """
        thr = prob.sum() * np.random.rand()
        new_topic = 0
        tmp = prob[new_topic]
        while tmp < thr:
            new_topic += 1
            tmp += prob[new_topic]
        return new_topic

    def loglikelihood(self):
        """
        Compute log likelihood function
        :return: log likelihood function
        """
        return self._topic_loglikelihood() + self._document_loglikelihood()

    def _topic_loglikelihood(self):
        """
        Compute log likelihood by topics
        :return: log likelihood by topics
        """
        raise NotImplementedError

    def _document_loglikelihood(self):
        """
        Compute log likelihood by documents
        :return: log likelihood by documents
        """
        raise NotImplementedError

    def _optimize(self):
        """
        Optimize hyperparameters
        :return: void
        """
        self._alphaoptimize()
        self._betaoptimize()
        self._gammaoptimize()

    def _alphaoptimize(self, conv_threshold=0.001):
        """
        Optimize alpha vector
        :return: void
        """
        raise NotImplementedError

    def _betaoptimize(self, conv_threshold=0.001):
        """
        Optimize beta value
        :return: void
        """
        raise NotImplementedError

    def _gammaoptimize(self, conv_threshold=0.001):
        """
        Optimize gamma value
        :return: void
        """
        raise NotImplementedError

    def export_result(self, output_file_name, rank_idx=100):
        """
        Export Algorithm Result to File
        :param output_file_name: output file name
        :param rank_idx:
        :return: the number of printed words in a topic in output file
        """
        # Raw data
        np.save("%s_DST.npy" % output_file_name, self.DST)
        # np.save("%s_STW.npy" % output_file_name, self.STW)

        # Ranked words in topics
        with open(
            "%s_Topic_Ranked.csv" % output_file_name, "w"
        ) as ranked_topic_word_file:
            for senti_idx in range(self.S):
                for topic_idx in range(self.K):
                    topic_vec = self.STW[senti_idx, topic_idx, :]
                    sorted_words = sorted(
                        enumerate(topic_vec), key=lambda x: x[1], reverse=True
                    )
                    print("x sorted_words[:rank_idx]=", sorted_words[:rank_idx])
                    print("x[0]=", sorted_words[:rank_idx][0])
                    for x in sorted_words[:rank_idx]:
                        if x is not None:
                            if x[0] < len(self.words) and x[1] > 0:
                                print(self.words[x[0]], "$" * 20)
                    print(
                        "senti/topic {}/{},{}".format(
                            senti_idx,
                            topic_idx,
                            ",".join(
                                [
                                    self.words[x[0]]
                                    if (x[0] <= len(self.words) and x[1] > 0)
                                    else ""
                                    for x in sorted_words[:rank_idx]
                                ]
                            ),
                        ),
                        file=ranked_topic_word_file,
                    )

    def load_stopwords(file_path):
        stop_words = []
        with open(file_path, encoding="UTF-8") as words:
            stop_words.extend([i.strip() for i in words.readlines()])
        return stop_words

    def content_to_text(review):
        stopword_path = "mydata/i1stopwords.txt"
        stop_words = load_stopwords(stopword_path)
        # 去除英文
        review = re.sub("[^\u4e00-\u9fa5^a-z^A-Z]", "", review)
        review = jieba.cut(review)
        # 去掉停用词
        if stop_words:
            all_stop_words = set(stop_words)
            words = [w for w in review if w not in all_stop_words]

        return words

    @staticmethod
    def read_bow(file_path):
        """
        Read BOW file to run topic models with Gibbs sampling
        :param file_path: The path of BOW file
        :return: documents list
        """
        lac = hub.Module(name="lac")

        module = hub.Module(name="word2vec_skipgram")  # 实例化 word2vec_skipgram 模型
        inputs, outputs, program = module.context(trainable=False)
        # 利用 模型实例化后的 API，把接口导出来，这里有 3 个接口，分别是 输入，输出，程序主体

        vocab = load_vocab(module.get_vocab_path())  # 获得 词表 字典
        words = list(vocab.keys())
        words_to_idx = dict()
        word_idx = 0
        for word in words:
            words_to_idx[word] = word_idx
            word_idx += 1

        split_pattern = re.compile(r"[ :]")
        docs = list()

        with open(file_path, "r") as bow_file:
            for each_line in bow_file:
                print("#" * 10, "each_line=", each_line)
                results = lac.lexical_analysis(
                    texts=[each_line], use_gpu=False, batch_size=1
                )
                results0 = results[0]["word"]
                print("分词=", results0)

                one_doc = list()
                text_a = convert_tokens_to_ids(words_to_idx, results0)

                # sentences = each_line.split(",")[2:]
                # sentences = each_line
                # for each_sentence in sentences:
                #     split_line = split_pattern.5(each_sentence)
                #     word_ids = [int(x) for x in split_line[0::2]]
                #     word_counts = [int(x) for x in split_line[1::2]]
                #     print(word_ids, '@'*10, word_counts)
                #     one_doc.append(zip(word_ids, word_counts))
                r = [(x, text_a.count(x)) for x in set(text_a)]
                a = []
                b = []
                for item in r:
                    a.append(item[0])
                    b.append(item[1])
                print(a, "#", b)
                c = zip(a, b)
                one_doc.append(c)
                docs.append(one_doc)

        return docs
