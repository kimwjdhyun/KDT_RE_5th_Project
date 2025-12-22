# 📁 샘플 프로젝트 폴더 구조

```
sample/
│
├── 📊 01_analysis/                    # 데이터 분석 및 시각화
│   ├── gangwon_energy_analysis.py     # Folium + Matplotlib 분석 스크립트
│   ├── create_dashboard.py            # HTML 대시보드 생성 스크립트
│   └── run_analysis.bat               # 원클릭 실행 스크립트
│
├── 🕷️ 02_crawling/                   # 웹 크롤링
│   ├── data_crawler.py                # 기본 크롤링 스크립트
│   ├── advanced_crawler.py            # 고급 크롤링 (클래스 기반)
│   ├── crawler_config.py              # 크롤링 설정 파일
│   └── run_crawler.bat                # 원클릭 실행 스크립트
│
├── 📚 03_docs/                        # 문서
│   ├── README.md                      # 기본 사용 설명서
│   ├── CRAWLING_GUIDE.md             # 크롤링 완전 가이드
│   └── PROJECT_GUIDE.md              # 전체 프로젝트 가이드
│
└── 📖 START_HERE.md                  # 이 파일 - 시작 가이드
```

---

## 🚀 빠른 시작

### 1. 라이브러리 설치 (최초 1회)
```bash
pip install pandas numpy matplotlib seaborn folium selenium beautifulsoup4 requests webdriver-manager openpyxl
```

### 2. 분석 실행
```
01_analysis/run_analysis.bat 더블클릭
```

### 3. 크롤링 실행
```
02_crawling/run_crawler.bat 더블클릭
```

---

## 📂 각 폴더 설명

### 📊 01_analysis/
**데이터 분석 및 시각화 코드**

- `gangwon_energy_analysis.py`: 
  - Pandas로 데이터 처리
  - Matplotlib/Seaborn으로 차트 생성 (5개)
  - Folium으로 인터랙티브 지도 생성
  - 한글 폰트 설정 포함

- `create_dashboard.py`:
  - 모든 차트와 지도를 통합
  - HTML 웹 대시보드 생성
  - 반응형 디자인 적용

- `run_analysis.bat`:
  - 위 두 스크립트를 자동 실행
  - 브라우저로 결과 자동 열기

### 🕷️ 02_crawling/
**웹 크롤링 코드**

- `data_crawler.py`:
  - Selenium으로 동적 페이지 크롤링
  - BeautifulSoup으로 HTML 파싱
  - 공공데이터, 기상청, 에너지공단 크롤링
  - 데이터 CSV 저장

- `advanced_crawler.py`:
  - 객체지향 크롤링 클래스
  - 테이블 자동 추출
  - 페이지네이션 처리
  - 데이터 검증 기능

- `crawler_config.py`:
  - API 키 설정
  - URL 목록
  - 크롤링 설정 (대기시간, 재시도 등)

- `run_crawler.bat`:
  - 크롤링 자동 실행
  - 모드 선택 (기본/고급/둘다)

### 📚 03_docs/
**문서 및 가이드**

- `README.md`:
  - 프로젝트 개요
  - 설치 방법
  - 기본 사용법

- `CRAWLING_GUIDE.md`:
  - 크롤링 기법 상세 설명
  - Selenium 사용법
  - BeautifulSoup 예제
  - API 활용법
  - 문제 해결

- `PROJECT_GUIDE.md`:
  - 전체 프로젝트 가이드
  - 모든 기능 설명
  - 실습 과제
  - 학습 자료

---

## 💡 사용 시나리오

### 시나리오 1: 예시 데이터로 연습
1. `01_analysis/run_analysis.bat` 실행
2. 생성된 차트와 지도 확인
3. 코드 열어서 수정해보기

### 시나리오 2: 실제 데이터 수집
1. `02_crawling/crawler_config.py`에서 API 키 설정
2. `02_crawling/run_crawler.bat` 실행
3. 수집된 CSV 파일 확인
4. `01_analysis/gangwon_energy_analysis.py`에서 데이터 경로 수정
5. 분석 다시 실행

### 시나리오 3: 커스터마이징
1. `03_docs/`의 가이드 읽기
2. 원하는 기능 찾기
3. 코드 복사해서 수정
4. 본인 프로젝트 폴더에서 작업

---

## 📖 각 파일 읽는 순서 추천

### 초보자
1. `START_HERE.md` (이 파일)
2. `03_docs/README.md`
3. `01_analysis/gangwon_energy_analysis.py` 실행
4. 코드 한 줄씩 읽어보기

### 중급자
1. `03_docs/PROJECT_GUIDE.md`
2. `02_crawling/data_crawler.py` 실행
3. `03_docs/CRAWLING_GUIDE.md`
4. 코드 수정해보기

### 고급자
1. 전체 코드 훑어보기
2. `advanced_crawler.py`로 고급 기법 학습
3. 본인 프로젝트에 적용

---

## ⚠️ 주의사항

1. **이 폴더는 샘플(참고용)**입니다
2. 실제 작업은 **본인의 프로젝트 폴더**에서 하세요
3. 샘플 코드를 **복사해서 수정**하는 방식으로 사용하세요
4. 파일 경로는 본인 환경에 맞게 수정하세요

---

## 🎯 다음 단계

1. ✅ 샘플 코드 실행해보기
2. ✅ 결과물 확인 (차트, 지도, 대시보드)
3. ✅ 코드 읽고 이해하기
4. ✅ 본인 프로젝트 폴더로 복사
5. ✅ 실제 데이터로 수정
6. ✅ 커스터마이징

---

## 💬 도움이 필요하면?

1. `03_docs/` 폴더의 가이드 문서 참고
2. 코드 주석 읽기
3. 오류 메시지 구글 검색
4. 팀원과 상의

---

**Good Luck! 🍀**
