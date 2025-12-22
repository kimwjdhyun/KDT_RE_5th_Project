"""
강원도 신재생 에너지 현황 분석 - 샘플 코드
Folium 지도 + Matplotlib 차트 생성

이 파일은 참고용 샘플입니다. 본인 프로젝트 폴더에 복사해서 사용하세요.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

print("="*60)
print("강원도 신재생 에너지 현황 분석")
print("="*60)

# ==================== 데이터 준비 ====================
region_data = {
    '지역': ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', 
            '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군',
            '철원군', '화천군', '양구군', '인제군', '고성군', '양양군'],
    '태양광(GWh)': [145.2, 198.7, 176.4, 89.3, 67.8, 92.1, 
                   134.5, 156.8, 112.3, 98.7, 87.4, 76.5,
                   145.3, 89.6, 67.8, 54.3, 98.5, 87.9],
    '풍력(GWh)': [23.5, 15.2, 145.8, 78.5, 198.3, 56.4,
                 167.9, 34.2, 21.5, 45.3, 189.6, 123.7,
                 67.8, 34.5, 45.6, 56.7, 89.3, 112.5],
    '수력(GWh)': [89.3, 34.1, 12.3, 5.2, 15.7, 8.9,
                 45.6, 123.4, 67.8, 89.2, 56.3, 145.8,
                 23.4, 234.7, 78.9, 156.8, 12.4, 23.6],
    '위도': [37.8813, 37.3422, 37.7519, 37.5247, 37.1640, 38.2070,
            37.4500, 37.6974, 37.4828, 37.1836, 37.3709, 37.3807,
            38.1467, 38.1063, 38.1098, 38.0695, 38.3806, 38.0750],
    '경도': [127.7298, 127.9202, 128.8760, 129.1143, 128.9856, 128.5918,
            129.1658, 127.8895, 127.9844, 128.4614, 128.3906, 128.6686,
            127.3136, 127.7084, 127.9897, 128.1706, 128.4692, 128.6190]
}

df = pd.DataFrame(region_data)
df['총발전량(GWh)'] = df['태양광(GWh)'] + df['풍력(GWh)'] + df['수력(GWh)']

print("\n✅ 데이터 로드 완료")
print(df.head())

# ==================== 차트 생성 ====================
print("\n[차트 생성 중...]")

# 1. 시군별 총 발전량
fig, ax = plt.subplots(figsize=(14, 6))
df_sorted = df.sort_values('총발전량(GWh)', ascending=False)
ax.bar(df_sorted['지역'], df_sorted['총발전량(GWh)'], color='#4CAF50')
ax.set_xlabel('지역', fontsize=12, fontweight='bold')
ax.set_ylabel('총 발전량 (GWh)', fontsize=12, fontweight='bold')
ax.set_title('강원도 시군별 총 발전량', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('./chart1_total.png', dpi=300, bbox_inches='tight')
print("✅ chart1_total.png 저장")

# 2. 에너지원별 스택 바
fig, ax = plt.subplots(figsize=(14, 6))
x = range(len(df))
ax.bar(x, df['태양광(GWh)'], label='태양광', color='#FFB800')
ax.bar(x, df['풍력(GWh)'], bottom=df['태양광(GWh)'], label='풍력', color='#00C4FF')
ax.bar(x, df['수력(GWh)'], bottom=df['태양광(GWh)']+df['풍력(GWh)'], label='수력', color='#0066FF')
ax.set_xticks(x)
ax.set_xticklabels(df['지역'], rotation=45, ha='right')
ax.set_ylabel('발전량 (GWh)')
ax.set_title('에너지원별 발전량')
ax.legend()
plt.tight_layout()
plt.savefig('./chart2_stack.png', dpi=300, bbox_inches='tight')
print("✅ chart2_stack.png 저장")

plt.close('all')

# ==================== Folium 지도 생성 ====================
print("\n[Folium 지도 생성 중...]")

m = folium.Map(location=[37.8228, 128.1555], zoom_start=9)

for idx, row in df.iterrows():
    if row['총발전량(GWh)'] > 300:
        color = 'red'
    elif row['총발전량(GWh)'] > 200:
        color = 'orange'
    else:
        color = 'green'
    
    popup_html = f"""
    <div style="font-family: Malgun Gothic; width: 200px;">
        <h4>{row['지역']}</h4>
        <p>🔆 태양광: {row['태양광(GWh)']} GWh</p>
        <p>💨 풍력: {row['풍력(GWh)']} GWh</p>
        <p>💧 수력: {row['수력(GWh)']} GWh</p>
        <p><b>⚡ 총: {row['총발전량(GWh)']:.1f} GWh</b></p>
    </div>
    """
    
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=row['지역'],
        icon=folium.Icon(color=color, icon='bolt', prefix='fa')
    ).add_to(m)

m.save('./gangwon_map.html')
print("✅ gangwon_map.html 저장")

print("\n" + "="*60)
print("✅ 모든 작업 완료!")
print("="*60)
print("\n생성된 파일:")
print("  - chart1_total.png")
print("  - chart2_stack.png")
print("  - gangwon_map.html")
