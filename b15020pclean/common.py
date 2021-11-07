import re, collections


def get_words(text):
    return re.findall("[a-z]+", text.lower())


def probability_model(wordseq):
    wordCount = collections.defaultdict(lambda: 1)
    for word in wordseq:
        wordCount[word] += 1
    return wordCount
