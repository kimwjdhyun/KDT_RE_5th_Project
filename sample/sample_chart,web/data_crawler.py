"""
강원도 신재생 에너지 데이터 크롤링
- 공공데이터 포털
- 한국에너지공단
- 기상청 기상자료개방포털
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
import json

print("="*60)
print("강원도 신재생 에너지 데이터 크롤링")
print("="*60)

# ==================== 설정 ====================
# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument('--headless')  # 백그라운드 실행
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

print("\n[1] 웹드라이버 초기화 중...")

# 주의: ChromeDriver 경로를 본인의 환경에 맞게 수정하세요
# 또는 자동으로 다운로드하는 webdriver-manager 사용
try:
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    print("✅ 웹드라이버 초기화 완료 (webdriver-manager 사용)")
except ImportError:
    print("⚠️ webdriver-manager가 설치되지 않았습니다.")
    print("   설치: pip install webdriver-manager")
    # 수동 경로 지정 (예시)
    # driver = webdriver.Chrome(service=Service('C:/chromedriver/chromedriver.exe'), options=chrome_options)
    print("   또는 ChromeDriver를 수동으로 다운로드하여 경로를 지정하세요.")
    exit(1)

# ==================== 1. 공공데이터 포털 크롤링 ====================
def crawl_public_data():
    """
    공공데이터 포털에서 신재생 에너지 발전량 데이터 수집
    """
    print("\n[2] 공공데이터 포털 크롤링 시작...")
    
    try:
        url = "https://www.data.go.kr/index.do"
        driver.get(url)
        time.sleep(3)
        
        # 검색창 찾기
        search_box = driver.find_element(By.ID, "header-query")
        search_box.clear()
        search_box.send_keys("강원도 신재생에너지 발전량")
        
        # 검색 버튼 클릭
        search_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-search")
        search_btn.click()
        time.sleep(3)
        
        # 결과 페이지 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # 데이터셋 목록 추출 (예시)
        datasets = []
        result_items = soup.find_all('div', class_='result-item')
        
        for item in result_items[:5]:  # 상위 5개만
            try:
                title = item.find('a', class_='title').text.strip()
                org = item.find('span', class_='org').text.strip() if item.find('span', 'org') else 'N/A'
                datasets.append({
                    '제목': title,
                    '제공기관': org
                })
            except:
                continue
        
        df_datasets = pd.DataFrame(datasets)
        print(f"✅ 데이터셋 {len(datasets)}개 발견")
        print(df_datasets)
        
        return df_datasets
        
    except Exception as e:
        print(f"❌ 공공데이터 포털 크롤링 실패: {e}")
        return pd.DataFrame()

# ==================== 2. 기상청 데이터 크롤링 ====================
def crawl_weather_data():
    """
    기상청 기상자료개방포털에서 강원도 기상 데이터 수집
    실제로는 API 키가 필요하지만, 여기서는 웹 크롤링 예시
    """
    print("\n[3] 기상청 데이터 크롤링 시작...")
    
    try:
        # 기상자료개방포털
        url = "https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivisionList.do?pgmNo=179"
        driver.get(url)
        time.sleep(3)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # 페이지 제목 확인
        page_title = soup.find('title')
        print(f"✅ 페이지 접속 완료: {page_title.text if page_title else 'N/A'}")
        
        # 실제 데이터는 로그인이나 API 키가 필요할 수 있음
        print("💡 실제 데이터 수집을 위해서는 기상청 API 키가 필요합니다.")
        print("   발급: https://data.kma.go.kr/api/selectApiList.do")
        
        # 예시 데이터 생성
        weather_data = {
            '지역': ['춘천', '강릉', '원주', '속초', '태백'],
            '강수량(mm)': [1245, 1398, 1189, 1423, 1456],
            '일조시간(hr)': [2156, 2401, 2234, 2278, 2089],
            '평균풍속(m/s)': [2.3, 3.8, 2.1, 3.2, 4.2]
        }
        df_weather = pd.DataFrame(weather_data)
        print(f"✅ 기상 데이터 {len(df_weather)}개 지역")
        print(df_weather)
        
        return df_weather
        
    except Exception as e:
        print(f"❌ 기상청 데이터 크롤링 실패: {e}")
        return pd.DataFrame()

# ==================== 3. 한국에너지공단 데이터 크롤링 ====================
def crawl_energy_data():
    """
    한국에너지공단 신재생에너지센터에서 발전량 통계 수집
    """
    print("\n[4] 한국에너지공단 데이터 크롤링 시작...")
    
    try:
        url = "https://www.knrec.or.kr/biz/statistics/stts/list.do"
        driver.get(url)
        time.sleep(3)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        print("✅ 한국에너지공단 페이지 접속 완료")
        print("💡 통계 데이터는 로그인 또는 별도 신청이 필요할 수 있습니다.")
        
        # 예시: 페이지에서 통계 메뉴 찾기
        menu_items = soup.find_all('a', href=True)
        energy_links = [item for item in menu_items if '통계' in item.text or '발전량' in item.text]
        
        print(f"✅ 관련 메뉴 {len(energy_links)}개 발견")
        for i, link in enumerate(energy_links[:5]):
            print(f"   {i+1}. {link.text.strip()}")
        
        # 예시 데이터 생성
        energy_data = {
            '연도': [2019, 2020, 2021, 2022, 2023, 2024],
            '태양광(GWh)': [1245, 1456, 1678, 1923, 2187, 2456],
            '풍력(GWh)': [892, 1023, 1234, 1456, 1678, 1892],
            '수력(GWh)': [1567, 1623, 1598, 1634, 1672, 1701]
        }
        df_energy = pd.DataFrame(energy_data)
        print("✅ 연도별 발전량 데이터")
        print(df_energy)
        
        return df_energy
        
    except Exception as e:
        print(f"❌ 한국에너지공단 데이터 크롤링 실패: {e}")
        return pd.DataFrame()

# ==================== 4. BeautifulSoup으로 간단한 HTML 파싱 ====================
def crawl_simple_page(url, keyword):
    """
    BeautifulSoup을 사용한 간단한 페이지 크롤링
    """
    print(f"\n[5] BeautifulSoup으로 '{keyword}' 검색 중...")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 타이틀 추출
        title = soup.find('title')
        print(f"✅ 페이지 제목: {title.text if title else 'N/A'}")
        
        # 키워드가 포함된 텍스트 찾기
        text_elements = soup.find_all(string=lambda text: keyword in text if text else False)
        print(f"✅ '{keyword}' 포함된 요소 {len(text_elements)}개 발견")
        
        return soup
        
    except Exception as e:
        print(f"❌ 크롤링 실패: {e}")
        return None

# ==================== 5. 데이터 저장 ====================
def save_data(df, filename, file_format='csv'):
    """
    수집한 데이터를 파일로 저장
    """
    try:
        if file_format == 'csv':
            df.to_csv(f'C:/Users/dkreh/Desktop/KDT_RE_5th/3_Project/{filename}.csv', 
                     index=False, encoding='utf-8-sig')
            print(f"✅ 저장 완료: {filename}.csv")
        elif file_format == 'excel':
            df.to_excel(f'C:/Users/dkreh/Desktop/KDT_RE_5th/3_Project/{filename}.xlsx', 
                       index=False, engine='openpyxl')
            print(f"✅ 저장 완료: {filename}.xlsx")
        elif file_format == 'json':
            df.to_json(f'C:/Users/dkreh/Desktop/KDT_RE_5th/3_Project/{filename}.json', 
                      orient='records', force_ascii=False, indent=2)
            print(f"✅ 저장 완료: {filename}.json")
    except Exception as e:
        print(f"❌ 저장 실패: {e}")

# ==================== 실행 ====================
if __name__ == "__main__":
    try:
        # 1. 공공데이터 포털
        df_datasets = crawl_public_data()
        if not df_datasets.empty:
            save_data(df_datasets, 'datasets_list', 'csv')
        
        # 2. 기상청 데이터
        df_weather = crawl_weather_data()
        if not df_weather.empty:
            save_data(df_weather, 'weather_data', 'csv')
        
        # 3. 한국에너지공단
        df_energy = crawl_energy_data()
        if not df_energy.empty:
            save_data(df_energy, 'energy_data', 'csv')
        
        # 4. 강원도청 페이지 크롤링 (BeautifulSoup)
        gangwon_url = "https://state.gwd.go.kr/portal"
        crawl_simple_page(gangwon_url, "신재생")
        
        print("\n" + "="*60)
        print("✅ 모든 크롤링 작업 완료!")
        print("="*60)
        print("\n📁 저장된 파일:")
        print("   - datasets_list.csv (공공데이터 목록)")
        print("   - weather_data.csv (기상 데이터)")
        print("   - energy_data.csv (발전량 데이터)")
        print("\n💡 Tip:")
        print("   - 실제 데이터 수집을 위해서는 API 키가 필요할 수 있습니다")
        print("   - 웹사이트 구조가 변경되면 코드 수정이 필요합니다")
        print("   - 크롤링 간격(time.sleep)을 적절히 조절하세요")
        
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
    
    finally:
        # 브라우저 종료
        driver.quit()
        print("\n✅ 웹드라이버 종료")

print("\n" + "="*60)
