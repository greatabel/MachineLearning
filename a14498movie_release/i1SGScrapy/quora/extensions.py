from os.path import dirname, abspath
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_selenium_chrome():
    p = dirname(dirname(abspath(__file__)))
    chrome_path = p + "/chromedriver"
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument(" --window-size=1920x1080")
    chrome_options.add_argument(" --no-sandbox")
    # download the chrome driver from
    # https://sites.google.com/a/chromium.org/chromedriver/downloads

    # Set the browser settings to web driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_path)
    return driver
