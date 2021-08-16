import string
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import json
from tqdm.notebook import tqdm

from sklearn.base import TransformerMixin


def get_answer(text: str, answer: dict) -> str:
    """
    Gets a specific part of the text from an answer dictionary.
    """
    tokenized_text = text.split()

    return " ".join(tokenized_text[answer["start_token"] : answer["end_token"]])


def read_sample(
    filepath="data/mytrain.jsonl", n=100, offset=0, ignore_doc_text=False
) -> pd.DataFrame:
    with open(filepath, "r") as file:

        for e in range(offset):
            file.readline()

        line = json.loads(file.readline())
        if ignore_doc_text:
            del line["document_text"]

        series = pd.Series(data=list(line.values()), index=line.keys())
        dataset = series.to_frame().T
        for idx in tqdm(range(n - 1)):
            line = json.loads(file.readline())
            if ignore_doc_text:
                del line["document_text"]
            series = pd.Series(data=list(line.values()), index=line.keys())
            dataset = pd.concat(
                [dataset, series.to_frame().T], axis="rows", ignore_index=True
            )
    return dataset


# Custom transformer to implement sentence cleaning


class TextCleanerTransformer(TransformerMixin):
    def __init__(self, tokenizer, stemmer, regex_list, lower=True, remove_punct=True):
        self.tokenizer = tokenizer
        self.stemmer = stemmer
        self.regex_list = regex_list
        self.lower = lower
        self.remove_punct = remove_punct

    def transform(self, X, *_):
        X = list(map(self._clean_sentence, X))
        return X

    def _clean_sentence(self, sentence):

        # Replace given regexes
        for regex in self.regex_list:
            sentence = re.sub(regex[0], regex[1], sentence)

        # lowercase
        if self.lower:
            sentence = sentence.lower()

        # Split sentence into list of words
        words = self.tokenizer.tokenize(sentence)

        # Remove punctuation
        if self.remove_punct:
            # remove punct
            words = list(
                map(
                    lambda word: word.translate(
                        str.maketrans("", "", string.punctuation)
                    ),
                    words,
                )
            )
            # ignore empty strings
            words = list(filter(bool, words))

        # Stem words
        if self.stemmer:
            words = map(self.stemmer.stem, words)

        # Join list elements into string
        sentence = " ".join(words)

        return sentence

    def fit(self, *_):
        return self
