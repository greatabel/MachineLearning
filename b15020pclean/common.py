import re, collections


def get_words(text):
    return re.findall("[a-z]+", text.lower())


def probability_model(wordseq):
    wordCount = collections.defaultdict(lambda: 1)
    for word in wordseq:
        wordCount[word] += 1
    return wordCount


def valid_telephone_number(inp):
    # make sure len is 12 and all char at index 3 and 7  are -
    if not all(inp[x] == "-" for x in [3,7])and len(inp) == 12:
        return False
    # will be True if all that is left are digits after removing the - else False
    return inp.replace("-", "", 3).isdigit()



