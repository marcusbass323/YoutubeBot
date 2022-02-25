from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

chrome_options = Options()

#Run headless
chrome_options.add_argument("--headless")

#Removes browser control flag
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

#Set browser size
chrome_options.add_argument("--start-maximized")

# User-Agent
chrome_options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95 Safari/537.36")

#disable chrome password/security popups
prefs = {"credentials_enable_service": False,
     "profile.password_manager_enabled": False}
chrome_options.add_experimental_option("prefs", prefs)

#Modifying navigator.webdriver flag to prevent selenium detection
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)