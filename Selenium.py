from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import chrome_helper

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
chrome_helper.check_browser_driver_available()

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-software-rasterizer")


chrome = webdriver.Chrome(r'C:\temp\chrome\chromedriver', chrome_options=options)
chrome.get("https://my.ntu.edu.tw/attend/ssi.aspx?")


import configparser
import os
#   load user info. from config
def loadUserInfo( config: configparser.ConfigParser ) :
    if "USER" not in config :
        raise Exception("Config Error: section \"USER\" not find.")
    userName = config["USER"]["UserName"]
    password = config["USER"]["Password"]
    userDict = {'user': userName, 'pass': password}
    return userDict

#   read config root
configFile = "./config.ini"
#   check argument
if not os.path.isfile( configFile ) :
    raise Exception("Config Error: file + " + configFile + " not find!")

#   read config ini
config = configparser.ConfigParser()
config.read(configFile)
# load user info.
userDict = loadUserInfo( config )


#   Selenium auto detect login status

if not chrome.find_elements_by_css_selector('span#LabName'):
    if chrome.find_elements_by_css_selector('a.btn.btn-lg.btn-info.btn-block'):
        chrome.find_element_by_css_selector('a.btn.btn-lg.btn-info.btn-block').click()
        user = chrome.find_element_by_name("user")
        user.send_keys(userDict['user'])
        password = chrome.find_element_by_name("pass")
        password.send_keys(userDict['pass'])
        password.submit()
        
#   Selenium auto signin and out
#   Signin first. Check if the signin is done. If not done yet, then signin and quit.
#   If signin is done, then check signout status. If not done yet, then signout and quit.

#signin_info
signin_info = chrome.find_element_by_xpath("//*[@id='signs']")
signin_time_text = minority.get_attribute("textContent")

#signout_info
signout_info = chrome.find_element_by_xpath("//*[@id='signe']")
signout_time_text = minority.get_attribute("textContent")

if signin_time_text == '':
        if not chrome.find_elements_by_css_selector('a#btSign.btn.btn-lg.btn-success.btn-block.disabled'):
            chrome.find_element_by_css_selector('a#btSign.btn.btn-lg.btn-success.btn-block').click()
            print('singIN')

elif signout_time_text =='':
        if not chrome.find_elements_by_css_selector('a#btSign2.btn.btn-lg.btn-success.btn-block.disabled'):
            chrome.find_element_by_css_selector('a#btSign2.btn.btn-lg.btn-success.btn-block').click()
            print('singOUT')

#   Close chrome

chrome.close()
chrome.quit()

