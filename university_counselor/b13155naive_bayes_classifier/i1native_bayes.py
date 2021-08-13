import re
import csv
import random

import numpy as np
import jieba

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from i0preprocessing import csv_writer_list_to_local


jieba.load_userdict("data/i1userdict.txt")
file_path = "data/i1addtional_content.csv"
stopword_path = "data/i1stopwords.txt"


def load_dataset(content_path):
    with open(content_path, "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    # 将读取出来的语料转为list
    content_data = np.array(rows).tolist()
    # 打乱语料的顺序
    random.shuffle(content_data)

    content_list = []
    sentiment_list = []
    # 第一列为差评/好评， 第二列为内容
    for words in content_data:
        content_list.append(words[1])
        sentiment_list.append(words[0])

    return content_list, sentiment_list


def load_stopwords(file_path):
    stop_words = []
    with open(file_path, encoding="UTF-8") as words:
        stop_words.extend([i.strip() for i in words.readlines()])
    return stop_words


def content_to_text(review):
    stop_words = load_stopwords(stopword_path)
    # 去除英文
    review = re.sub("[^\u4e00-\u9fa5^a-z^A-Z]", "", review)
    review = jieba.cut(review)
    # 去掉停用词
    if stop_words:
        all_stop_words = set(stop_words)
        words = [w for w in review if w not in all_stop_words]

    return words

# 定义Pipeline对全部步骤的流式化封装和管理，可以很方便地使参数集在新数据集（比如测试集）上被重复使用。
def MuitpleNativeBayes_Classifier():
    return Pipeline([("count_vec", CountVectorizer()), ("mnb", MultinomialNB())])



# 加载语料
content_list, sentiment_list = load_dataset(file_path)

# 将全部语料按1:9分为测试集与训练集
n = len(content_list) // 10
train_content_list, train_sentiment_list = content_list[n:], sentiment_list[n:]
test_content_list, test_sentiment_list = content_list[:n], sentiment_list[:n]

print("训练集数量： {}".format(str(len(train_content_list))))
print("测试集数量： {}".format(str(len(test_content_list))))


# 用于训练的内容
content_train = [" ".join(content_to_text(review)) for review in train_content_list]
# 对于训练内容对应的好评/差评
sentiment_train = train_sentiment_list

# 用于测试的内容
content_test = [" ".join(content_to_text(review)) for review in test_content_list]
# 对于测试内容对应的好评/差评
sentiment_test = test_sentiment_list

count_vec = CountVectorizer(max_df=0.8, min_df=3)

tfidf_vec = TfidfVectorizer()



mnbc_clf = MuitpleNativeBayes_Classifier()

# 进行训练
mnbc_clf.fit(content_train, sentiment_train)

# 测试集准确率
print("测试集准确率： {:0.2f}".format(mnbc_clf.score(content_test, sentiment_test)))

# 收集测试集结果
a = mnbc_clf.predict(content_test).tolist()
my_pedict_list = []
for i in range(len(content_test)):
    data = {'sentiment': '', 'content': '', 'predict':''}

    data['sentiment'] = sentiment_test[i]
    data['content'] = content_test[i]
    data['predict'] = a[i]

    my_pedict_list.append(data)

print('--保存预测结果--')
print(len(my_pedict_list), my_pedict_list[1:3])
csv_writer_list_to_local('data/i1my_pedict_list.csv', my_pedict_list)