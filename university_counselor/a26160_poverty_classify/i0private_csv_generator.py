import random
import pandas as pd

def generate_csv(num_records):
    data = []

    for i in range(num_records):
        education_level = random.choice(['本科', '硕士', '博士'])
        age = random.randint(20, 30)
        housing_condition = random.randint(50, 200)

        if education_level == '本科':
            financial_aid_prob = random.uniform(0.6, 0.9)
        elif education_level == '硕士':
            financial_aid_prob = random.uniform(0.3, 0.6)
        else:
            financial_aid_prob = random.uniform(0.1, 0.3)

        financial_aid = int(random.random() < financial_aid_prob)

        # 使 poverty_level 和 financial_aid 正相关
        if financial_aid == 1:
            poverty_level = random.choice([1, 2])
        else:
            poverty_level = random.choice([2, 3])

        row = {
            'id': i + 1,
            'age': age,
            'gender': random.choice(['M', 'F']),
            'education_level': education_level,
            'major': random.choice(['计算机科学', '生物科学', '物理学']),
            'family_income': random.randint(30000, 100000),
            'family_size': random.randint(2, 6),
            'housing_condition': housing_condition,
            'financial_aid': financial_aid,
            'poverty_level': poverty_level
        }

        data.append(row)

    df = pd.DataFrame(data)
    df.to_csv('generated_data.csv', index=False)

generate_csv(10000)
