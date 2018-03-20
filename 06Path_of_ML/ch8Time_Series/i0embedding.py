import re
import numpy as np

def process_text(text):
    """将标点符号替换成空格"""
    dot_word = r'。|，|\.|\?|,|!|，|\(|\)|\(|\)| '
    return re.sub(dot_word, ' ', text)


def text2vec(text):
    """将文本转换成向量"""
    cleaned_text = process_text(text) # 输入文本预处理
    text_vec = cleaned_text.split()
    vocab_list = list(set(text_vec)) # 词汇集
    numer_vec = [0.]*len(vocab_list) # 数字向量
    for word in text_vec:
        # 每遇到一个单词，对应的数字向量位置+1
        numer_vec[vocab_list.index(word)] += 1
    return numer_vec / np.sum(numer_vec) # 归一化，让向量中所有数值加起来等于1

text = 'Without a doubt, a loving and friendly puppy or dog can put an instant smile on your face! \
        When you adopt a dog from Atlanta Humane Society, you gain a wonderful canine companion. \
        But most of all, when you adopt a rescue dog, you have the ability to bond with one of \
        Atlanta’s forgotten and neglected animals.'

result = text2vec(text)
print(result)