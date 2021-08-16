import numpy as np  # linear algebra

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
import json


from common import get_answer, read_sample

print("---- 1. let us check the first document in the dataset ----")
df = read_sample(n=3)
print(df.head())

print("---- 2. Distribution of text word count of 100 docs ----")
df = read_sample(n=100)
doc_text_words = df["document_text"].apply(lambda x: len(x.split(" ")))
plt.figure(figsize=(12, 6))
sns.distplot(doc_text_words.values, kde=True, hist=False).set_title(
    "Distribution of text word count of 100 docs"
)
plt.savefig("i2.png")

print("---- 3. let us check the first document in the dataset ----")


def myprocess(n=10):
    df = read_sample(n=n, ignore_doc_text=True)
    df["yes_no"] = df.annotations.apply(lambda x: x[0]["yes_no_answer"])
    df["long"] = df.annotations.apply(
        lambda x: [x[0]["long_answer"]["start_token"], x[0]["long_answer"]["end_token"]]
    )
    df["short"] = df.annotations.apply(lambda x: x[0]["short_answers"])
    return df


df = myprocess(500)
display(
    df.long.apply(
        lambda x: "Answer Doesn't exist" if x[0] == -1 else "Answer Exists"
    ).value_counts(normalize=True)
)

mask_answer_exists = (
    df.long.apply(lambda x: "Answer Doesn't exist" if x == -1 else "Answer Exists")
    == "Answer Exists"
)

print("---- 4. Distribution of Yes and No Answers ----")
yes_no_dist = df[mask_answer_exists].yes_no.value_counts(normalize=True)
print(yes_no_dist)


print("---- 5. short answers ----")
short_dist = (
    df[mask_answer_exists]
    .short.apply(
        lambda x: "Short answer exists" if len(x) > 0 else "Short answer doesn't exist"
    )
    .value_counts(normalize=True)
)
plt.figure(figsize=(8, 6))
sns.barplot(x=short_dist.index, y=short_dist.values).set_title(
    "Distribution of short answers in answerable questions"
)
plt.savefig("i5.png")


print("---- 6. multiple short answers to a question ----")
short_size_dist = df[mask_answer_exists].short.apply(len).value_counts(normalize=True)
short_size_dist_pretty = pd.concat(
    [
        short_size_dist.loc[
            [
                0,
                1,
            ],
        ],
        pd.Series(short_size_dist.loc[2:].sum(), index=[">=2"]),
    ]
)
short_size_dist_pretty = short_size_dist_pretty.rename(
    index={
        0: "No Short answer",
        1: "1 Short answer",
        ">=2": "More than 1 short answers",
    }
)
plt.figure(figsize=(12, 6))
sns.barplot(x=short_size_dist_pretty.index, y=short_size_dist_pretty.values).set_title(
    "Distribution of Number of Short Answers in answerable questions"
)
plt.savefig("i6.png")
