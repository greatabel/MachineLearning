import numpy as np  # linear algebra

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
import json


print("---- 1. let us check the first document in the dataset ----")
df = pd.read_csv("datasets/passenger_dirty.csv")
print(df.head())


doc_text_words = df["PlaceName"].apply(lambda x: len(x.split(" ")))
plt.figure(figsize=(12, 6))
sns.distplot(doc_text_words.values, kde=True, hist=False).set_title(
    "Distribution of text word count of all PlaceName"
)
plt.show()
# plt.savefig("reports/i2.png")
