import numpy as np  # linear algebra

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
import json


print("---- 1. let us check the first document in the dataset ----")
df = pd.read_csv("datasets/placename.csv")
print(df.head())


doc_text_words = df["PlaceNameMentioned"].apply(lambda x: len(x.split(" ")))
plt.figure(figsize=(12, 6))
sns.distplot(doc_text_words.values, kde=True, hist=False).set_title(
    "Distribution of text word count of all PlaceNameMentioned"
)
plt.show()
# plt.savefig("reports/i3I.png")




names = ['London Central Hostel"', '"Coca-Cola London Eye']
values = [6, 4]

plt.figure(figsize=(9, 3))

# plt.subplot(131)
plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
plt.suptitle('place frequencey')
# plt.savefig("reports/i3II.png")
plt.show()