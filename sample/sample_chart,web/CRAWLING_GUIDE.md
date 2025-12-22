# 웹 크롤링 완전 가이드 📚

## 📦 필요한 라이브러리 설치

```bash
# 기본 라이브러리
pip install selenium beautifulsoup4 requests pandas

# 크롬 드라이버 자동 관리
pip install webdriver-manager

# 엑셀 파일 처리 (선택)
pip install openpyxl

# 모두 한 번에 설치
pip install selenium beautifulsoup4 requests pandas webdriver-manager openpyxl
```

---

## 🚀 빠른 시작

### 1단계: 기본 크롤링 실행

```bash
python data_crawler.py
```

이 스크립트는:
- ✅ 공공데이터 포털 검색
- ✅ 기상청 페이지 접속
- ✅ 한국에너지공단 통계 메뉴 확인
- ✅ 예시 데이터 생성 및 저장

### 2단계: 고급 크롤링 실행

```bash
python advanced_crawler.py
```

이 스크립트는:
- ✅ 동적 페이지 처리
- ✅ 테이블 데이터 자동 추출
- ✅ 페이지네이션 자동 처리
- ✅ 데이터 정합성 검증

---

## 🔧 설정 파일 수정

### API 키 설정 (`crawler_config.py`)

```python
API_KEYS = {
    'WEATHER_API_KEY': '여기에_발급받은_키_입력',
    'PUBLIC_DATA_API_KEY': '여기에_발급받은_키_입력',
}
```

### API 키 발급 방법

#### 1. 기상청 API
1. https://data.kma.go.kr 접속
2. 회원가입 후 로그인
3. 상단 메뉴 → API → 오픈API 신청
4. 활용 목적 작성 후 신청
5. 승인 후 API 키 발급

#### 2. 공공데이터 포털 API
1. https://www.data.go.kr 접속
2. 회원가입 후 로그인
3. 데이터 검색 → "신재생에너지" 검색
4. 원하는 데이터셋 선택 → "활용신청" 클릭
5. 승인 후 인증키(API 키) 발급

---

## 💡 크롤링 기법별 사용 예시

### 1. Selenium으로 동적 페이지 크롤링

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 드라이버 초기화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 페이지 열기
driver.get("https://example.com")

# 요소 찾기
element = driver.find_element(By.ID, "search-box")
element.send_keys("강원도 신재생에너지")

# 버튼 클릭
button = driver.find_element(By.CSS_SELECTOR, "button.search")
button.click()

# 결과 가져오기
results = driver.find_elements(By.CLASS_NAME, "result-item")
for result in results:
    print(result.text)

# 종료
driver.quit()
```

### 2. BeautifulSoup으로 정적 페이지 크롤링

```python
import requests
from bs4 import BeautifulSoup

# 페이지 요청
url = "https://example.com"
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 데이터 추출
title = soup.find('h1', class_='title').text
items = soup.find_all('div', class_='item')

for item in items:
    name = item.find('span', class_='name').text
    value = item.find('span', class_='value').text
    print(f"{name}: {value}")
```

### 3. 테이블 데이터 추출

```python
import pandas as pd

# HTML 테이블을 바로 DataFrame으로
url = "https://example.com/table-page"
tables = pd.read_html(url)

# 첫 번째 테이블
df = tables[0]
print(df.head())

# CSV로 저장
df.to_csv('table_data.csv', index=False, encoding='utf-8-sig')
```

### 4. API 요청으로 데이터 수집

```python
import requests
import pandas as pd

# API 엔드포인트
url = "http://apis.data.go.kr/your-api-endpoint"

# 파라미터 설정
params = {
    'serviceKey': 'YOUR_API_KEY',
    'numOfRows': 100,
    'pageNo': 1,
    'dataType': 'JSON'
}

# 요청
response = requests.get(url, params=params)
data = response.json()

# DataFrame으로 변환
items = data['response']['body']['items']['item']
df = pd.DataFrame(items)
```

---

## 🎯 실전 크롤링 프로젝트

### 강원도 신재생 에너지 데이터 수집 프로세스

```python
from advanced_crawler import AdvancedCrawler
import pandas as pd

# 1. 크롤러 초기화
crawler = AdvancedCrawler(headless=False)  # 브라우저 보기

try:
    # 2. 한국에너지공단 통계 페이지
    crawler.driver.get("https://www.knrec.or.kr/biz/statistics/stts/list.do")
    
    # 3. 강원도 선택 (예시)
    region_select = crawler.driver.find_element(By.ID, "region")
    region_select.click()
    
    gangwon = crawler.driver.find_element(By.XPATH, "//option[text()='강원']")
    gangwon.click()
    
    # 4. 검색 버튼 클릭
    search_btn = crawler.driver.find_element(By.CSS_SELECTOR, "button.search")
    search_btn.click()
    
    # 5. 결과 테이블 추출
    df = crawler.extract_table_data()
    
    # 6. 데이터 정제
    df = crawler.validate_data(df)
    
    # 7. 저장
    df.to_csv('gangwon_energy_real.csv', index=False, encoding='utf-8-sig')
    print("✅ 데이터 수집 완료!")
    
finally:
    crawler.close()
```

---

## 🛠️ 문제 해결

### 1. ChromeDriver 오류

**문제:** `selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH`

**해결:**
```bash
pip install webdriver-manager
```

코드에서:
```python
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

### 2. 한글 깨짐

**문제:** CSV 파일에서 한글이 깨져 보임

**해결:**
```python
df.to_csv('data.csv', encoding='utf-8-sig', index=False)  # utf-8-sig 사용
```

### 3. 요소를 찾을 수 없음

**문제:** `NoSuchElementException`

**해결:**
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 요소가 나타날 때까지 대기
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element-id"))
)
```

### 4. 페이지 로딩이 느림

**문제:** 페이지가 완전히 로드되기 전에 크롤링 시도

**해결:**
```python
import time

driver.get(url)
time.sleep(3)  # 3초 대기

# 또는 명시적 대기
driver.implicitly_wait(10)  # 최대 10초 대기
```

### 5. 봇 탐지로 차단

**문제:** `403 Forbidden` 또는 captcha 발생

**해결:**
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)
```

---

## 📊 데이터 후처리

### 결측치 처리

```python
# 결측치 확인
print(df.isnull().sum())

# 결측치 제거
df_clean = df.dropna()

# 결측치 채우기
df['컬럼명'].fillna(df['컬럼명'].mean(), inplace=True)  # 평균값으로
df['컬럼명'].fillna(method='ffill', inplace=True)  # 앞 값으로
```

### 중복 제거

```python
# 중복 확인
print(f"중복 행 수: {df.duplicated().sum()}")

# 중복 제거
df_unique = df.drop_duplicates()
```

### 데이터 타입 변환

```python
# 문자열 → 숫자
df['발전량'] = pd.to_numeric(df['발전량'], errors='coerce')

# 문자열 → 날짜
df['날짜'] = pd.to_datetime(df['날짜'])

# 쉼표 제거 후 숫자 변환
df['값'] = df['값'].str.replace(',', '').astype(float)
```

---

## 🎓 학습 리소스

### Selenium 공식 문서
- https://www.selenium.dev/documentation/

### BeautifulSoup 공식 문서
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### 크롤링 연습 사이트
- http://quotes.toscrape.com (초보자용)
- https://books.toscrape.com (실습용)

### 한국 공공데이터 포털
- https://www.data.go.kr
- https://kosis.kr
- https://data.kma.go.kr

---

## ⚖️ 웹 크롤링 주의사항

### 법적 주의사항
1. **robots.txt 확인**: 사이트의 크롤링 정책 준수
2. **저작권**: 수집한 데이터의 저작권 확인
3. **개인정보**: 개인정보 수집 금지
4. **상업적 이용**: 상업적 목적 시 별도 허가 필요

### 기술적 주의사항
1. **요청 간격**: 서버 부하 방지를 위해 적절한 대기 시간 설정
2. **User-Agent**: 봇이 아님을 나타내는 헤더 추가
3. **에러 처리**: try-except로 오류 처리
4. **로깅**: 크롤링 과정 기록

### 예시 코드

```python
import time
import random

# 1. 적절한 대기 시간
time.sleep(random.uniform(2, 5))  # 2~5초 랜덤 대기

# 2. User-Agent 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# 3. 에러 처리
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"요청 실패: {e}")

# 4. 로깅
import logging
logging.basicConfig(level=logging.INFO)
logging.info("크롤링 시작")
```

---

## 📝 실습 과제

### 초급: 단순 페이지 크롤링
- 강원도청 홈페이지에서 공지사항 제목 가져오기

### 중급: 테이블 데이터 추출
- KOSIS에서 강원도 인구 통계 테이블 크롤링

### 고급: 동적 페이지 + API
- 공공데이터 포털에서 검색 → API 활용 → 데이터 통합

---

## 🚀 다음 단계

1. 실제 API 키 발급받기
2. 크롤링 자동화 스케줄러 구축
3. 데이터베이스 연동
4. 실시간 모니터링 대시보드 제작

---

**Happy Crawling! 🕷️**
