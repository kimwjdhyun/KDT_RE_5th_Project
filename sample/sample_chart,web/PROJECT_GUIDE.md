# 🌿 강원도 신재생 에너지 분석 프로젝트 - 전체 가이드

## 📂 프로젝트 구조

```
3_Project/
│
├── 📊 데이터 분석 및 시각화
│   ├── gangwon_energy_analysis.py      # 메인 분석 스크립트 (Folium + Matplotlib)
│   ├── create_dashboard.py             # HTML 대시보드 생성
│   └── gangwon_energy_dashboard.html   # 최종 웹 대시보드 (생성됨)
│
├── 🕷️ 웹 크롤링
│   ├── data_crawler.py                 # 기본 크롤링 (공공데이터, 기상청, 에너지공단)
│   ├── advanced_crawler.py             # 고급 크롤링 (동적 페이지, 테이블 추출, 검증)
│   ├── crawler_config.py               # 크롤링 설정 파일
│   └── CRAWLING_GUIDE.md              # 크롤링 완전 가이드
│
├── ⚡ 실행 스크립트
│   ├── run_analysis.bat                # 분석 + 대시보드 원클릭 실행
│   └── run_crawler.bat                 # 크롤링 원클릭 실행
│
├── 📚 문서
│   ├── README.md                       # 메인 사용 설명서
│   └── 데이터분석 프로젝트 계획서.pdf   # 프로젝트 문서
│
└── 📁 생성되는 파일들
    ├── gangwon_energy_map.html         # Folium 인터랙티브 지도
    ├── chart1~5.png                    # 분석 차트들
    └── *.csv                           # 크롤링된 데이터
```

---

## 🚀 빠른 시작 (3단계)

### 1️⃣ 라이브러리 설치 (최초 1회)

```bash
pip install pandas numpy matplotlib seaborn folium selenium beautifulsoup4 requests webdriver-manager openpyxl
```

### 2️⃣ 데이터 수집 (크롤링)

**방법 A: 원클릭 실행**
```
run_crawler.bat 더블클릭
```

**방법 B: 수동 실행**
```bash
# 기본 크롤링
python data_crawler.py

# 고급 크롤링
python advanced_crawler.py
```

### 3️⃣ 분석 및 대시보드 생성

**방법 A: 원클릭 실행**
```
run_analysis.bat 더블클릭
```

**방법 B: 수동 실행**
```bash
# 1. 분석 실행
python gangwon_energy_analysis.py

# 2. 대시보드 생성
python create_dashboard.py

# 3. 브라우저로 열기
gangwon_energy_dashboard.html
```

---

## 📊 생성되는 결과물

### 1. 인터랙티브 지도 (`gangwon_energy_map.html`)
- 🗺️ 강원도 18개 시군 위치 표시
- 📍 클릭하면 발전량, 기상 데이터 팝업
- 🎨 발전량에 따른 색상 구분

### 2. 분석 차트 (5개 PNG 파일)
- **chart1**: 시군별 총 발전량 막대 그래프
- **chart2**: 에너지원별 스택 바 차트
- **chart3**: 2019-2024 추이 라인 차트
- **chart4**: 에너지 비중 파이 차트
- **chart5**: 기상 상관관계 히트맵

### 3. 통합 웹 대시보드 (`gangwon_energy_dashboard.html`)
- 📱 반응형 디자인 (모바일/PC 지원)
- 📊 모든 차트 + 지도 통합
- 💡 주요 인사이트 제공
- 🎯 통계 카드

---

## 🎓 프로젝트에서 배우는 기술

### 데이터 분석
```python
✅ Pandas - 데이터 처리 및 분석
✅ NumPy - 수치 계산
✅ Matplotlib - 기본 시각화
✅ Seaborn - 고급 통계 시각화
✅ Folium - 지도 시각화
```

### 웹 크롤링
```python
✅ Selenium - 동적 웹페이지 크롤링
✅ BeautifulSoup - HTML 파싱
✅ Requests - HTTP 요청
✅ 데이터 정제 및 검증
✅ API 활용
```

### 웹 개발
```python
✅ HTML5 - 구조
✅ CSS3 - 스타일링
✅ 반응형 디자인
✅ 데이터 시각화 통합
```

---

## 💡 주요 기능 설명

### 🗺️ Folium 지도 기능

```python
# 지도 생성
m = folium.Map(location=[37.8228, 128.1555], zoom_start=9)

# 마커 추가
folium.Marker(
    location=[위도, 경도],
    popup="상세 정보",
    icon=folium.Icon(color='red', icon='bolt')
).add_to(m)

# 원 추가 (발전량 비례)
folium.Circle(
    location=[위도, 경도],
    radius=발전량 * 50,
    color='red',
    fill=True
).add_to(m)

# 저장
m.save('map.html')
```

### 📊 Matplotlib 차트 기능

```python
# 막대 그래프
plt.bar(지역, 발전량, color='#4CAF50')
plt.xlabel('지역')
plt.ylabel('발전량 (GWh)')
plt.title('시군별 총 발전량')
plt.savefig('chart.png', dpi=300)

# 라인 차트
plt.plot(연도, 태양광, marker='o', label='태양광')
plt.plot(연도, 풍력, marker='s', label='풍력')
plt.legend()

# 파이 차트
plt.pie(값들, labels=라벨, autopct='%1.1f%%')

# 히트맵 (Seaborn)
sns.heatmap(상관관계, annot=True, cmap='coolwarm')
```

### 🕷️ 크롤링 기법

```python
# Selenium 기본
driver.get(url)
element = driver.find_element(By.ID, "search")
element.send_keys("검색어")
button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()

# BeautifulSoup 기본
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('h1').text
items = soup.find_all('div', class_='item')

# 테이블 추출
df = pd.read_html(url)[0]

# API 요청
response = requests.get(api_url, params={'key': 'value'})
data = response.json()
```

---

## 🎯 실제 데이터로 업데이트하기

### 1단계: API 키 발급

#### 기상청 API
1. https://data.kma.go.kr 접속
2. 회원가입 → 로그인
3. API → 오픈API 신청
4. 발급받은 키를 `crawler_config.py`에 입력

#### 공공데이터 포털
1. https://www.data.go.kr 접속
2. "강원도 신재생에너지" 검색
3. 데이터셋 선택 → 활용신청
4. 발급받은 키를 `crawler_config.py`에 입력

### 2단계: 데이터 수집

```bash
python data_crawler.py
```

### 3단계: 분석 코드 수정

`gangwon_energy_analysis.py`에서 데이터 경로 수정:
```python
# 크롤링한 데이터 불러오기
df = pd.read_csv('crawled_data.csv')

# 또는 수동으로 데이터 입력
region_data = {
    '지역': [...],
    '태양광(GWh)': [...],  # 실제 데이터
    # ...
}
```

---

## 🔧 문제 해결

### Q1: "ModuleNotFoundError: No module named 'selenium'"
```bash
pip install selenium beautifulsoup4 requests pandas webdriver-manager
```

### Q2: ChromeDriver 오류
```bash
pip install webdriver-manager
```

### Q3: 한글 깨짐
```python
df.to_csv('data.csv', encoding='utf-8-sig')  # utf-8-sig 사용
plt.rcParams['font.family'] = 'Malgun Gothic'  # 한글 폰트
```

### Q4: API 요청 실패
- API 키 확인
- 요청 제한 확인 (일일 횟수 제한)
- URL 및 파라미터 확인

### Q5: 브라우저가 자동으로 닫힘
```python
# headless=False로 변경
crawler = AdvancedCrawler(headless=False)

# 또는 대기 시간 추가
time.sleep(10)
```

---

## 📚 학습 자료

### 공식 문서
- Pandas: https://pandas.pydata.org/docs/
- Matplotlib: https://matplotlib.org/stable/contents.html
- Selenium: https://www.selenium.dev/documentation/
- Folium: https://python-visualization.github.io/folium/

### 한국 공공데이터
- 공공데이터 포털: https://www.data.go.kr
- 국가통계포털: https://kosis.kr
- 기상청: https://data.kma.go.kr
- 한국에너지공단: https://www.knrec.or.kr

---

## 🎓 실습 과제

### 초급
1. ✅ 기존 예시 데이터로 차트 생성
2. ✅ Folium 지도에 마커 추가
3. ✅ HTML 대시보드 색상 변경

### 중급
1. 🔄 실제 API로 데이터 수집
2. 📊 새로운 차트 추가 (산점도, 박스플롯)
3. 🗺️ 지도에 히트맵 오버레이

### 고급
1. 🤖 데이터 수집 자동화 (스케줄러)
2. 📈 머신러닝으로 발전량 예측
3. ⚡ 실시간 업데이트 대시보드

---

## 👥 프로젝트 정보

**포스코 x 코딩온 신재생에너지 IoT개발자 과정 5기 1조**

**팀원**
- 김정현: 데이터 수집 자동화, 전처리, 시각화
- 천예리: 정책 자료 정리, 분석 설계, 결과 해석

**기간**
- 2024.12.15 ~ 2025.01.13

**기술 스택**
- Python 3.14
- Pandas, NumPy, Matplotlib, Seaborn
- Folium
- Selenium, BeautifulSoup

---

## 📞 추가 도움이 필요하면?

1. 📖 `README.md` - 기본 사용법
2. 🕷️ `CRAWLING_GUIDE.md` - 크롤링 완전 가이드
3. ⚙️ `crawler_config.py` - 설정 파일
4. 💬 프로젝트 Issues에 질문 남기기

---

## 🎯 다음 단계

1. ✅ 기본 예시 실행해보기
2. 🔑 API 키 발급받기
3. 📊 실제 데이터 수집
4. 🎨 대시보드 커스터마이징
5. 🚀 자동화 및 고도화

---

**Happy Coding! 🚀**

Made with ❤️ by KDT RE 5th Team 1
