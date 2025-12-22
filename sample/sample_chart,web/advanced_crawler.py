"""
고급 웹 크롤링 기법
- 동적 페이지 처리
- 페이지네이션 자동 처리
- 데이터 정합성 검증
- 결측치 처리
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

class AdvancedCrawler:
    """고급 크롤링 클래스"""
    
    def __init__(self, headless=True):
        """초기화"""
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
        
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
            print("✅ 크롤러 초기화 완료")
        except Exception as e:
            print(f"❌ 크롤러 초기화 실패: {e}")
            raise
    
    def wait_for_element(self, by, value, timeout=10):
        """요소가 로드될 때까지 대기"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"⚠️ 요소를 찾을 수 없습니다: {value}")
            return None
    
    def scroll_to_bottom(self, pause_time=2):
        """페이지 끝까지 스크롤 (무한 스크롤 페이지용)"""
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # 페이지 끝까지 스크롤
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause_time)
            
            # 새로운 높이 계산
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            if new_height == last_height:
                break
            last_height = new_height
        
        print("✅ 페이지 끝까지 스크롤 완료")
    
    def crawl_with_pagination(self, base_url, max_pages=5):
        """
        페이지네이션이 있는 사이트 크롤링
        """
        all_data = []
        
        for page in range(1, max_pages + 1):
            try:
                url = f"{base_url}?page={page}"
                self.driver.get(url)
                time.sleep(2)
                
                print(f"📄 페이지 {page} 크롤링 중...")
                
                # 데이터 추출 로직
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                items = soup.find_all('div', class_='data-item')  # 실제 클래스명으로 수정
                
                page_data = []
                for item in items:
                    try:
                        # 데이터 추출 (예시)
                        title = item.find('h3').text.strip()
                        value = item.find('span', class_='value').text.strip()
                        page_data.append({'제목': title, '값': value})
                    except:
                        continue
                
                all_data.extend(page_data)
                print(f"   ✅ {len(page_data)}개 항목 수집")
                
            except Exception as e:
                print(f"   ❌ 페이지 {page} 크롤링 실패: {e}")
                break
        
        return pd.DataFrame(all_data)
    
    def extract_table_data(self, table_selector='table'):
        """
        HTML 테이블 데이터 추출
        """
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            tables = soup.find_all(table_selector)
            
            if not tables:
                print("⚠️ 테이블을 찾을 수 없습니다")
                return pd.DataFrame()
            
            # 첫 번째 테이블 추출
            table = tables[0]
            
            # 헤더 추출
            headers = []
            thead = table.find('thead')
            if thead:
                headers = [th.text.strip() for th in thead.find_all('th')]
            
            # 데이터 추출
            rows = []
            tbody = table.find('tbody') or table
            for tr in tbody.find_all('tr'):
                row = [td.text.strip() for td in tr.find_all(['td', 'th'])]
                if row:
                    rows.append(row)
            
            # DataFrame 생성
            if headers:
                df = pd.DataFrame(rows, columns=headers)
            else:
                df = pd.DataFrame(rows)
            
            print(f"✅ 테이블 데이터 {len(df)}행 추출")
            return df
            
        except Exception as e:
            print(f"❌ 테이블 추출 실패: {e}")
            return pd.DataFrame()
    
    def download_file(self, download_url, save_path):
        """
        파일 다운로드
        """
        try:
            import requests
            response = requests.get(download_url, timeout=30)
            response.raise_for_status()
            
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ 파일 다운로드 완료: {save_path}")
            return True
        except Exception as e:
            print(f"❌ 파일 다운로드 실패: {e}")
            return False
    
    def clean_text(self, text):
        """
        텍스트 정제 (공백, 특수문자 제거)
        """
        if not text:
            return ""
        
        # 다중 공백을 단일 공백으로
        text = re.sub(r'\s+', ' ', text)
        # 앞뒤 공백 제거
        text = text.strip()
        # 특정 특수문자 제거 (필요에 따라 수정)
        text = re.sub(r'[^\w\s가-힣.,()%-]', '', text)
        
        return text
    
    def validate_data(self, df):
        """
        데이터 정합성 검증
        """
        print("\n📊 데이터 검증 중...")
        
        # 1. 결측치 확인
        missing = df.isnull().sum()
        if missing.any():
            print(f"⚠️ 결측치 발견:")
            print(missing[missing > 0])
        else:
            print("✅ 결측치 없음")
        
        # 2. 중복 확인
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            print(f"⚠️ 중복 데이터 {duplicates}개 발견")
        else:
            print("✅ 중복 데이터 없음")
        
        # 3. 데이터 타입 확인
        print("\n📋 데이터 타입:")
        print(df.dtypes)
        
        # 4. 기본 통계
        print("\n📈 기본 통계:")
        print(df.describe())
        
        return df
    
    def close(self):
        """브라우저 종료"""
        if self.driver:
            self.driver.quit()
            print("✅ 크롤러 종료")

# ==================== 특정 사이트 크롤링 함수들 ====================

def crawl_kosis_data(crawler):
    """
    국가통계포털(KOSIS) 데이터 크롤링
    """
    print("\n[KOSIS] 국가통계포털 크롤링...")
    
    try:
        url = "https://kosis.kr/statHtml/statHtml.do?orgId=388&tblId=DT_388N_0001"
        crawler.driver.get(url)
        time.sleep(3)
        
        # 테이블 데이터 추출
        df = crawler.extract_table_data()
        
        if not df.empty:
            # 데이터 정제
            df = df.applymap(crawler.clean_text)
            print(f"✅ KOSIS 데이터 {len(df)}행 수집")
            return df
        
    except Exception as e:
        print(f"❌ KOSIS 크롤링 실패: {e}")
    
    return pd.DataFrame()

def crawl_weather_api_data():
    """
    기상청 API를 사용한 데이터 수집 (API 키 필요)
    """
    print("\n[기상청 API] 데이터 수집...")
    
    # API 키가 필요합니다
    API_KEY = "YOUR_API_KEY_HERE"
    
    if API_KEY == "YOUR_API_KEY_HERE":
        print("⚠️ 기상청 API 키를 설정해주세요")
        print("   발급: https://data.kma.go.kr/api/selectApiList.do")
        return pd.DataFrame()
    
    try:
        import requests
        
        # 예시: 특정 지점의 일별 데이터
        url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"
        
        params = {
            'serviceKey': API_KEY,
            'numOfRows': 100,
            'pageNo': 1,
            'dataCd': 'ASOS',
            'dateCd': 'DAY',
            'startDt': '20240101',
            'endDt': '20241231',
            'stnIds': '101',  # 춘천
            'dataType': 'JSON'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # JSON 데이터를 DataFrame으로 변환
        items = data.get('response', {}).get('body', {}).get('items', {}).get('item', [])
        df = pd.DataFrame(items)
        
        print(f"✅ 기상청 API 데이터 {len(df)}행 수집")
        return df
        
    except Exception as e:
        print(f"❌ 기상청 API 수집 실패: {e}")
        return pd.DataFrame()

# ==================== 실행 예시 ====================
if __name__ == "__main__":
    print("="*60)
    print("고급 웹 크롤링 실행")
    print("="*60)
    
    # 크롤러 초기화
    crawler = AdvancedCrawler(headless=True)
    
    try:
        # 1. KOSIS 데이터
        df_kosis = crawl_kosis_data(crawler)
        if not df_kosis.empty:
            crawler.validate_data(df_kosis)
            df_kosis.to_csv('C:/Users/dkreh/Desktop/KDT_RE_5th/3_Project/kosis_data.csv', 
                           index=False, encoding='utf-8-sig')
        
        # 2. 기상청 API 데이터
        df_weather = crawl_weather_api_data()
        if not df_weather.empty:
            df_weather.to_csv('C:/Users/dkreh/Desktop/KDT_RE_5th/3_Project/weather_api_data.csv',
                             index=False, encoding='utf-8-sig')
        
        print("\n" + "="*60)
        print("✅ 고급 크롤링 완료!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
    
    finally:
        crawler.close()
