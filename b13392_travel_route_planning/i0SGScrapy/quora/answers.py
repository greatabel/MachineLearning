import time
from termcolor import colored
import requests
import quora.config
from common import convert_si_to_number


def scrape_answers(url, driver):
    print('抓取内容和图片:', colored(url, 'red'))
    driver.get(url)
    time.sleep(3)
    imgsrc = driver.find_elements_by_xpath(
        "//img[contains(@class,'q-image qu-display--block qu-borderRadius--small')]")
    for ele in imgsrc:
        x = ele.get_attribute("src")
        pic_last = x.rsplit('/', 1)[-1].rsplit('-', 1)[-1].replace('.webp', '')
        driver.execute_script("arguments[0].innerHTML = arguments[1]", ele, '#' + pic_last)
        print('image =>', x)
        get_image(x, pic_last + ".webp")

    t_answers = driver.find_elements_by_xpath(
        "//div[@class='q-text']")
    print(t_answers[0].text, '\n')

    # 获取浏览数和点赞数
    view_upvoter_div = driver.find_elements_by_xpath(
        "//div[contains(@class, 'q-text qu-mt--small qu-color--gray_light qu-fontSize--small')]")

    splits = view_upvoter_div[0].text.split(' ')
    views = splits[0]
    upvoter = splits[2]
    print('#'*20, view_upvoter_div[0].text)
    print(convert_si_to_number(views), convert_si_to_number(upvoter))


def get_image(imageurl, name):
    http_proxy = "http://127.0.0.1:1087"
    https_proxy = "https://127.0.0.1:1087"
    proxydict = {
                  "http": http_proxy,
                  "https": https_proxy,
                }
    data = requests.get(imageurl, proxies=proxydict).content
    with open(quora.config.img_folder + '/' + name, 'wb') as handler:
        handler.write(data)
