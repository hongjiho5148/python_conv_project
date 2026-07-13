# 편의점 행사 통합 대시보드

CU, GS25, 7-Eleven, emart24의 행사 상품 데이터를 수집하고 정제해 사용자가 가격, 행사 유형, 브랜드, 카테고리 기준으로 비교할 수 있도록 만든 Streamlit 기반 데이터 대시보드입니다.

이 프로젝트는 단순한 상품 목록 화면이 아니라, 서로 다른 편의점 사이트의 데이터 구조를 공통 스키마로 통합하고 배치 작업으로 갱신 가능한 분석용 데이터셋을 만드는 데 초점을 두었습니다.

## 목차

- [팀 소개](#팀-소개)
- [서비스 개요](#서비스-개요)
- [주요 기능](#주요-기능)
- [기술 스택](#기술-스택)
- [프로젝트 구조](#프로젝트-구조)
- [데이터 파이프라인](#데이터-파이프라인)
- [실행 방법](#실행-방법)
- [Git 협업 정보](#git-협업-정보)
- [트러블슈팅 및 개선점](#트러블슈팅-및-개선점)

## 팀 소개

편의점 행사 상품 데이터의 수집, 정제, 분석, 시각화, 추천 기능을 함께 구현한 6인 팀 프로젝트입니다.

| 김한진(팀장) | 이시연 | 임서연 | 김현석A | 이세영 | 홍지호 |
| --- | --- | --- | --- | --- | --- |
| <img src="https://github.com/Engineer-kim.png" width="120" alt="김한진"> | <img src="https://github.com/siyeon04.png" width="120" alt="이시연"> | <img src="https://github.com/seoyeon020.png" width="120" alt="임서연"> | <img src="https://github.com/Hyeonseok93.png" width="120" alt="김현석A"> | <img src="https://github.com/owhat02.png" width="120" alt="이세영"> | <img src="https://github.com/hongjiho5148.png" width="120" alt="홍지호"> |
| ![Leader](https://img.shields.io/badge/Leader-FFD43B) ![Data](https://img.shields.io/badge/Data_Crawling-2F9E44) | ![Data](https://img.shields.io/badge/Data_Cleaning-2F9E44) ![Planning](https://img.shields.io/badge/Planning-1971C2) | ![Data](https://img.shields.io/badge/Data_Analysis-2F9E44) ![Dashboard](https://img.shields.io/badge/Dashboard-1971C2) | ![Crawling](https://img.shields.io/badge/Crawling-2F9E44) ![Frontend](https://img.shields.io/badge/UI-1971C2) | ![Crawling](https://img.shields.io/badge/Crawling-2F9E44) ![UX](https://img.shields.io/badge/UX_Planning-1971C2) | ![Crawling](https://img.shields.io/badge/Crawling-2F9E44) ![Dashboard](https://img.shields.io/badge/Dashboard-1971C2) |
| 7-Eleven 행사 상품 크롤링, 대시보드 기획, 메인 페이지 테스트, 챗봇 로직 수정 | 수집 데이터 정제/분석, 목적 기반 상품 분류 기획, 장바구니 기능, 발표 준비 | 데이터 분석/정제, 시각화 대시보드 기능 기획, 시간대별 상품 추천, 기능 테스트 | emart24 행사 정보 크롤링 도구, 카테고리 그래프 UI, 야식/럭키박스/매장 찾기 기능 | GS25 행사 상품 크롤링, 검색 기반 추천 UX, 행사 뉴스 크롤링, 기능 테스트 | CU 행사 상품 크롤링 및 CSV 저장, 웹 대시보드 구현, 예산 추천/브랜드 비교/잭팟 게임 |
| github:<br>[Engineer-kim](https://github.com/Engineer-kim) | github:<br>[siyeon04](https://github.com/siyeon04) | github:<br>[seoyeon020](https://github.com/seoyeon020) | github:<br>[Hyeonseok93](https://github.com/Hyeonseok93) | github:<br>[owhat02](https://github.com/owhat02) | github:<br>[hongjiho5148](https://github.com/hongjiho5148) |

## 서비스 개요

편의점 행사 정보는 브랜드별로 제공 방식과 페이지 구조가 다릅니다. 이 프로젝트는 각 브랜드별 수집기를 분리해 데이터를 가져온 뒤, `brand`, `name`, `price`, `event`, `img_url`, `category` 형태의 공통 데이터로 정리합니다.

정제된 데이터는 Streamlit 대시보드에서 다음과 같은 방식으로 활용됩니다.

- 전체 행사 상품 검색 및 필터링
- 브랜드별 행사 규모와 가격 분포 비교
- 할인 효율이 높은 상품 랭킹
- 사용자의 예산에 맞는 상품 조합 추천
- 다이어트, 야식, 랜덤 추천 등 상황별 상품 탐색
- 전국 편의점 위치 지도
- 행사/이벤트 관련 뉴스 확인
- 챗봇 기반 상품 추천 보조

## 주요 기능

| 메뉴 | 설명 |
| --- | --- |
| 메인보드 | 추천 상품, 시간대별 상품, 빠른 메뉴, 최신 뉴스 제공 |
| 전체 요약 | 행사 상품 목록 검색, 브랜드/행사/카테고리 필터링 |
| 브랜드별 비교 | CU, GS25, 7-Eleven, emart24 행사 규모 및 통계 비교 |
| 가성비 TOP 50 | 행사 유형을 반영한 개당 가격 기준 상품 랭킹 |
| 예산 맞춤 조합 | 사용자가 입력한 예산 안에서 구매 가능한 상품 조합 추천 |
| 다이어트 가이드 | 식사류, 음료 등 카테고리를 활용한 목적별 상품 추천 |
| 야식 & 안주 가이드 | 야식과 안주에 적합한 행사 상품 탐색 |
| 편의점 지도 | 브랜드별 전국 편의점 위치 확인 |
| 랜덤 픽커 | 상품 선택이 어려울 때 랜덤 추천 제공 |
| 잭팟 게임 | 상품 데이터를 활용한 간단한 슬롯형 게임 |
| 행사 뉴스 | 편의점 브랜드 행사 및 이벤트 관련 뉴스 제공 |

## 기술 스택

| 영역 | 기술 |
| --- | --- |
| 애플리케이션 | Python, Streamlit |
| 데이터 처리 | Pandas |
| 크롤링 | Requests, BeautifulSoup4, Selenium, webdriver-manager |
| 시각화 | Plotly, Folium, streamlit-folium |
| 배치 | APScheduler, pytz, loguru |
| AI 보조 | Groq API, python-dotenv |
| 협업 | Git, GitHub |

## 프로젝트 구조

```text
python_conv_project/
├── app.py                         # Streamlit 앱 진입점 및 페이지 네비게이션
├── style.css                      # 공통 UI 스타일
├── requirements.txt               # Python 의존성 목록
├── assets/                        # 로고, 그래프 등 정적 이미지
├── batch/                         # 정기 데이터 수집 배치
│   ├── batch_scheduler_manager.py # APScheduler 기반 스케줄러 관리
│   ├── Batach_README.md           # 배치 실행 가이드
│   └── script/
│       └── crawl_batch_script.py  # 브랜드별 수집, 정제, 분류 실행 스크립트
├── data/                          # 원본/정제/분류 CSV 데이터
│   ├── CU_260224.csv
│   ├── GS25_260224.csv
│   ├── 7Eleven_260224.csv
│   ├── emart24_260224.csv
│   ├── cleaned_data.csv
│   ├── categorized_data.csv
│   ├── filtered_convenience_stores.csv
│   └── official_event_news.csv
├── pages/                         # Streamlit 페이지
│   ├── 00_home.py
│   ├── 01_overall_summary.py
│   ├── 02_brand_comparison.py
│   ├── 03_best_value.py
│   ├── 04_budget_combination.py
│   ├── 05_diet_guide.py
│   ├── 06_night_snack_guide.py
│   ├── 07_convenience_store_map.py
│   ├── 08_random_picker.py
│   ├── 09_jackpot_game.py
│   └── 10_event_news.py
├── scraper/                       # 브랜드별 행사 상품 수집기
│   ├── cu_scraper.py
│   ├── gs25_scraper.py
│   ├── seven_eleven_scraper.py
│   ├── emart24_scraper.py
│   └── event_news_scraper.py
├── utils/                         # 데이터 정제, 분류, 챗봇, 장바구니, 시각화 유틸
└── test/                          # 배치 및 스케줄러 테스트
```

## 데이터 파이프라인

```text
브랜드별 행사 페이지
  -> scraper/ 브랜드별 수집기
  -> data/ 브랜드별 원본 CSV
  -> utils/data_cleaner.py 또는 data_cleaner_batch.py
  -> data/cleaned_data.csv
  -> utils/data_categorize.py
  -> data/categorized_data.csv
  -> Streamlit 대시보드, 추천 기능, 챗봇, 지도/뉴스 화면
```

핵심 설계 포인트는 수집 단계와 분석 단계를 분리한 것입니다. 브랜드마다 요청 방식, 응답 구조, 행사명 표기가 다르기 때문에 수집기는 독립적으로 관리하고, 대시보드가 사용하는 데이터는 공통 CSV로 정리합니다.

## 실행 방법

### 1. 가상환경 준비

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. Streamlit 실행

```bash
streamlit run app.py
```

### 4. 데이터 수동 갱신

필요할 때 브랜드별 수집기와 정제 스크립트를 직접 실행할 수 있습니다.

```bash
python scraper/cu_scraper.py
python scraper/gs25_scraper.py
python scraper/seven_eleven_scraper.py
python scraper/emart24_scraper.py
python utils/data_cleaner.py
python utils/data_categorize.py
```

배치 흐름 전체를 확인하려면 아래 파일을 참고하세요.

```bash
python batch/script/crawl_batch_script.py
```

## Git 협업 정보

현재 저장소는 GitHub 원격 저장소와 연결되어 있습니다.

```text
origin: https://github.com/hongjiho5148/python_conv_project.git
branch: main
```

기본 협업 흐름은 다음과 같이 가져갈 수 있습니다.

```bash
git pull origin main
git checkout -b feature/작업-이름
git add .
git commit -m "feat: 작업 내용 요약"
git push origin feature/작업-이름
```

README의 팀원 GitHub 링크는 계정 페이지로 연결해 두었습니다. GitHub의 Contributors 영역에 정확히 연결되게 하려면 각 팀원이 본인 GitHub 계정 이메일 또는 noreply 이메일로 커밋하도록 설정해야 합니다.

## 트러블슈팅 및 개선점

### 1. 브랜드별 데이터 구조 차이

브랜드마다 행사 상품 페이지의 요청 방식과 응답 형식이 달라 하나의 크롤러로 통합하기 어렵습니다.

해결 방식:

- 브랜드별 수집기를 분리했습니다.
- 수집 결과는 공통 컬럼으로 맞췄습니다.
- 이후 대시보드와 추천 기능은 `categorized_data.csv`만 바라보도록 구성했습니다.

### 2. Streamlit 재실행과 배치 중복 등록

Streamlit은 사용자 상호작용마다 스크립트를 다시 실행할 수 있어 스케줄러 작업이 중복 등록될 가능성이 있습니다.

해결 방식:

- `batch_scheduler_manager.py`에서 스케줄러 관리 책임을 분리했습니다.
- job id를 기준으로 중복 등록을 방지하는 구조를 사용했습니다.
- 배치 로그와 실행 스크립트 로그를 분리해 문제 지점을 추적할 수 있게 했습니다.

### 3. 데이터 정제 품질

크롤링 데이터에는 가격 표기 차이, 결측값, 중복 상품, 행사명 표기 차이가 포함될 수 있습니다.

해결 방식:

- 가격 문자열에서 숫자만 추출해 정수형으로 변환합니다.
- 필수 컬럼이 비어 있는 데이터는 제거합니다.
- 중복 상품을 제거하고 행사 유형을 표준화합니다.
- 상품명 기반 카테고리 분류를 추가해 추천/필터 기능에서 활용합니다.

### 4. 앞으로 보완하면 좋은 점

- 팀원별 실제 담당 영역과 프로젝트 기간 추가
- 주요 화면 스크린샷 추가
- `.env.example` 파일 제공
- 데이터 정제 로직 단위 테스트 확대
- 배치 실행 결과 리포트 자동 생성
- 브랜드별 크롤링 실패 시 알림 기능 추가
- GitHub Actions를 활용한 테스트 자동화

---

2026 Convenience Store Event Dashboard Project.
