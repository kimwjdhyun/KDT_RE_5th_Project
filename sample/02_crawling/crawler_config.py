# 크롤링 설정 파일 - 샘플

# ==================== API 키 ====================
API_KEYS = {
    'WEATHER_API_KEY': 'YOUR_API_KEY_HERE',
    'PUBLIC_DATA_API_KEY': 'YOUR_API_KEY_HERE',
}

# ==================== URL ====================
URLS = {
    'DATA_GO_KR': 'https://www.data.go.kr/index.do',
    'KOSIS': 'https://kosis.kr/index/index.do',
    'WEATHER': 'https://data.kma.go.kr',
    'ENERGY': 'https://www.knrec.or.kr',
}

# ==================== 크롤링 설정 ====================
CONFIG = {
    'HEADLESS': True,           # 백그라운드 실행
    'WAIT_TIME': 3,             # 페이지 로딩 대기 (초)
    'MAX_PAGES': 5,             # 최대 페이지 수
}

# ==================== 강원도 지역 ====================
REGIONS = [
    '춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시',
    '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군',
    '철원군', '화천군', '양구군', '인제군', '고성군', '양양군'
]
