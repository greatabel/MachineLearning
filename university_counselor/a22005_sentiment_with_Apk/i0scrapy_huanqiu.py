from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from lxml import etree
import os
import requests
import csv
import time


chrome_path = "/Users/abel/AbelProject/MachineLearning/a22005_sentiment_with_Apk/chrome/chromedriver"
data_folder = "data"


chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(chrome_path, options=chrome_options)
browser.implicitly_wait(8)


def download_page(url, news_type):
    time.sleep(1)
    browser.get(url)
    sleep(1)
    for one in range(5):
        # 翻到页底
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(1)
    # 拿到页面源代码
    source = browser.page_source
    parse_page(url, source)


# 对新闻列表页面进行解析
def parse_page(url, html):
    # 创建etree对象
    tree = etree.HTML(html)
    new_lst = tree.xpath('//ul[@id="recommend"]//a')
    for one_new in new_lst:
        title = one_new.xpath(".//h4/text()")[0]
        link = url + one_new.xpath("./@href")[0]
        try:
            write_in(title, link, news_type)
        except Exception as e:
            print(e)


# 将其写入到文件
def write_in(title, link, news_type):
    alist = []
    print("开始写入新闻:{}".format(title))
    # response = requests.get(url=link)
    browser.get(link)
    sleep(1)
    # 再次翻页到底
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 拿到页面源代码
    source = browser.page_source
    tree = etree.HTML(source)

    alist.append(news_type)
    # title = title.replace('?', '')
    alist.append(title)

    con_link = link
    alist.append(con_link)

    content_lst = tree.xpath('//section[@data-type="rtext"]/p')
    con = ""
    if content_lst:
        for one_content in content_lst:
            if one_content.text:
                con = con + "\n" + one_content.text.strip()
        alist.append(con)

        # post_time_source = tree.xpath('//div[@class="left-t"]')[0].text

        post_time = tree.xpath('//div[@class="metadata-info"]//p[@class="time"]')[
            0
        ].text
        alist.append(post_time)

        post_source = tree.xpath(
            '//div[@class="metadata-info"]//span[@class="source"]//a'
        )
        if post_source:
            post_source = post_source[0].text
        else:
            post_source = tree.xpath(
                '//div[@class="metadata-info"]//span[@class="source"]//span'
            )[0].text
        alist.append(post_source)
        # 1. 创建文件对象
        f = open(data_folder + "/huanqiu.csv", "a+", encoding="utf-8", newline="")
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        print(alist)
        print("------" * 5, "downloading", "------" * 5)
        csv_writer.writerow(alist)
        f.close()


if __name__ == "__main__":
    urls = [
        # "https://world.huanqiu.com/",
        "https://china.huanqiu.com/",
        "https://mil.huanqiu.com/",
    ]

    news_types = [
        # "国际",
        "国内",
        "军事",
    ]
    i = 0
    for url in urls:
        if not os.path.exists(data_folder):
            os.mkdir(data_folder)
        news_type = news_types[i]
        download_page(url, news_type)
        i = i + 1
    browser.quit()
