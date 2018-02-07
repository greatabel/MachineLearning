import pandas as pd # pandas是python的数据格式处理类库

# 加载泰坦尼克号生存预测数据集
data_train = pd.read_csv("../data/titanic/train.csv")
print(data_train.info())

sur_count = data_train.groupby('Survived').count()
print(sur_count)