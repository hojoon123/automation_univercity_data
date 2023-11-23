import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import pyautogui
import os
import json

# driver 셋팅 API
def update_chrome():
    global driver
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('lang=ko_KR')  # 사용언어 한국어
    chrome_options.add_argument('disable-gpu')  # 하드웨어 가속 안함
    #chrome_options.add_argument("headless") # 백그라운드 실행
    chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])  # 불필요한 에러 메세지 삭제
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    return

# url을 매개변수로 페이지 오픈 API
def open_page(page_url):
    try:
        driver.get(page_url)
        driver.implicitly_wait(10)
    except:
        print("url 오픈 오류")
        driver.quit()
    
    return



# 결과 dict을 매개변수로 현재 위치에서 폴더 생성 후 json 파일 생성 API
def create_json_file(result_data):
    # 폴더명 및 파일명 지정
        output_folder = 'json_data'
        output_file_name = f"2019_pass_or_fail.json"
        output_path = os.path.join(os.path.dirname(__file__), output_folder)
    
        # extract_json 폴더가 없으면 생성
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # 추출한 데이터를 JSON 파일로 저장
        output_file = os.path.join(output_path, output_file_name)
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(result_data, json_file, indent=4, ensure_ascii=False)

# 메인 function
def main():
    try:
        update_chrome()
        open_page("https://ipsi.jinhak.or.kr/subList/20000000095")
    except:
        driver.quit()
        return
if __name__ == "__main__":
    main()
