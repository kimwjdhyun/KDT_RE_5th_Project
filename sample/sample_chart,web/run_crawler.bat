@echo off
chcp 65001 > nul
echo ╔══════════════════════════════════════════════════════════╗
echo ║     강원도 신재생 에너지 데이터 크롤링 실행          ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

echo [확인] 필요한 라이브러리 확인 중...
python -c "import selenium, bs4, requests, pandas, webdriver_manager" 2>nul
if errorlevel 1 (
    echo ❌ 필요한 라이브러리가 설치되어 있지 않습니다.
    echo.
    echo 다음 명령어로 설치해주세요:
    echo pip install selenium beautifulsoup4 requests pandas webdriver-manager openpyxl
    echo.
    pause
    exit /b 1
) else (
    echo ✅ 라이브러리 확인 완료!
)
echo.

echo ╔══════════════════════════════════════════════════════════╗
echo ║                크롤링 모드 선택                       ║
echo ╚══════════════════════════════════════════════════════════╝
echo.
echo [1] 기본 크롤링 (data_crawler.py)
echo     - 공공데이터 포털 검색
echo     - 기상청, 에너지공단 페이지 접속
echo     - 예시 데이터 생성
echo.
echo [2] 고급 크롤링 (advanced_crawler.py)
echo     - 동적 페이지 처리
echo     - 테이블 자동 추출
echo     - 데이터 검증
echo.
echo [3] 둘 다 실행
echo.

set /p choice="선택하세요 (1/2/3): "

if "%choice%"=="1" goto basic
if "%choice%"=="2" goto advanced
if "%choice%"=="3" goto both
echo ❌ 잘못된 선택입니다.
pause
exit /b 1

:basic
echo.
echo [실행] 기본 크롤링 시작...
python data_crawler.py
if errorlevel 1 (
    echo ❌ 크롤링 실패
    pause
    exit /b 1
)
echo ✅ 기본 크롤링 완료!
goto end

:advanced
echo.
echo [실행] 고급 크롤링 시작...
python advanced_crawler.py
if errorlevel 1 (
    echo ❌ 크롤링 실패
    pause
    exit /b 1
)
echo ✅ 고급 크롤링 완료!
goto end

:both
echo.
echo [실행] 기본 크롤링 시작...
python data_crawler.py
if errorlevel 1 (
    echo ❌ 기본 크롤링 실패
    pause
    exit /b 1
)
echo ✅ 기본 크롤링 완료!
echo.
echo [실행] 고급 크롤링 시작...
python advanced_crawler.py
if errorlevel 1 (
    echo ❌ 고급 크롤링 실패
    pause
    exit /b 1
)
echo ✅ 고급 크롤링 완료!

:end
echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║              크롤링 작업 완료!                        ║
echo ╚══════════════════════════════════════════════════════════╝
echo.
echo 📁 수집된 데이터 파일:
dir /b *.csv 2>nul
echo.
echo 💡 다음 단계:
echo    1. 수집된 데이터 확인
echo    2. gangwon_energy_analysis.py로 분석 실행
echo    3. 대시보드 생성
echo.
pause
