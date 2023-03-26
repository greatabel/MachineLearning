#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder


# In[7]:


# 1. 加载CSV数据集
# data = pd.read_csv('poverty_data.csv')
data = pd.read_csv('sample.csv')

# 2. 数据预处理
# 对分类变量进行编码
gender_encoder = LabelEncoder()
data['gender'] = gender_encoder.fit_transform(data['gender'])

education_level_encoder = LabelEncoder()
data['education_level'] = education_level_encoder.fit_transform(data['education_level'])

major_encoder = LabelEncoder()
data['major'] = major_encoder.fit_transform(data['major'])

financial_aid_encoder = LabelEncoder()
data['financial_aid'] = financial_aid_encoder.fit_transform(data['financial_aid'])


# In[8]:


# 提取特征和标签
X = data.drop(columns=['id', 'poverty_level']).values
y = data['poverty_level'].values

# 拆分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 特征缩放
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[9]:



# 3. 构建深度学习模型
num_features = X_train.shape[1]
num_classes = len(np.unique(y_train))

model = tf.keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(num_features,)),
    layers.Dropout(0.2),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 使用早停法防止过拟合
early_stopping = tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)

history = model.fit(X_train, y_train,
                    epochs=100,
                    batch_size=32,
                    validation_data=(X_test, y_test),
                    callbacks=[early_stopping])

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {test_loss}, Test accuracy: {test_accuracy}")




# In[10]:


# 假设这是一个实际学生的数据情况
sample_data = {
    'age': 23,
    'gender': 'M',
    'education_level': '本科',
    'major': '计算机科学',
    'family_income': 50000,
    'family_size': 4,
    'housing_condition': 70,
    'financial_aid': 0
}

# 对分类变量进行编码
sample_data['gender'] = gender_encoder.transform([sample_data['gender']])[0]
sample_data['education_level'] = education_level_encoder.transform([sample_data['education_level']])[0]
sample_data['major'] = major_encoder.transform([sample_data['major']])[0]

# 转换为NumPy数组并应用特征缩放
sample_data_array = np.array(list(sample_data.values())).reshape(1, -1)
sample_data_scaled = scaler.transform(sample_data_array)

# 使用模型进行预测
prediction = model.predict(sample_data_scaled)

# 输出预测结果
predicted_class = np.argmax(prediction)
print(f"预测的贫困等级: {predicted_class}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




