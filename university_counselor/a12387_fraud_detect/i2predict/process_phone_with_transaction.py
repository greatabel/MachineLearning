#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import numpy as np
import csv
import pickle


def save_obj(obj, name):
    with open(name + ".pkl", "wb") as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + ".pkl", "rb") as f:
        return pickle.load(f)


device_list = []


def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


# 生成手机号
num = 247
for i in range(0, num):
    phone = create_phone()
    print(phone)
    device_list.append(phone)

device_list.append("device101")
device_list.append("device122")
device_list.append("device332")

print(len(device_list), "#" * 20)


with open("sample_transactions.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)


print(data[1], len(data[1]))

numline = len(data)

lst = range(numline)
divide = np.array_split(lst, num + 4)
print(len(divide), "-" * 20, "divide")
k_v = {}

i = 0
for d in device_list:
    myrange = divide[i]
    record = data[i]
    print(i, d, myrange, record[30])
    if record[30] != "Class":
        k_v[d] = record[30]
    else:
        k_v[d] = 0
    i += 1

save_obj(k_v, "k_v")
# with open("device_list.txt", "w") as output:
#     output.write(str(device_list))
