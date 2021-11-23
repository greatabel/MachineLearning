import re, collections

from common import get_words, probability_model, filterTheDict

import pandas as pd 

'''
构建语料，作为一个背景，先验材料：调用更正(w) 尝试为w 选择最可能的拼写更正。 
没有办法确定（例如，应该将“los”更正为“lost”或“loss”……），
这之间只有从材料中获得我们使用概率。 
在给定原始单词 word 的情况下，我们试图从所有可能的候选更正中找到更正correct，
使 correct 是预期更正的概率最大化：
'''
orginal_txt = ''
df = pd.read_csv("datasets/hospital_clean.csv")
# df = pd.read_csv("datasets/hospital_dirty.csv")
for index, row in df.iterrows():
    orginal_txt += ' ' + row['HospitalName']
    orginal_txt += ' ' + row['Address1']
    orginal_txt += ' ' + row['MeasureName']


r = get_words(orginal_txt)
dictionary = probability_model(
    r
)  # all the words in the language model

# 提高错误和正确区分阀值
dictionary = filterTheDict(dictionary, lambda elem: elem[1] > 10)
print(dictionary)

alphabet = "abcdefghijklmnopqrstuvwxyz"


'''
可以理解成类似修改次数最小的方案，然后用对应的次数来表示A和B的距离的想法：
：对单词的简单编辑是删除（删除一个字母）、换位（交换两个相邻的字母）、
替换（将一个字母更改为另一个字母）或插入（添加一个字母）。 
函数 edits1 返回一组所有编辑过的字符串（无论是否为单词），
这些字符串可以通过一个简单的编辑完成
'''
def dist1_words(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]  # n deletions
    transposes = [
        a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1
    ]  # n-1 transpositions
    replaces = [
        a + c + b[1:] for a, b in splits for c in alphabet if b
    ]  # 26n alterations
    inserts = [a + c + b for a, b in splits for c in alphabet]  # 26(n+1) insertions
    return set(deletes + transposes + replaces + inserts)

'''
获得并集
'''
def dist2_words(word):

    return set(word2 for word1 in dist1_words(word) for word2 in dist1_words(word1))


def legal_words(words):

    return set(w for w in words if w in dictionary)

'''
单个词的修正/补全
'''
def correct_word(word):

    possibleWords = (
        legal_words([word])
        or legal_words(dist1_words(word))
        or legal_words(dist2_words(word))
        or [word]
    )
    return max(possibleWords, key=dictionary.get)

'''
列表的修正和不缺
'''
def correct_words(sentence):

    words = get_words(sentence)

    # return set(correct_word(word) for word in words )
    return " ".join(correct_word(word) for word in words)



