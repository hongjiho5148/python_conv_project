# Emart24 Event Scraper

이마트24의 행사 상품(1+1, 2+1, 3+1, SALE) 정보를 자동으로 수집하여 CSV로 저장하는 스크래퍼입니다.

## 구성 파일
- `emart24_scraper.py`: 스크래핑 로직 핵심
- `requirements.txt`: 필요한 라이브러리 목록 (버전 명시)
- `.gitignore`: 불필요한 파일 제외 설정

## 설치 및 실행
1. **필수 라이브러리 설치**
   ```bash
   pip install -r requirements.txt
   ```
2. **실행**
   ```bash
   python emart24_scraper.py
   ```

## 결과물
- `emart24_YYMMDD.csv` 형식으로 당일 날짜의 수집 데이터가 저장됩니다.
