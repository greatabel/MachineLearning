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

filtered_meta = json.load(open(filtered_meta, "r"))

def misspelled_fraction(p):
    tokens = p.split()
    if not tokens:
        return 0.0
    # step1 = sum(speller.check(t) for t in tokens)
    # step2 = len(tokens)
    # print('step: ',step1, step2, 1-float(step1)/step2)
    return 1 - float(sum(speller.check(t) for t in tokens)) / len(tokens)

def data(filename, col=None):
    # count = 0
    for line in open(filename, "r"):
        data = line.strip().split("\t")
        # count += 1
        # if count <= 5:
        #     print(data, '\n')
                # check format
        Id, ParentId, IsAccepted, TimeToAnswer, \
            Score, Text, NumTextTokens, NumCodeLines, \
            LinkCount, NumImages = data

        if col:
            yield data[col]
        else:
            yield data

posts_to_keep = set()

found_questions = 0

num_qestion_sample = 1000

filter_method = "negative_positive"  # warning: this does not retrieve many!
# filter_method = "only_one_per_class"
MaxAnswersPerQuestions = 10  # filter_method == "sample_per_question"

unaccepted_scores = {}

has_q_accepted_a = {}
num_q_with_accepted_a = 0
num_q_without_accepted_a = 0



for ParentId, posts in filtered_meta.items():
    assert ParentId != -1

    if len(posts) < 2:
        continue

    ParentId = int(ParentId)
    AllIds = set([ParentId])
    AcceptedId = None
    UnacceptedId = None
    UnacceptedIds = []
    UnacceptedScore = sys.maxsize

    NegativeScoreIds = []
    PositiveScoreIds = []

    if filter_method == "half-half":

        has_accepted_a = False
        for post in posts:
            Id, IsAccepted, TimeToAnswer, Score = post

            if IsAccepted:
                has_accepted_a = True
                break

        has_q_accepted_a[ParentId] = has_accepted_a

        if has_accepted_a:
            if num_q_with_accepted_a < num_qestion_sample / 2:
                num_q_with_accepted_a += 1
                posts_to_keep.add(ParentId)
        else:
            if num_q_without_accepted_a < num_qestion_sample / 2:
                num_q_without_accepted_a += 1
                posts_to_keep.add(ParentId)

        if num_q_without_accepted_a + num_q_with_accepted_a > num_qestion_sample:
            assert -1 not in posts_to_keep
            break

    else:

        for post in posts:
            Id, IsAccepted, TimeToAnswer, Score = post

            if filter_method == "all":
                AllIds.add(int(Id))

            elif filter_method == "only_one_per_class":
                if IsAccepted:
                    AcceptedId = Id
                elif Score < UnacceptedScore:
                    UnacceptedScore = Score
                    UnacceptedId = Id

            elif filter_method == "sample_per_question":
                if IsAccepted:
                    AcceptedId = Id
                else:
                    UnacceptedIds.append(Id)

            elif filter_method == "negative_positive":
                if Score < 0:
                    NegativeScoreIds.append((Score, Id))
                elif Score > 0:
                    PositiveScoreIds.append((Score, Id))

            else:
                raise ValueError(filter_method)

        added = False
        if filter_method == "all":
            posts_to_keep.update(AllIds)
            added = True
        elif filter_method == "only_one_per_class":
            if AcceptedId is not None and UnacceptedId is not None:
                posts_to_keep.add(ParentId)
                posts_to_keep.add(AcceptedId)
                posts_to_keep.add(UnacceptedId)
                added = True

        elif filter_method == "sample_per_question":
            if AcceptedId is not None and UnacceptedIds is not None:
                posts_to_keep.add(ParentId)
                posts_to_keep.add(AcceptedId)
                posts_to_keep.update(UnacceptedIds[:MaxAnswersPerQuestions])
                added = True

        elif filter_method == "negative_positive":
            if PositiveScoreIds and NegativeScoreIds:
                posts_to_keep.add(ParentId)

                posScore, posId = sorted(PositiveScoreIds)[-1]
                posts_to_keep.add(posId)

                negScore, negId = sorted(NegativeScoreIds)[0]
                posts_to_keep.add(negId)
                print("%i: %i/%i %i/%i" % (ParentId, posId,
                      posScore, negId, negScore))
                added = True

        if added:
            found_questions += 1

    if num_qestion_sample and found_questions >= num_qestion_sample:
        break

total = 0

with open(chosen, "w") as f:
    for line in data(filtered):
        strId, ParentId, IsAccepted, TimeToAnswer, Score, Text,\
         NumTextTokens, NumCodeLines, LinkCount, NumImages = line
        Text = Text.strip()
        total += 1

        Id = int(strId)

print(total)


if __name__ == "__main__":
    result = misspelled_fraction("1.1 2.2 3.3")
    print('result:', result)