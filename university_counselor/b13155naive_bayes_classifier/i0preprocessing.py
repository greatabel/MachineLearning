import re
from html.parser import HTMLParser
import csv

path = "data/samples.txt"
target_path = "data/i0processed.csv"


"""
去掉无用web标签
"""


def strip_tags(html):
    """
    Python中过滤HTML标签的函数
    >>> str_text=strip_tags("<font color=red>hello</font>")
    >>> print str_text
    hello
    """
    html = html.strip()
    html = html.strip("\n")

    result = []
    parser = HTMLParser()
    parser.handle_data = result.append
    parser.feed(html)
    parser.close()
    result = "".join(result)
    result = result.replace("\n", "")
    return result


"""
截取中文
"""


def extract_chinese(txt):
    pattern = re.compile("[\u4e00-\u9fa5]")
    return "".join(pattern.findall(txt))


"""
保存处理后list为csv
"""


def csv_writer_list_to_local(filename, lines):
    with open(filename, "a") as csvfile:
        fieldnames = ["sentiment", "content"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for l in lines:
            writer.writerow({"sentiment": 0, "content": l})


if __name__ == "__main__":
    with open(path) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    lines = []
    for line in content:
        if line != "" and len(line) > 5:

            # str = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", line)
            line = strip_tags(line)
            line = extract_chinese(line)
            line = line.replace("<", "").replace(">", "")
            line = line.replace("/", "")

            lines.append(line)

    print(len(lines), lines[0], "\n\n\n", lines[1])

    csv_writer_list_to_local(target_path, lines)
