import requests
import proxylist
import random
import time
import string
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

chrome_options = Options()

#run headless
chrome_options.add_argument("--headless")

#removes browser control flag
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

#set browser size
chrome_options.add_argument("--start-maximized")

#mute audio
chrome_options.add_argument("--mute-audio")

#set user-agent
chrome_options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95 Safari/537.36")

#disable chrome password/security popups
prefs = {"credentials_enable_service": False,
     "profile.password_manager_enabled": False}
chrome_options.add_experimental_option("prefs", prefs)

#modifying navigator.webdriver flag to prevent selenium detection
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

#set IP
def set_ip():
    ip = random.choice(proxylist.proxies)
    proxy = {"http":"http://" + proxylist.auth + ip}
    chrome_options.add_argument('--proxy-server=' % proxy)
    print('Running from', ip)

video_links = [
    'http://www.youtube.com/watch?v=aWoR3oK7bAU&t=1089s',
    'http://www.youtube.com/watch?v=4dJrv-vMhp0&t=1s',
    'http://www.youtube.com/watch?v=4Rjss5Q-bCE&t=1424s',
    'http://www.youtube.com/watch?v=Bv82dPTqZWk',
    'http://www.youtube.com/watch?v=MpErucI98NU',
    'http://www.youtube.com/watch?v=xqCSLvfNk5M&t=1441s',
]    
def video_hit():
    for video in video_links:
        set_ip()
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        driver.get(video)
        print('Video', video_links.index(video), 'opened')
        buttons = driver.find_elements_by_tag_name('button')
        for button in buttons:
            id = button.get_attribute('aria-label')
            if id == 'Play':
                button.click()
        time.sleep(2)
    time.sleep(20)
    driver.quit()
    time.sleep(2)
    print('Tearing down service')
    print('Recycling IP')
    video_hit()
video_hit()
