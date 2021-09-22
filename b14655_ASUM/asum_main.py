import sys
import common
import my_asum


import numpy as np
from scipy.spatial import distance
from paddlehub.reader.tokenization import load_vocab
import paddle.fluid as fluid
import paddlehub as hub


def main():
    try:

        # 后期发现paddlehub的词库更好，就替换了哈工大词汇
        # voca_file_path = "mydata/THUOCL_food.txt"

        senti_words_prefix_path = "mydata/SentiWords-"

        document_file_path = "mydata/aquatic_pick.csv"
        output_file_name = "mydata/abel_aquatic.txt"

        # document_file_path = "mydata/food_db_pick.csv"
        # output_file_name = "mydata/abel_food.txt"

        # document_file_path = "mydata/vegetable_pick.csv"
        # output_file_name = "mydata/abel_vegetable.txt"

        # document_file_path = "mydata/meat_pick.csv"
        # output_file_name = "mydata/abel_meat.txt"

        # document_file_path = "mydata/frozen_pick.csv"
        # output_file_name = "mydata/abel_frozen.txt"

        topics = 3
    except IndexError:
        print(
            "Error import".format(
                __file__
            )
        )
        return

    # vocas = common.read_voca_file(voca_file_path)
    ###

    module = hub.Module(name="word2vec_skipgram")  # 实例化 word2vec_skipgram 模型
    inputs, outputs, program = module.context(trainable=False)
    # 利用 模型实例化后的 API，把接口导出来，这里有 3 个接口，分别是 输入，输出，程序主体

    vocab = load_vocab(module.get_vocab_path())  # 获得 词表 字典
    ###

    senti_words = list()
    # for senti_words_file_idx in range(3):
    for senti_words_file_idx in range(2):
        print("senti_words_file_idx=", senti_words_file_idx)
        senti_words_file_path = (
            senti_words_prefix_path + str(senti_words_file_idx) + ".txt"
        )
        senti_words.append(common.read_voca_file(senti_words_file_path))

    # ASUM_Model = my_asum.my_asum(topics, senti_words, document_file_path, vocas)
    ASUM_Model = my_asum.ASUMGibbs(topics, senti_words, document_file_path, vocab)
    ASUM_Model.run(max_iter=2000)
    ASUM_Model.export_result(output_file_name)


if __name__ == "__main__":
    main()
