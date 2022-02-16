import time
from termcolor import colored
from quora.profile_obj import Question
from quora.profile_writer import csv_profile_writer_to_local
import quora.config


drag_times = 1


def scrape_questions(profile_url, driver):
    # Getting to other user's link
    full_link = "https://www.quora.com/" + profile_url
    driver.get(full_link)

    t_answers = driver.find_elements_by_xpath(
        "//div[@class='q-text qu-medium qu-fontSize--small qu-color--red']")
    t_answers[0].click()
    # 找出answers数量
    answer_num = ''.join(filter(str.isdigit, t_answers[0].text))
    print('-'*20, colored('answer num:', 'blue'), answer_num)
    t = driver.find_elements_by_xpath(
            "//div[@class='q-text puppeteer_test_button_text qu-medium']")

    if 'Most Recent' in t[0].text:
        t[0].click()
        time.sleep(3)
        t0 = driver.find_elements_by_xpath(
            "//div[@class='q-text qu-fontSize--small qu-color--gray_dark']")
        # following 是第4个，因为默认第一个标签是选中的，不符合条件
        if 'All-Time Views' in t0[1].text:
            time.sleep(3)
            t0[1].click()
            time.sleep(2)
            # with open("page_source.html", "w") as f:
            #     f.write(driver.page_source)
            # driver.execute_script("window.a = document.getElementsByClassName('qt_read_more');")
            # driver.execute_script("for(var i=0; i<a.length; i+=1) { a[i].click(); }")
    i = 0
    while True:
        a = driver.execute_script("return document.body.scrollHeight;")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(7)
        b = driver.execute_script("return document.body.scrollHeight;")
        # 说明下啦到底了
        if a == b:
            print(colored('拉到底部了', 'red'))
            break

        # 拉到第几次停止
        i += 1
        if i >= drag_times:
            print(colored('拉到设置次数', 'magenta'))
            break
    questions = []
    elements = driver.find_elements_by_css_selector("div.q-text a")
    for element in elements:
        h = element.get_attribute("href")
        if h and 'topic' not in h and 'profile' not in h\
           and 'www.quora.com' in h and '-' in h:
            name = h + '/answer/' + profile_url
            print(name)
            questions.append(Question(name, followedby=profile_url))

    fields = ['name', 'followedby']
    csv_profile_writer_to_local(questions, filename=quora.config.questions, fieldnames=fields)
