from os import environ
import time
from selenium.webdriver.common.keys import Keys

from common import csv_reader_from_localfile
import quora.config
from quora.extensions import get_selenium_chrome
from quora.following import scrape_following
from quora.questions import scrape_questions
from quora.answers import scrape_answers


quorabot_login_email = environ.get('QUORABOT_LOGIN_EMAIL')
quorabot_login_password = environ.get('QUORABOT_LOGIN_PASSWORD')


# 暂时不需要抓取需要登陆到信息，但功能保留
# 将来可能抓取shares 的信息就需要登陆
def auto_login(driver):
    driver.get("https://www.quora.com/?prevent_redirect=1")
    time.sleep(3)
    form = driver.find_element_by_class_name('regular_login')
    email = form.find_element_by_name("email")
    email.send_keys(quorabot_login_email)
    password = form.find_element_by_name("password")
    password.send_keys(quorabot_login_password)
    password.send_keys(Keys.RETURN)
    time.sleep(3)


def scrape():
    driver = get_selenium_chrome()
    driver.get('https://www.quora.com/topic/Military-History-and-Wars-1')
    time.sleep(3)
    # 暂时不需要登陆
    # auto_login(driver)

    start_profiles = csv_reader_from_localfile(quora.config.start_profiles)
    for row in start_profiles:
        profile_url = row['url'].rsplit('/', 1)[-1]
        scrape_following(profile_url, driver)

        scrape_questions(profile_url, driver)

    question_urls = csv_reader_from_localfile(quora.config.questions)
    for row in question_urls:
        scrape_answers(row['name'], driver)
    driver.quit()
