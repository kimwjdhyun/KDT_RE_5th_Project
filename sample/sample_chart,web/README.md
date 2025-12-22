# 강원도 신재생 에너지 현황 분석 프로젝트

## 📌 프로젝트 개요
강원도 18개 시군의 신재생 에너지 발전 현황을 데이터 기반으로 분석하고 시각화하는 프로젝트입니다.

---

## 🛠️ 필요한 라이브러리 설치

터미널이나 명령 프롬프트에서 다음 명령어를 실행하세요:

```bash
pip install pandas numpy matplotlib seaborn folium
```

---

## 📂 프로젝트 파일 구조

```
3_Project/
├── gangwon_energy_analysis.py      # 데이터 분석 및 차트/지도 생성
├── create_dashboard.py              # HTML 웹페이지 생성
├── README.md                        # 이 파일
├── gangwon_energy_dashboard.html   # 최종 웹페이지 (실행 후 생성됨)
├── gangwon_energy_map.html         # Folium 지도 (실행 후 생성됨)
└── chart1~5.png                    # 분석 차트들 (실행 후 생성됨)
```

---

## 🚀 실행 방법

### 1단계: 데이터 분석 및 시각화 생성

```bash
python gangwon_energy_analysis.py
```

이 스크립트는 다음을 생성합니다:
- ✅ chart1_total_generation.png - 시군별 총 발전량
- ✅ chart2_energy_sources.png - 에너지원별 발전량
- ✅ chart3_yearly_trend.png - 연도별 추이
- ✅ chart4_energy_ratio.png - 에너지 비중
- ✅ chart5_correlation.png - 상관관계 분석
- ✅ gangwon_energy_map.html - Folium 인터랙티브 지도

### 2단계: HTML 웹페이지 생성

```bash
python create_dashboard.py
```

이 스크립트는 다음을 생성합니다:
- ✅ gangwon_energy_dashboard.html - 통합 대시보드

### 3단계: 웹페이지 확인

`gangwon_energy_dashboard.html` 파일을 더블클릭하거나 브라우저로 열어서 확인하세요!

---

## 📊 생성되는 분석 결과

### 1. 인터랙티브 지도 (Folium)
- 강원도 18개 시군의 위치와 발전량을 시각화
- 마커 클릭 시 상세 정보 팝업
- 발전량에 따른 색상 구분 (빨강/주황/초록)
- 원의 크기로 발전량 규모 표현

### 2. 데이터 분석 차트 (Matplotlib + Seaborn)
- **차트 1**: 지역별 총 발전량 막대 그래프
- **차트 2**: 에너지원별 스택 바 차트
- **차트 3**: 연도별 발전량 추이 라인 차트
- **차트 4**: 에너지원별 비중 파이 차트
- **차트 5**: 기상 조건 상관관계 히트맵

### 3. 통합 웹 대시보드
- 모든 차트와 지도를 하나의 웹페이지에 통합
- 반응형 디자인 (모바일/태블릿/PC 지원)
- 주요 통계 카드
- 분석 결과 및 인사이트 제공

---

## 🎨 주요 기능

### Folium 지도의 특징
```python
- 마커: 지역별 발전소 위치 표시
- 팝업: 클릭 시 상세 정보 (태양광/풍력/수력/기상 데이터)
- 원: 발전량에 비례하는 크기
- 색상: 발전량 수준 구분
```

### 차트의 특징
```python
- 한글 폰트 지원 (Malgun Gothic)
- 고해상도 이미지 (300 DPI)
- 색상 코드 통일 (태양광=#FFB800, 풍력=#00C4FF, 수력=#0066FF)
- 그리드 및 범례 포함
```

---

## 💡 커스터마이징 방법

### 1. 실제 데이터로 업데이트하기

`gangwon_energy_analysis.py` 파일에서 다음 부분을 수정하세요:

```python
# 강원도 시군별 데이터
region_data = {
    '지역': ['춘천시', '원주시', ...],
    '태양광(GWh)': [145.2, 198.7, ...],  # <- 여기에 실제 데이터 입력
    '풍력(GWh)': [23.5, 15.2, ...],
    # ... 나머지 데이터
}
```

### 2. 차트 스타일 변경하기

색상 변경:
```python
colors = ['#FFB800', '#00C4FF', '#0066FF']  # 원하는 색상 코드로 변경
```

차트 크기 변경:
```python
fig, ax = plt.subplots(figsize=(14, 6))  # (너비, 높이) 조정
```

### 3. HTML 디자인 변경하기

`create_dashboard.py`의 CSS 부분을 수정하세요:
```css
background: linear-gradient(135deg, #e3f2fd 0%, #e8f5e9 100%);
/* 배경 그라데이션 변경 */
```

---

## 📚 학습한 기술 스택

- **Python 3.14**: 프로그래밍 언어
- **Pandas**: 데이터 처리 및 분석
- **NumPy**: 수치 계산
- **Matplotlib**: 차트 시각화
- **Seaborn**: 고급 통계 시각화
- **Folium**: 인터랙티브 지도

---

## 🔧 문제 해결

### 한글 깨짐 문제
```python
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# 또는
plt.rcParams['font.family'] = 'AppleGothic'    # Mac
```

### 경로 오류
```python
# 절대 경로 대신 상대 경로 사용
plt.savefig('./chart1.png')
```

### 지도가 표시되지 않음
- 인터넷 연결 확인 (OpenStreetMap 타일 로딩)
- 브라우저 캐시 삭제 후 재시도

---

## 📈 분석 결과 예시

### 주요 인사이트
1. **화천군**: 수력 발전 최고 (234.7 GWh)
2. **태백시/평창군**: 풍력 발전 강점 (산악 지형)
3. **원주시**: 태양광 발전 1위 (198.7 GWh)
4. **2019-2024**: 태양광 97.3% 증가, 풍력 112.1% 증가

### RE100 경쟁력
- ✅ 다양한 에너지원 포트폴리오
- ✅ 풍부한 신재생 에너지 잠재력
- ✅ 그린 뉴딜 정책 지원
- ⚠️ 지역별 편차 및 인프라 개선 필요

---

## 👥 팀 정보

**포스코 x 코딩온 신재생에너지 IoT개발자 과정 5기 1조**
- 김정현: 데이터 수집 자동화, 전처리, 시각화
- 천예리: 정책 자료 정리, 분석 설계, 결과 해석

---

## 📞 추가 도움말

문제가 발생하면:
1. Python과 라이브러리 버전 확인
2. 경로가 올바른지 확인
3. 파일 권한 확인
4. 오류 메시지를 자세히 읽어보기

---

## 🎯 다음 단계

1. 실제 데이터 수집 (공공데이터 포털, 기상청)
2. 웹 크롤링으로 자동화
3. 머신러닝 예측 모델 추가
4. 실시간 업데이트 기능 구현

---

**Happy Coding! 🚀**
