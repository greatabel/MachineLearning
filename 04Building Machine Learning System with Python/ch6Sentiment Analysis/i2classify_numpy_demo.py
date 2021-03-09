import numpy as np

# 生成0，3 之间随机数 30个
arr = np.random.randint(0, 3, 30)

def map_to_sentiment(x):
    if x == 0:
        return "negative"
    elif x == 1:
        return "neutral"
    elif x == 2:
        return "positive"
vfunc = np.vectorize(map_to_sentiment)
sentiments = vfunc(arr)
print(sentiments)

classes = np.unique(sentiments)
print('classes:', classes)

for c in classes:
    print("#%s: %i" %(c, sum(sentiments==c)))
