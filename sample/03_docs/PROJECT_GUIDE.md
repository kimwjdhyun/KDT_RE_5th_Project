# 프로젝트 전체 가이드 - 요약 버전

## 📊 프로젝트 개요

강원도 신재생 에너지 발전 현황을 데이터 기반으로 분석하고 시각화하는 프로젝트

---

## 🛠️ 기술 스택

### 데이터 분석
- **Pandas**: 데이터 처리
- **NumPy**: 수치 계산
- **Matplotlib**: 차트 생성
- **Seaborn**: 고급 시각화
- **Folium**: 지도 시각화

### 웹 크롤링
- **Selenium**: 동적 페이지 크롤링
- **BeautifulSoup**: HTML 파싱
- **Requests**: HTTP 요청

---

## 📈 주요 분석 내용

1. **지역별 발전량 분석**
   - 18개 시군별 총 발전량
   - 에너지원별 비중 (태양광/풍력/수력)

2. **시각화**
   - 막대 그래프: 지역별 비교
   - 라인 차트: 연도별 추이
   - 파이 차트: 에너지 비중
   - 히트맵: 상관관계
   - 지도: 인터랙티브 시각화

3. **인사이트 도출**
   - RE100 산업 경쟁력
   - 그린 뉴딜 정책 효과
   - 최적 입지 조건

---

## 🎯 학습 목표

### 초급
- [ ] Pandas로 데이터 읽기/쓰기
- [ ] Matplotlib로 기본 차트 그리기
- [ ] Folium으로 지도 만들기

### 중급
- [ ] 데이터 전처리 (결측치, 중복)
- [ ] 다양한 차트 활용
- [ ] 웹 크롤링 기초

### 고급
- [ ] 데이터 자동 수집
- [ ] 통계 분석
- [ ] 대시보드 구축

---

## 💡 실전 팁

### Pandas 핵심
```python
# CSV 읽기
df = pd.read_csv('data.csv', encoding='utf-8-sig')

# 데이터 확인
df.head()
df.info()
df.describe()

# 결측치 처리
df.fillna(0, inplace=True)

# CSV 저장
df.to_csv('output.csv', index=False, encoding='utf-8-sig')
```

### Matplotlib 핵심
```python
# 한글 폰트
plt.rcParams['font.family'] = 'Malgun Gothic'

# 차트 생성
plt.figure(figsize=(10, 6))
plt.bar(x, y)
plt.xlabel('X축')
plt.ylabel('Y축')
plt.title('제목')
plt.savefig('chart.png', dpi=300)
```

### Folium 핵심
```python
# 지도 생성
m = folium.Map(location=[위도, 경도], zoom_start=9)

# 마커 추가
folium.Marker(
    [위도, 경도],
    popup='내용',
    icon=folium.Icon(color='red')
).add_to(m)

# 저장
m.save('map.html')
```

---

## 🔧 자주 하는 실수

### 1. 한글 깨짐
```python
# ❌ 틀림
df.to_csv('data.csv')

# ✅ 맞음
df.to_csv('data.csv', encoding='utf-8-sig')
```

### 2. 경로 오류
```python
# ❌ 틀림
df = pd.read_csv('data.csv')  # 파일이 없으면 오류

# ✅ 맞음
import os
if os.path.exists('data.csv'):
    df = pd.read_csv('data.csv')
```

### 3. 폰트 설정 안 함
```python
# ❌ 틀림
plt.title('한글제목')  # 깨져 보임

# ✅ 맞음
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.title('한글제목')
```

---

## 📚 참고 자료

- Pandas 공식 문서: https://pandas.pydata.org
- Matplotlib 공식 문서: https://matplotlib.org
- Folium 문서: https://python-visualization.github.io/folium/

---

더 자세한 내용은 원본 `PROJECT_GUIDE.md` 참고!
