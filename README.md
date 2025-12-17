# 강원도 신재생에너지 분석 프로젝트

## 프로젝트 개요
강원도 RE100 및 그린 뉴딜 정책 기반 신재생 에너지 산업 분석

## 팀원
- 천예리: 정책 자료 정리, 분석 설계, 결과 해석
- 김정현: 데이터 수집 자동화, 전처리, 시각화

## 프로젝트 구조
```
KDT-RE-DataAnalysis/
├── data/
│   ├── raw/              # 원본 데이터
│   ├── processed/        # 전처리된 데이터
│   └── policy/           # 정책 자료
├── scripts/
│   ├── crawling/         # 크롤링 스크립트
│   └── preprocessing/    # 전처리 스크립트
├── notebooks/            # 분석용 Jupyter Notebook
├── docs/                 # 문서
├── results/              # 분석 결과
│   ├── figures/          # 그래프/차트
│   └── tables/           # 통계 테이블
└── README.md
```

## 설치 방법

### 1. 가상환경 생성 (권장)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 필요 라이브러리 설치
```bash
pip install pandas numpy matplotlib seaborn
pip install requests beautifulsoup4 selenium
pip install folium jupyter
```

## 실행 방법

### 전체 파이프라인 실행 (샘플 데이터)
```bash
python run_pipeline.py --sample
```

### 실제 데이터로 실행
```bash
python run_pipeline.py --real-data
```

### 단계별 실행
```bash
# 1. 데이터 수집
python scripts/renewable_energy_crawler.py

# 2. 기상 데이터 수집
python scripts/weather_data_crawler.py

# 3. 데이터 전처리
python scripts/data_preprocessing.py

# 4. 데이터 통합
python scripts/data_integration.py
```

## 데이터 소스

### 신재생에너지 발전량
- **출처**: 한국에너지공단 신재생에너지센터
- **URL**: https://www.knrec.or.kr/biz/pds/statistic/list.do
- **내용**: 지역별/에너지원별 발전량, 설비용량

### 기상 데이터
- **출처**: 기상청 기상자료개방포털
- **URL**: https://data.kma.go.kr
- **내용**: 일사량, 풍속, 강수량, 기온
- **참고**: API 키 발급 필요

### 정책 및 예산
- **출처**: 강원특별자치도청
- **URL**: https://state.gwd.go.kr/portal
- **내용**: 그린뉴딜 예산, RE100 정책

## 분석 목표

### 핵심 분석 질문
1. 기후 요인은 강원도 신재생에너지 발전량에 얼마나 영향을 미치는가?
2. 정책 예산 투입 전후 발전량 변화는 통계적으로 유의미한가?
3. 강원도는 타 시도 대비 RE100 산업 입지로서 어떤 강약점을 가지는가?

### 분석 방법
- 상관관계 분석
- 시계열 분석
- 회귀 모델
- 시각화 및 지도 매핑

## Git Commit 규칙

### Conventional Commits 사용
- `feat:` 새로운 기능 추가
- `fix:` 버그 수정
- `docs:` 문서 수정
- `style:` 코드 스타일 변경
- `refactor:` 코드 리팩토링

### 예시
```bash
git commit -m "feat: 강원도 발전량 시계열 분석 추가"
git commit -m "fix: 연도별 발전량 집계 오류 수정"
```

## 일정

- **1단계** (12.15~12.17): 주제 선정, 계획 수립
- **2단계** (12.17~12.24): 데이터 수집 및 전처리
- **3단계** (12.24~01.07): 데이터 분석 및 시각화
- **4단계** (01.07~01.12): 결과 검증 및 보고서 작성
- **최종** (01.13): 결과 발표

## 문의사항
- GitHub Issues 활용
- Slack 채널: #kdt-re-analysis

## 라이선스
MIT License
