import re
from collections import Counter

import matplotlib.pyplot as plt

'''
requirement:
能统计下我们那个api代理已经有多少人用了吗？
大致问了哪些问题能查到吗？写报告用

'''



# 读取日志文件
with open('flask.log') as f:
    log_text = f.read()

# 定义正则表达式
ip_regex = r'from IP (\d+\.\d+\.\d+\.\d+)'
session_regex = r'\[(.*?)\]'
search_regex = r'with search input \'(.*?)\''

# 匹配所有的ip、session和search
ips = re.findall(ip_regex, log_text)
sessions = re.findall(session_regex, log_text)
searches = re.findall(search_regex, log_text)

# 统计不同ip的数量和列表
ip_count = {}
for ip in ips:
    if ip not in ip_count:
        ip_count[ip] = 1
    else:
        ip_count[ip] += 1
ip_list = list(ip_count.keys())

# 统计不同session的数量
session_count = len(set(sessions))

# 统计头20个问得最多的
search_count = {}
for search in searches:
    if search not in search_count:
        search_count[search] = 1
    else:
        search_count[search] += 1
top_searches = sorted(search_count.items(), key=lambda x: x[1], reverse=True)[:20]

# 输出结果
print('1', '#'*20)
print("不同ip的数量：", len(ip_list))
print("不同ip的列表：", ip_list)

print('2', '#'*20)
print("不同session的数量：【1次浏览器未关闭，都算1个session】", session_count)

print('3', '#'*20)
print("头20个问得最多的：")
for search, count in top_searches:
    print(f"{search}: {count}")



import datetime

# 读取日志文件
with open("flask.log", "r") as file:
    lines = file.readlines()

# print(lines[0], '\n', lines[-1])
# print('#'*20)
# print(lines[0].strip().split(' - ')[0],lines[-1].strip().split(' - ')[0])

# 获取第一行和最后一行的日期时间
first_line = datetime.datetime.strptime(lines[0].strip().split(' - ')[0], "%Y-%m-%d %H:%M:%S,%f")
last_line = datetime.datetime.strptime(lines[-1].strip().split(' - ')[0], "%Y-%m-%d %H:%M:%S,%f")

print(first_line)
print(last_line)
# 计算日期时间差
time_delta = last_line - first_line

# 计算小时差
hours = time_delta.total_seconds() / 3600

print('4', '#'*20)
print(f"日志文件中从第一行到最后1行的日期间隔为 {hours:.2f} 小时")
print('-------------------')






with open('flask.log', 'r') as f:
    total_requests = 0
    for line in f:
        if "POST request to /get_response" in line:
            total_requests += 1
    print('5', '#'*20)
    print("Total requests: ", total_requests)


# 提取日期数据
dates = re.findall(r'^(\d{4}-\d{2}-\d{2})', log_text, flags=re.MULTILINE)

# 统计每天的访问次数
daily_counts = Counter(dates)

# 可视化每天的访问次数
plt.bar(daily_counts.keys(), daily_counts.values())
plt.title('Request Per date')
plt.xlabel('Date')
plt.ylabel('Access Count')
plt.show()


