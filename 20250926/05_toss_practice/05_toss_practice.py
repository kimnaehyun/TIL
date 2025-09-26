import time
import os
import sys
import django

# 프로젝트 루트를 PYTHONPATH에 추가
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Django 설정 모듈 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance.settings")
django.setup()

from crawlings.models import Crawling
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ---------------------------
# Django 환경 초기화
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 위치
sys.path.append(BASE_DIR)  # 프로젝트 루트 추가
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlings.settings")  # settings.py 위치
django.setup()

from crawlings.models import Crawling

# ---------------------------
# Selenium 크롬 드라이버 설정
# ---------------------------
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("../chromedriver-win64/chromedriver.exe")  # 크롬 드라이버 경로

# ---------------------------
# 댓글 수집 함수
# ---------------------------
def fetch_visible_comments(company_name, limit=20, max_scroll=10):
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Toss 접속
        driver.get("https://www.tossinvest.com/")
        time.sleep(1)

        # 검색
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys("/")
        time.sleep(1)

        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='검색어를 입력해주세요']")
            )
        )
        search_input.send_keys(company_name)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)

        # 종목 코드 추출
        WebDriverWait(driver, 15).until(EC.url_contains("/order"))
        current_url = driver.current_url
        stock_code = current_url.split("/")[current_url.split("/").index("stocks") + 1]
        print(f"stock_code={stock_code}")

        # 커뮤니티 페이지 접속
        community_url = f"https://www.tossinvest.com/stocks/{stock_code}/community"
        driver.get(community_url)
        time.sleep(1)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main article"))
        )

        # 댓글 수집
        comments = []
        last_height = driver.execute_script("return document.body.scrollHeight")

        for scroll in range(max_scroll):
            spans = driver.find_elements(By.CSS_SELECTOR, "article.comment span.tw-1r5dc8g0._60z0ev1")
            for span in spans:
                text = span.text.strip()
                if text and text not in comments:
                    comments.append(text)

            if len(comments) >= limit:
                break

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    finally:
        driver.quit()

    return comments[:limit], stock_code

# ---------------------------
# 실행
# ---------------------------
if __name__ == "__main__":
    company_name = "삼성전자"
    comments, stock_code = fetch_visible_comments(company_name, limit=20)

    if not comments:
        print("댓글을 가져오지 못했습니다.")
    else:
        print("\n=== 커뮤니티 댓글 ===")
        for c in comments:
            print(c)
            # Django DB 저장
            crawling = Crawling(company_name=company_name, code=stock_code, comment=c)
            crawling.save()
        print(f"\n총 {len(comments)}개의 댓글을 DB에 저장했습니다.")
