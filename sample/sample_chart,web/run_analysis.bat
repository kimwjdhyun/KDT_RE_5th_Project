@echo off
chcp 65001 > nul
echo ====================================
echo 강원도 신재생 에너지 분석 프로젝트
echo ====================================
echo.

echo [1단계] 필요한 라이브러리 확인 중...
python -c "import pandas, numpy, matplotlib, seaborn, folium" 2>nul
if errorlevel 1 (
    echo ❌ 라이브러리가 설치되어 있지 않습니다.
    echo.
    echo 다음 명령어로 설치해주세요:
    echo pip install pandas numpy matplotlib seaborn folium
    echo.
    pause
    exit /b 1
) else (
    echo ✅ 라이브러리 확인 완료!
)
echo.

echo [2단계] 데이터 분석 및 시각화 생성 중...
python gangwon_energy_analysis.py
if errorlevel 1 (
    echo ❌ 분석 실행 실패
    pause
    exit /b 1
)
echo ✅ 차트 및 지도 생성 완료!
echo.

echo [3단계] HTML 대시보드 생성 중...
python create_dashboard.py
if errorlevel 1 (
    echo ❌ 대시보드 생성 실패
    pause
    exit /b 1
)
echo ✅ 대시보드 생성 완료!
echo.

echo ====================================
echo 🎉 모든 작업이 완료되었습니다!
echo ====================================
echo.
echo 📁 생성된 파일:
echo   - gangwon_energy_map.html (Folium 지도)
echo   - chart1~5.png (분석 차트)
echo   - gangwon_energy_dashboard.html (통합 대시보드)
echo.
echo 🌐 대시보드를 브라우저로 여는 중...
start gangwon_energy_dashboard.html
echo.
echo ✨ 완료!
pause
