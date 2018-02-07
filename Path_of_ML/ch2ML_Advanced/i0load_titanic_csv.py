import pandas as pd # pandas是python的数据格式处理类库

# 加载泰坦尼克号生存预测数据集
data_train = pd.read_csv("../data/titanic/train.csv")
print(data_train.info())

sur_count = data_train.groupby('Survived').count()
print(sur_count)

h3 = data_train.head(3)
print(h3)

# 处理数据缺失
def set_missing_ages(p_df):
    p_df.loc[(p_df.Age.isnull()), 'Age'] = p_df.Age.dropna().mean()
    return p_df

df = set_missing_ages(data_train)


# 归一化数值数据
import sklearn.preprocessing as preprocessing

scaler = preprocessing.StandardScaler()
df['Age_scaled'] = scaler.fit_transform(data_train['Age'].values.reshape(-1, 1))
df['Fare_scaled'] = scaler.fit_transform(data_train['Fare'].values.reshape(-1, 1))

# 处理类别意义的特征
def set_cabin_type(p_df):
    p_df.loc[(p_df.Cabin.notnull()), 'Cabin'] = "Yes"
    p_df.loc[(p_df.Cabin.isnull()), 'Cabin'] = "No"
    return p_df
df = set_cabin_type(df)

dummies_pclass = pd.get_dummies(data_train['Pclass'], prefix='Pclass')
ph3 = dummies_pclass.head(3)
print('ph3=', ph3)

dummies_embarked = pd.get_dummies(data_train['Embarked'], prefix='Embarked')
dummies_sex = pd.get_dummies(data_train['Sex'], prefix='Sex')

df = pd.concat([df, dummies_embarked, dummies_sex, dummies_pclass], axis=1)

# noinspection PyUnresolvedReferences
df.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

# 选择哪些特征作为训练特征
train_df = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
print(train_df.head(1))

train_np = train_df.as_matrix()
y = train_np[:, 0]
x = train_np[:, 1:]

from abupy import AbuML
titanic = AbuML(x, y, train_df)

titanic.estimator.logistic_classifier()
s = titanic.cross_val_accuracy_score()
print(s)
