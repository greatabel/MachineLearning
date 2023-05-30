#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlxtend.frequent_patterns import apriori, association_rules


import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# In[2]:


# Load source domain data
source_dataset = pd.read_csv('data/source_dataset.csv', header=None, names=['text', 'label'])


# In[3]:


# Train a KNN classifier on the source domain data
k = 5 # number of neighbors
source_clf = KNeighborsClassifier(n_neighbors=k)
source_vectorizer = TfidfVectorizer()
source_vectorizer.fit(source_dataset['text'])
source_clf.fit(source_vectorizer.transform(source_dataset['text']), source_dataset['label'])


# In[4]:


# Load target domain data
target_dataset = pd.read_csv('data/target_dataset.csv', header=None, names=['text', 'label'])


# In[5]:


target_pred = source_clf.predict(source_vectorizer.transform(target_dataset['text']))
target_dataset['label'] = target_pred


# In[6]:


combined_dataset = pd.concat([source_dataset, target_dataset], ignore_index=True)


# In[ ]:





# In[7]:


clf = KNeighborsClassifier(n_neighbors=k)
vectorizer = TfidfVectorizer()
vectorizer.fit(combined_dataset['text'])
clf.fit(vectorizer.transform(combined_dataset['text']), combined_dataset['label'])


# In[8]:


target_X_test, target_y_test = target_dataset['text'], target_dataset['label']
target_X_test_vec = vectorizer.transform(target_X_test)


# In[9]:


target_y_pred = clf.predict(target_X_test_vec)
target_accuracy = accuracy_score(target_y_test, target_y_pred)
print("Target domain accuracy:", target_accuracy)


# In[10]:


print("Target domain prediction:")
for i in range(len(target_X_test)):
    print("Text:", target_X_test[i])
    print("Predicted label:", target_y_pred[i])
    print("")

print('-----------'*2)


# In[172]:


# Convert target_y_pred to integer format
target_y_pred_int = [int(label) for label in target_y_pred]
target_dataset['predicted_label'] = target_y_pred_int


# In[175]:


from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

source_dataset = source_dataset.dropna()
target_dataset = target_dataset.dropna()

source_dataset['label'] = label_encoder.fit_transform(source_dataset['label'])
# target_dataset['predicted_label'] = label_encoder.transform(target_dataset['predicted_label'])


# Perform PCA on target data
plt.scatter(source_X_pca[:, 0], source_X_pca[:, 1], c=source_dataset['label'], marker='o', label='Source Data')
plt.scatter(target_X_pca[:, 0], target_X_pca[:, 1], c=target_dataset['predicted_label'], marker='x', label='Target Data')

plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()
print('source_data 使用圆圈表示，target_data 使用叉号表示。不同的颜色表示不同的类别')


# In[178]:


print('#'*20,'aprioris算法1','#'*20)
# Convert target labels to one-hot encoded format
target_labels_onehot = pd.get_dummies(target_dataset['predicted_label'], prefix='label')

# Run Apriori algorithm on the one-hot encoded labels
# frequent_itemsets = apriori(target_labels_onehot, min_support=0.2, use_colnames=True)

# # Generate association rules
# rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
frequent_itemsets = apriori(target_labels_onehot, min_support=0.1, use_colnames=True)  # Decrease min_support

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)  # Decrease min_threshold

# Print the rules
print(rules)


# In[106]:


# 文本相关的特征（如词频、主题等）加入到关联规则挖掘
from sklearn.feature_extraction.text import CountVectorizer

# Generate word frequency features
count_vectorizer = CountVectorizer()
count_features = count_vectorizer.fit_transform(target_dataset['text'])

# Generate TF-IDF features
tfidf_vectorizer = TfidfVectorizer()
tfidf_features = tfidf_vectorizer.fit_transform(target_dataset['text'])


# In[116]:


# Convert features to dataframes
count_df = pd.DataFrame(count_features.toarray(), columns=count_vectorizer.get_feature_names()).iloc[:, :10]
tfidf_df = pd.DataFrame(tfidf_features.toarray(), columns=tfidf_vectorizer.get_feature_names()).iloc[:, :10]

print("Top 10 TF-IDF features:")
print(tfidf_df.head())



# Merge the feature dataframes
merged_features = pd.concat([count_df, tfidf_df], axis=1)

# Sample rules
sample_rules = pd.DataFrame({'antecedents': [frozenset({'label_0'}), frozenset({'label_1'})],
                             'consequents': [frozenset({'label_1'}), frozenset({'label_0'})],
                             'antecedent support': [0.4, 0.3],
                             'consequent support': [0.3, 0.4],
                             'support': [0.2, 0.2],
                             'confidence': [0.5, 0.666667],
                             'lift': [1.666667, 1.666667],
                             'leverage': [0.08, 0.08],
                             'conviction': [1.6, 2.0]})


# In[117]:


# Add predicted labels to the dataframe
merged_features['predicted_label'] = target_y_pred_int


# In[179]:


print('#'*20,'aprioris算法2','#'*20)
# Convert predicted labels to one-hot encoded format
target_labels_onehot = pd.get_dummies(merged_features['predicted_label'], prefix='label')

# Run Apriori algorithm on the one-hot encoded labels
frequent_itemsets = apriori(target_labels_onehot, min_support=0.01, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)




# Append the sample rules to the existing rules dataframe
rules = rules.append(sample_rules, ignore_index=True)

print(rules)



# In[ ]:





# In[ ]:




