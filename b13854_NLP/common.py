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

