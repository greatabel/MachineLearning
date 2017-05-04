import os
try:
    import ujson as json  # UltraJSON if available
except:
    import json
import sys
from collections import defaultdict
from i0data import chosen, chosen_meta, filtered, filtered_meta

try:
    # http://stackoverflow.com/questions/3683181/cannot-install-pyenchant-on-osx
    # 安装步骤如下：
    # brew install enchant
    # pip3.5 install PyEnchant
    import enchant
    speller = enchant.Dict("en_US")

except:
    print("""\
Enchant is not installed, which is not a problem since spell correction features
will not be used in the chapter. If, however, you want to experiment with them
(highly encouraged!), you can get the library from http://packages.python.org/pyenchant/.
""")

class EnchantMock:

    def __init__(self):
        pass

    def check(self, word):
        return True

speller = EnchantMock()

filter_meta = json.load(open(filtered_meta, "r"))

def misspelled_fraction(p):
    tokens = p.split()
    if not tokens:
        return 0.0
    # step1 = sum(speller.check(t) for t in tokens)
    # step2 = len(tokens)
    # print('step: ',step1, step2, 1-float(step1)/step2)
    return 1 - float(sum(speller.check(t) for t in tokens)) / len(tokens)

def data(filename, col=None):
    count = 0
    for line in open(filename, "r"):
        data = line.strip().split("\t")
        count += 1
        if count <= 5:
            print(data, '\n')
                # check format
        Id, ParentId, IsAccepted, TimeToAnswer, \
            Score, Text, NumTextTokens, NumCodeLines, \
            LinkCount, NumImages = data

        if col:
            yield data[col]
        else:
            yield data

with open(chosen, "w") as f:
    for line in data(filtered):
        strId, ParentId, IsAccepted, TimeToAnswer, Score, Text,\
         NumTextTokens, NumCodeLines, LinkCount, NumImages = line
        Text = Text.strip()


if __name__ == "__main__":
    result = misspelled_fraction("1.1 2.2 3.3")
    print('result:', result)