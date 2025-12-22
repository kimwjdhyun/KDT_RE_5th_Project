"""
웹 크롤링 샘플 코드
Selenium + BeautifulSoup 사용

이 파일은 참고용 샘플입니다.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

print("="*60)
print("웹 크롤링 샘플")
print("="*60)

# ==================== Chrome 설정 ====================
chrome_options = Options()
chrome_options.add_argument('--headless')  # 백그라운드 실행
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('user-agent=Mozilla/5.0')

print("\n[1] 웹드라이버 초기화...")

try:
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    print("✅ 웹드라이버 초기화 완료")
except ImportError:
    print("⚠️ webdriver-manager 설치 필요")
    print("   pip install webdriver-manager")
    exit(1)

# ==================== 크롤링 예제 ====================

def example_crawl():
    """간단한 크롤링 예제"""
    print("\n[2] 공공데이터 포털 접속...")
    
    try:
        url = "https://www.data.go.kr/index.do"
        driver.get(url)
        time.sleep(3)
        
        # 페이지 제목 가져오기
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        title = soup.find('title')
        print(f"✅ 페이지 제목: {title.text if title else 'N/A'}")
        
        # 검색창 찾기 (예시)
        try:
            search_box = driver.find_element(By.ID, "header-query")
            print("✅ 검색창 발견")
        except:
            print("⚠️ 검색창을 찾을 수 없습니다")
        
        return True
        
    except Exception as e:
        print(f"❌ 크롤링 실패: {e}")
        return False

# ==================== 실행 ====================
try:
    example_crawl()
    
    print("\n" + "="*60)
    print("✅ 크롤링 완료!")
    print("="*60)
    print("\n💡 실제 사용시:")
    print("  1. crawler_config.py에서 API 키 설정")
    print("  2. 크롤링 대상 URL 확인")
    print("  3. 코드 수정하여 사용")
    
except Exception as e:
    print(f"\n❌ 오류 발생: {e}")

finally:
    driver.quit()
    print("\n✅ 브라우저 종료")
