from textblob import TextBlob
from werkzeug.utils import secure_filename
import my_model_loader
import os
from os import scandir


def anlaysis(text):
    total = 0
    blob = TextBlob(text)
    blob.tags  # [('The', 'DT'), ('titular', 'JJ'),
    #  ('threat', 'NN'), ('of', 'IN'), ...]
    # print('@', blob.tags)
    blob.noun_phrases  # WordList(['titular threat', 'blob',
    #            'ultimate movie monster',
    #            'amoeba-like mass', ...])
    # print('#', blob.noun_phrases)
    for sentence in blob.sentences:
        # print(sentence.sentiment.polarity)
        total += sentence.sentiment.polarity

    # ------

    dir_entries = scandir("upload/")
    for text_file in dir_entries:
        if "DS_Store" not in text_file.name:
            filename = secure_filename(text_file.name)
            t = os.path.join("upload", filename)
            r = my_model_loader.classify(t)

    return blob.noun_phrases, total


# if __name__ == "__main__":
#     anlaysis('The fox and the wolf give you New Year greetings, so terrible')
