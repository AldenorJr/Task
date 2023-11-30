from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def execute(event, context):
    url = event.get('url')
    chrome_options = Options()
    chrome_options.binary_location = '/opt/headless-chromium'

    chrome_option_list = [
        "disable-extensions",
        "disable-gpu",
        "no-sandbox",
        "headless", # for Jenkins
        "disable-dev-shm-usage", # Jenkins
        "window-size=800x600", # Jenkins
        "window-size=800,600",
        "disable-setuid-sandbox",
        # Add more options as needed
    ]

    for option in chrome_option_list:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=Service('/opt/chromedriver'), options=chrome_options)
    driver.get(url)
    return {"statusCode": 200, "body": driver.page_source}
