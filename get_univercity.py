import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller as AutoChrome
import time
import pyperclip
import pyautogui
import os
import shutil

# 크롬 자동 업데이트 + driver 셋팅 API
def update_chrome():
    global driver
    # 크롬드라이버 버전 확인
    chrome_ver = AutoChrome.get_chrome_version().split('.')[0]

    options = webdriver.ChromeOptions()  # 브라우저 셋팅
    options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지
    options.add_argument('lang=ko_KR')  # 사용언어 한국어
    options.add_argument('disable-gpu')  # 하드웨어 가속 안함
    options.add_argument("headless") # 백그라운드 실행
    options.add_experimental_option("excludeSwitches", ['enable-logging'])  # 불필요한 에러 메세지 삭제

    # 실행 후 최신 버젼이 아니라서 실행이 안된다면 최신버젼으로 업데이트 후 재실행
    path = AutoChrome.install(True)
    driver = webdriver.Chrome(path)

    driver.implicitly_wait(10)
    
    
