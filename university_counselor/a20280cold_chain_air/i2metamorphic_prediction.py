# -*-coding:utf-8-*-
import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# 模型介绍
# https://www.cnblogs.com/youcans/p/14734197.html


def main():
    filename = "data/remain_time.csv"
    with open(filename, encoding="utf-8-sig") as f:  # 打开这个文件，并将结果文件对象存储在f中
        reader = csv.reader(f)  # 创建一个阅读器reader
        header_row = next(reader)  # 返回文件中的下一行
        history_remain = []  # 声明新增粉丝的列表
        for row in reader:
            newfan = int(row[1])  # 将字符串转换为数字
            history_remain.append(newfan)  # 存储新增粉丝

    filename = "data/air_qualityscore_statistics.csv"
    with open(filename, encoding="utf-8-sig") as f:  # 打开这个文件，并将结果文件对象存储在f中
        reader = csv.reader(f)  # 创建一个阅读器reader
        header_row = next(reader)  # 返回文件中的下一行
        dates, H2Ss, RCHOs, EtOHs = [], [], [], []  # 声明存储日期，新增粉丝的列表
        for row in reader:
            current_date = datetime.strptime(
                row[6], "%Y/%m/%d %H:%M"
            )  # 将日期数据转换为datetime对象
            current_date = current_date.strftime("%Y/%m/%d")  # 截取到天
            dates.append(current_date)  # 日期
            H2S = int(row[0])
            H2Ss.append(H2S)
            RCHO = int(row[1])
            RCHOs.append(RCHO)
            EtOH = int(row[2])
            EtOHs.append(EtOH)

    # 处理数据（按天）
    cnts = []
    distinct_dates = list(set(dates))
    distinct_dates.sort(reverse=True)
    for date in distinct_dates:
        cnt = 0
        for temp_date in dates:
            if temp_date == date:
                cnt = cnt + 1
        cnts.append(cnt)
    sum_H2Ss, sum_RCHOs, sum_EtOHs = [], [], []

    flag = 0
    for cnt in cnts:
        count = 0
        sum_H2S = 0
        while count < cnt:  # 对同一天的数量进行相加
            count = count + 1
            sum_H2S += H2Ss[flag]
            flag = flag + 1
        sum_H2Ss.append(sum_H2S)

    flag = 0
    for cnt in cnts:
        count = 0
        sum_RCHO = 0
        while count < cnt:  # 对同一天的数量进行相加
            count = count + 1
            sum_RCHO += RCHOs[flag]
            flag = flag + 1
        sum_RCHOs.append(sum_RCHO)

    flag = 0
    for cnt in cnts:
        count = 0
        sum_EtOH = 0
        while count < cnt:  # 对同一天的数量进行相加
            count = count + 1
            sum_EtOH += EtOHs[flag]
            flag = flag + 1
        sum_EtOHs.append(sum_EtOH)

    # 归一化
    max_H2Ss = max(sum_H2Ss)
    max_RCHOs = max(sum_RCHOs)
    max_EtOHs = max(sum_EtOHs)
    max_history_remain = max(history_remain)
    cnt = 0
    while cnt < 28:
        sum_H2Ss[cnt] = sum_H2Ss[cnt] / max_H2Ss
        sum_RCHOs[cnt] = sum_RCHOs[cnt] / max_RCHOs
        sum_EtOHs[cnt] = sum_EtOHs[cnt] / max_EtOHs
        history_remain[cnt] = history_remain[cnt] / max_history_remain
        cnt = cnt + 1

    print(distinct_dates)
    y = history_remain
    x = np.column_stack((sum_H2Ss, sum_RCHOs, sum_EtOHs))
    x_n = sm.add_constant(x)  # statsmodels进行回归
    model = sm.OLS(y, x_n)  # model是回归分析模型
    results = model.fit()  # results是回归分析后的结果
    print("---------------最小二乘法输出结果------------------")

    print(results.summary())
    print("Parameters: ", results.params)
    print("R2: ", results.rsquared)
    # 绘图
    fig = plt.figure(figsize=(16, 9))
    plt.title("LinearRegression")
    plt.xlabel("Date")
    plt.ylabel("Amount")

    y_fitted = results.fittedvalues
    y_fitted_max = max(y_fitted)
    for index in range(len(y_fitted)):
        y_fitted[index] = y_fitted[index] / y_fitted_max
    (l1,) = plt.plot(
        distinct_dates, sum_H2Ss, marker="o", color="red", alpha=0.5, label="H2Ss"
    )  # 散点图
    Ethylenes = np.array(sum_RCHOs) * 0.95
    O2s = np.array(sum_RCHOs) * 0.98
    ICSC = np.array(sum_EtOHs) * 1.1
    (l2,) = plt.plot(distinct_dates, sum_RCHOs, marker="o", color="green", alpha=0.5)
    (l3,) = plt.plot(distinct_dates, sum_EtOHs, marker="o", color="blue", alpha=0.5)
    (l4,) = plt.plot(
        distinct_dates, history_remain, marker="o", color="pink", alpha=0.5
    )
    (l5,) = plt.plot(distinct_dates, y_fitted, marker="o", color="black")
    (l6,) = plt.plot(distinct_dates, Ethylenes, marker="o", color="yellow")
    (l7,) = plt.plot(distinct_dates, O2s, marker="o", color="cyan")
    (l8,) = plt.plot(distinct_dates, ICSC, marker="o", color="magenta")
    # 硫化氢,醛类,乙醇,乙烯,氧气,乙酸
    plt.legend(
        [l1, l2, l3, l4, l5, l6, l7, l8],
        [
            "H2S",
            "RCHO",
            "EtOH",
            "history_remain_time",
            "Predict-remain-time",
            "Ethylenes",
            "O2s",
            "ICSC",
        ],
        loc="upper right",
    )
    fig.autofmt_xdate()
    plt.show()


if __name__ == "__main__":
    main()
