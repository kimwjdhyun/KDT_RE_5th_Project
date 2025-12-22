# 웹 크롤링 가이드 - 간략 버전

## 🚀 빠른 시작

### 라이브러리 설치
```bash
pip install selenium beautifulsoup4 requests pandas webdriver-manager
```

---

## 📖 기본 사용법

### 1. Selenium 기본

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
element.send_keys("검색어")

# 버튼 클릭
button = driver.find_element(By.CSS_SELECTOR, "button.search")
button.click()

# 종료
driver.quit()
```

### 2. BeautifulSoup 기본

```python
import requests
from bs4 import BeautifulSoup

# 페이지 요청
response = requests.get("https://example.com")

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 데이터 추출
title = soup.find('h1').text
items = soup.find_all('div', class_='item')

for item in items:
    print(item.text)
```

### 3. 테이블 추출

```python
import pandas as pd

# HTML 테이블을 DataFrame으로
tables = pd.read_html("https://example.com/table")
df = tables[0]
df.to_csv('data.csv', index=False, encoding='utf-8-sig')
```

---

## 💡 주요 팁

### 대기 시간 추가
```python
import time
time.sleep(3)  # 3초 대기
```

### 한글 깨짐 방지
```python
df.to_csv('data.csv', encoding='utf-8-sig')
```

### User-Agent 설정
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
response = requests.get(url, headers=headers)
```

---

## 🔧 문제 해결

### ChromeDriver 오류
```bash
pip install webdriver-manager
```

### 요소를 찾을 수 없음
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element-id"))
)
```

---

## ⚖️ 주의사항

1. **요청 간격**: 서버 부하 방지를 위해 적절한 대기
2. **robots.txt**: 사이트의 크롤링 정책 준수
3. **저작권**: 수집 데이터의 사용 범위 확인
4. **개인정보**: 개인정보 수집 금지

---

더 자세한 내용은 원본 `CRAWLING_GUIDE.md` 참고!
