# 웹 크롤링 설정 파일

# ==================== API 키 설정 ====================
# 실제 사용 시 본인의 API 키로 교체하세요

API_KEYS = {
    # 기상청 API
    'WEATHER_API_KEY': 'YOUR_WEATHER_API_KEY',
    
    # 공공데이터 포털 API
    'PUBLIC_DATA_API_KEY': 'YOUR_PUBLIC_DATA_API_KEY',
    
    # 한국에너지공단 API (있는 경우)
    'ENERGY_API_KEY': 'YOUR_ENERGY_API_KEY',
}

# ==================== 크롤링 대상 URL ====================
URLS = {
    # 공공데이터 포털
    'DATA_GO_KR': 'https://www.data.go.kr/index.do',
    
    # 국가통계포털
    'KOSIS': 'https://kosis.kr/index/index.do',
    
    # 기상청 기상자료개방포털
    'WEATHER': 'https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivisionList.do?pgmNo=179',
    
    # 한국에너지공단
    'ENERGY': 'https://www.knrec.or.kr/biz/statistics/stts/list.do',
    
    # 강원특별자치도
    'GANGWON': 'https://state.gwd.go.kr/portal',
    
    # 강원도 투자환경
    'INVEST_GANGWON': 'https://www.investkorea.org/gwn-kr/index.do',
}

# ==================== 크롤링 설정 ====================
CRAWLER_CONFIG = {
    # 브라우저 설정
    'HEADLESS': True,  # True: 백그라운드 실행, False: 브라우저 보이기
    'WINDOW_SIZE': '1920,1080',
    
    # 대기 시간 (초)
    'WAIT_TIME': 3,  # 페이지 로딩 대기
    'SCROLL_PAUSE': 2,  # 스크롤 간격
    'ELEMENT_TIMEOUT': 10,  # 요소 대기 시간
    
    # 페이지네이션
    'MAX_PAGES': 5,  # 최대 크롤링 페이지 수
    
    # 재시도 설정
    'MAX_RETRIES': 3,  # 최대 재시도 횟수
    'RETRY_DELAY': 5,  # 재시도 간격 (초)
}

# ==================== 데이터 저장 설정 ====================
SAVE_CONFIG = {
    # 저장 경로
    'OUTPUT_DIR': 'C:/Users/dkreh/Desktop/KDT_RE_5th/3_Project/crawled_data/',
    
    # 파일 형식
    'FILE_FORMAT': 'csv',  # csv, excel, json
    
    # CSV 설정
    'CSV_ENCODING': 'utf-8-sig',  # 한글 깨짐 방지
    'CSV_INDEX': False,
    
    # Excel 설정
    'EXCEL_ENGINE': 'openpyxl',
    
    # JSON 설정
    'JSON_ORIENT': 'records',
    'JSON_INDENT': 2,
}

# ==================== 강원도 시군 목록 ====================
GANGWON_REGIONS = [
    '춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시',
    '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군',
    '철원군', '화천군', '양구군', '인제군', '고성군', '양양군'
]

# ==================== 에너지원 목록 ====================
ENERGY_TYPES = [
    '태양광', '풍력', '수력', '바이오', '연료전지', '지열'
]

# ==================== 기상 데이터 항목 ====================
WEATHER_ITEMS = [
    '강수량',  # mm
    '일조시간',  # hr
    '일사량',  # MJ/m²
    '평균풍속',  # m/s
    '최대풍속',  # m/s
    '평균기온',  # ℃
    '최고기온',  # ℃
    '최저기온',  # ℃
]

# ==================== 검색 키워드 ====================
SEARCH_KEYWORDS = [
    '강원도 신재생에너지',
    '강원도 태양광 발전',
    '강원도 풍력 발전',
    '강원도 수력 발전',
    'RE100 강원도',
    '그린뉴딜 강원도',
    '신재생에너지 발전량',
    '신재생에너지 설비용량',
]

# ==================== 데이터 정제 규칙 ====================
DATA_CLEANING = {
    # 결측치 처리
    'FILL_METHOD': 'forward',  # forward, backward, mean, median, zero
    
    # 중복 제거
    'REMOVE_DUPLICATES': True,
    
    # 이상치 처리
    'OUTLIER_METHOD': 'IQR',  # IQR, Z-score, None
    'OUTLIER_THRESHOLD': 1.5,
}

# ==================== User-Agent 리스트 ====================
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]

# ==================== 로깅 설정 ====================
LOGGING_CONFIG = {
    'ENABLE_LOGGING': True,
    'LOG_FILE': 'C:/Users/dkreh/Desktop/KDT_RE_5th/3_Project/crawler.log',
    'LOG_LEVEL': 'INFO',  # DEBUG, INFO, WARNING, ERROR
}

# ==================== 이메일 알림 설정 (선택사항) ====================
EMAIL_CONFIG = {
    'ENABLE_EMAIL': False,
    'SMTP_SERVER': 'smtp.gmail.com',
    'SMTP_PORT': 587,
    'EMAIL_FROM': 'your_email@gmail.com',
    'EMAIL_TO': 'recipient@gmail.com',
    'EMAIL_PASSWORD': 'your_app_password',
}
