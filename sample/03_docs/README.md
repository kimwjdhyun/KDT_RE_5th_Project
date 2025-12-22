# 강원도 신재생 에너지 분석 프로젝트 - 샘플 코드

## 📌 이 폴더는?

이 폴더는 **참고용 샘플 코드**입니다. 제가 만든 모든 코드와 가이드를 정리해놓았어요.

---

## 📂 폴더 구조

```
sample/
│
├── 01_analysis/              # 데이터 분석 & 시각화
│   └── gangwon_energy_analysis.py
│
├── 02_crawling/              # 웹 크롤링
│   ├── data_crawler.py
│   └── crawler_config.py
│
├── 03_docs/                  # 가이드 문서
│   ├── README.md
│   ├── CRAWLING_GUIDE.md
│   └── PROJECT_GUIDE.md
│
└── START_HERE.md            # 시작 가이드
```

---

## 🚀 사용 방법

### 1. 샘플 코드 실행해보기

```bash
# 분석 코드 실행
cd 01_analysis
python gangwon_energy_analysis.py

# 크롤링 코드 실행
cd 02_crawling
python data_crawler.py
```

### 2. 본인 프로젝트에 적용하기

1. 원하는 파일을 **복사**
2. 본인 프로젝트 폴더에 **붙여넣기**
3. 파일 경로와 데이터 **수정**
4. 실행!

---

## 📚 문서 읽는 순서

1. **START_HERE.md** ← 지금 여기!
2. **03_docs/README.md** - 기본 사용법
3. **03_docs/CRAWLING_GUIDE.md** - 크롤링 상세 가이드
4. **03_docs/PROJECT_GUIDE.md** - 전체 가이드

---

## 💡 주요 기능

### 📊 분석 코드 (01_analysis/)
- Pandas: 데이터 처리
- Matplotlib: 차트 생성
- Folium: 지도 시각화
- 한글 폰트 설정 포함

### 🕷️ 크롤링 코드 (02_crawling/)
- Selenium: 동적 페이지
- BeautifulSoup: HTML 파싱
- 설정 파일 분리
- 에러 처리 포함

---

## ⚠️ 중요!

1. 이 폴더는 **읽기 전용**으로 사용하세요
2. 실제 작업은 **본인 프로젝트 폴더**에서!
3. 코드를 **복사해서 수정**하는 방식 추천
4. 파일 경로는 꼭 본인 환경에 맞게 수정!

---

## 🎯 학습 포인트

### 초보자
- [ ] 샘플 코드 실행해보기
- [ ] 결과물 확인 (차트, 지도)
- [ ] 코드 주석 읽어보기
- [ ] 간단한 값 바꿔보기

### 중급자
- [ ] 전체 코드 이해하기
- [ ] 새로운 차트 추가해보기
- [ ] 크롤링 대상 변경해보기
- [ ] 본인 데이터로 수정

### 고급자
- [ ] 코드 구조 개선
- [ ] 기능 확장 (DB 연동 등)
- [ ] 자동화 스케줄러 추가
- [ ] 배포 준비

---

## 🛠️ 필요한 라이브러리

```bash
pip install pandas numpy matplotlib seaborn folium selenium beautifulsoup4 requests webdriver-manager openpyxl
```

---

## 📞 도움이 필요하면?

1. `03_docs/` 폴더의 가이드 문서 참고
2. 코드의 주석 읽기
3. 오류 메시지 구글 검색
4. 팀원과 상의

---

**Happy Coding! 🚀**
