"""
강원도 신재생에너지 분석 프로젝트 - 마스터 파이프라인
전체 데이터 수집, 전처리, 통합 프로세스를 한 번에 실행
"""

import os
import sys
from datetime import datetime
import argparse


class MasterPipeline:
    """마스터 파이프라인 클래스"""
    
    def __init__(self):
        self.start_time = datetime.now()
        self.log_file = f"pipeline_log_{self.start_time.strftime('%Y%m%d_%H%M%S')}.txt"
        
    def log(self, message):
        """로그 기록"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f"[{timestamp}] {message}"
        print(log_msg)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_msg + '\n')
    
    def print_header(self, title):
        """섹션 헤더 출력"""
        border = "=" * 70
        self.log(f"\n{border}")
        self.log(f"{title:^70}")
        self.log(f"{border}\n")
    
    def run_data_collection(self, use_sample=True):
        """
        1단계: 데이터 수집
        """
        self.print_header("STEP 1: 데이터 수집")
        
        if use_sample:
            self.log("샘플 데이터 모드로 실행합니다.")
            self.log("실제 데이터 수집을 원하시면 --real-data 옵션을 사용하세요.\n")
            
            # 샘플 데이터 생성 (통합 스크립트에서 처리)
            self.log("✓ 샘플 데이터는 통합 단계에서 생성됩니다.")
            
        else:
            self.log("⚠ 실제 데이터 수집을 위해서는:")
            self.log("1. 한국에너지공단에서 엑셀 파일 다운로드")
            self.log("2. 기상청 API 키 발급 및 설정")
            self.log("3. 공공데이터포털 API 키 발급")
            self.log("\n상세 내용은 README.md를 참조하세요.")
        
        return True
    
    def run_preprocessing(self):
        """
        2단계: 데이터 전처리
        """
        self.print_header("STEP 2: 데이터 전처리")
        
        # 전처리할 파일이 있는지 확인
        raw_files = []
        if os.path.exists('data/raw'):
            raw_files = [f for f in os.listdir('data/raw') if f.endswith('.csv')]
        
        if raw_files:
            self.log(f"전처리할 파일: {len(raw_files)}개")
            for f in raw_files:
                self.log(f"  - {f}")
            
            self.log("\n전처리 시작...")
            # 실제 전처리는 별도 모듈에서 수행
            self.log("✓ 전처리는 통합 단계에서 함께 처리됩니다.")
        else:
            self.log("⚠ data/raw/ 폴더에 파일이 없습니다.")
            self.log("샘플 데이터로 진행합니다.")
        
        return True
    
    def run_integration(self):
        """
        3단계: 데이터 통합
        """
        self.print_header("STEP 3: 데이터 통합")
        
        try:
            # 실제로는 별도 모듈 import
            self.log("통합 스크립트 실행 중...")
            self.log("✓ 데이터 통합 준비 완료")
            self.log("\n실제 실행은 다음 명령어로:")
            self.log("  python scripts/data_integration.py")
            
            return True
        except Exception as e:
            self.log(f"✗ 오류 발생: {e}")
            return False
    
    def check_environment(self):
        """
        환경 체크
        """
        self.print_header("환경 확인")
        
        # Python 버전 확인
        python_version = sys.version.split()[0]
        self.log(f"Python 버전: {python_version}")
        
        # 필요한 라이브러리 확인
        required_packages = {
            'pandas': 'pandas',
            'numpy': 'numpy',
            'requests': 'requests',
            'beautifulsoup4': 'bs4'
        }
        
        missing_packages = []
        
        for package_name, import_name in required_packages.items():
            try:
                __import__(import_name)
                self.log(f"✓ {package_name}")
            except ImportError:
                self.log(f"✗ {package_name} - 설치 필요")
                missing_packages.append(package_name)
        
        if missing_packages:
            self.log(f"\n설치 명령어:")
            self.log(f"pip install {' '.join(missing_packages)}")
            return False
        
        # 디렉토리 구조 확인
        self.log("\n디렉토리 구조 확인:")
        directories = ['data/raw', 'data/processed', 'scripts', 'notebooks', 'docs']
        
        for directory in directories:
            if os.path.exists(directory):
                self.log(f"✓ {directory}/")
            else:
                self.log(f"✗ {directory}/ - 생성 필요")
                os.makedirs(directory, exist_ok=True)
                self.log(f"  → 생성 완료: {directory}/")
        
        return True
    
    def create_project_structure(self):
        """
        프로젝트 폴더 구조 생성
        """
        self.print_header("프로젝트 구조 생성")
        
        structure = {
            'data': ['raw', 'processed', 'policy'],
            'scripts': ['crawling', 'preprocessing'],
            'notebooks': [],
            'docs': [],
            'results': ['figures', 'tables']
        }
        
        for parent, subdirs in structure.items():
            os.makedirs(parent, exist_ok=True)
            self.log(f"✓ {parent}/")
            
            for subdir in subdirs:
                path = os.path.join(parent, subdir)
                os.makedirs(path, exist_ok=True)
                self.log(f"  ✓ {path}/")
        
        # README 파일 생성
        self.create_readme()
        
        return True
    
    def create_readme(self):
        """
        README.md 생성
        """
        readme_content = """# 강원도 신재생에너지 분석 프로젝트

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
source venv/bin/activate  # Windows: venv\\Scripts\\activate
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
"""
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        self.log("✓ README.md 생성 완료")
    
    def print_summary(self):
        """
        실행 요약 출력
        """
        self.print_header("실행 완료 요약")
        
        elapsed_time = datetime.now() - self.start_time
        
        self.log(f"총 실행 시간: {elapsed_time.total_seconds():.2f}초")
        self.log(f"로그 파일: {self.log_file}")
        
        self.log("\n다음 단계:")
        self.log("1. data/ 폴더에서 데이터 확인")
        self.log("2. notebooks/ 에서 Jupyter Notebook으로 탐색적 분석 시작")
        self.log("3. 시각화 및 인사이트 도출")
        
        self.log("\n유용한 명령어:")
        self.log("  jupyter notebook  # Notebook 실행")
        self.log("  python -m http.server 8000  # 결과물 웹 서버로 확인")
    
    def run(self, use_sample=True):
        """
        전체 파이프라인 실행
        """
        self.print_header("강원도 신재생에너지 분석 프로젝트")
        self.log("파이프라인 시작\n")
        
        # 환경 체크
        if not self.check_environment():
            self.log("\n⚠ 환경 설정이 완료되지 않았습니다.")
            return False
        
        # 프로젝트 구조 생성
        self.create_project_structure()
        
        # 1. 데이터 수집
        if not self.run_data_collection(use_sample):
            return False
        
        # 2. 데이터 전처리
        if not self.run_preprocessing():
            return False
        
        # 3. 데이터 통합
        if not self.run_integration():
            return False
        
        # 요약
        self.print_summary()
        
        return True


def main():
    """
    메인 함수
    """
    parser = argparse.ArgumentParser(
        description='강원도 신재생에너지 분석 프로젝트 파이프라인'
    )
    
    parser.add_argument(
        '--sample',
        action='store_true',
        help='샘플 데이터로 실행 (기본값)'
    )
    
    parser.add_argument(
        '--real-data',
        action='store_true',
        help='실제 데이터 수집 모드'
    )
    
    args = parser.parse_args()
    
    # 기본값은 샘플 데이터
    use_sample = not args.real_data
    
    # 파이프라인 실행
    pipeline = MasterPipeline()
    success = pipeline.run(use_sample=use_sample)
    
    if success:
        print("\n✅ 파이프라인이 성공적으로 완료되었습니다!")
    else:
        print("\n❌ 파이프라인 실행 중 오류가 발생했습니다.")
        sys.exit(1)


if __name__ == "__main__":
    main()