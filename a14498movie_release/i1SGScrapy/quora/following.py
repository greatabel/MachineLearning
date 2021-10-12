import time
from termcolor import colored
import pprint

import quora.config
from quora.profile_obj import Profile, merge_lists
from quora.profile_writer import csv_profile_writer_to_local

# 限制下拉次数
drag_times = 1


def scrape_following(profile_url, driver):
    # Getting to other user's link
    full_link = "https://www.quora.com/" + profile_url
    driver.get(full_link)

    t = driver.find_elements_by_xpath(
            "//div[@class='q-text qu-medium qu-fontSize--small qu-color--gray_light']")

    print(full_link, '-'*20, colored('菜单项中关注者按钮位置内容:', 'red'), t[4].text, '\n')

    # following 是第4个，因为默认第一个标签是选中的，不符合条件
    if 'Following' in t[4].text:
        t[4].click()
    elif 'More' in t[4].text:
        # 一行太长，following在more下面的情况,点击more
        t[4].click()
        t = driver.find_elements_by_xpath(
                "//div[@class='q-text qu-fontSize--small qu-color--gray_dark']")
        print(colored('需要点击more展开:', 'blue'), t[0].text)
        t[0].click()

    i = 0
    name_url_list = []
    name_bio_list = []
    # Let's retrieve the whole page so that you don't miss a single answer
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

    ls = driver.find_elements_by_tag_name("a")
    for l in ls:
        if l.text and 'profile' in l.get_attribute('href') and \
           profile_url not in l.get_attribute('href'):
            # print(l.text, l.get_attribute('href'))
            name_url_list.append(Profile(l.text, url=l.get_attribute('href'),
                                         followedby=profile_url))

    # 名字，简介的获取
    t = driver.find_elements_by_xpath(
            "//div[@class='q-flex qu-alignItems--center qu-py--small" +
            " qu-borderBottom qu-tapHighlight--none']")
    for name_bio in t:
        # print(name_bio.text)
        pairs = name_bio.text.split(',', 1)
        if len(pairs) > 1:
            name_bio_list.append(Profile(pairs[0], bio=pairs[1], followedby=profile_url))
        else:
            name_bio_list.append(Profile(pairs[0], followedby=profile_url))

    profiles = merge_lists(name_url_list, name_bio_list)
    pprint.pprint(profiles)
    fields = ['name', 'url', 'bio', 'followedby']
    csv_profile_writer_to_local(profiles, filename=quora.config.followings, fieldnames=fields)
