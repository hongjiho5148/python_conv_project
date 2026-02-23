import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from datetime import datetime

class Emart24Scraper:
    def __init__(self):
        self.brand = "emart24"
        self.base_url = "https://emart24.co.kr/goods/event"
        self.categories = {1: '1+1', 2: '2+1', 3: '3+1', 4: 'SALE'}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def run(self):
        start_ts = datetime.now()
        print(f"[{start_ts.strftime('%Y-%m-%d %H:%M:%S')}] {self.brand} 수집 시작 (이미지 다운로드 제외)")
        
        data_list = []

        for seq, label in self.categories.items():
            page = 1
            print(f"\n--- 카테고리: {label} ---")
            
            while True:
                params = {'page': page, 'category_seq': seq}
                try:
                    res = requests.get(self.base_url, headers=self.headers, params=params, timeout=10)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    items = soup.find_all('div', class_='itemWrap')
                except Exception as e:
                    print(f" [ERROR] {page}페이지 호출 실패: {e}")
                    break

                if not items:
                    break

                for item in items:
                    try:
                        name = item.select_one('.itemtitle p a').text.strip()
                        price = item.select_one('.price').text.strip()
                        # 행사 정보 태그가 있으면 사용, 없으면 기본 라벨 사용
                        event = item.select_one('.itemTit span.floatR').text.strip() if item.select_one('.itemTit span.floatR') else label
                        
                        # 이미지 URL 추출 및 절대 경로 보정
                        img_raw = item.select_one('.itemSpImg img')['src']
                        img_url = img_raw if img_raw.startswith('http') else f"https://emart24.co.kr{img_raw}"

                        # 데이터 저장
                        data_list.append({
                            'brand': self.brand,
                            'name': name,
                            'price': price,
                            'event': event,
                            'img_url': img_url
                        })
                        
                        # 개별 상품 실시간 로그 출력
                        current_time = datetime.now().strftime('%H:%M:%S')
                        print(f"[{current_time}] [{label}] {name} - {price}")

                    except Exception:
                        continue

                page += 1
                # 서버 부하 방지를 위한 랜덤 지연
                time.sleep(random.uniform(0.3, 0.5))
            
            print(f"> {label} 수집 완료!")

        # 데이터 저장 로직 호출
        self._save_to_csv(data_list, start_ts)

    def _save_to_csv(self, data_list, start_ts):
        if not data_list:
            print("수집된 데이터가 없습니다.")
            return

        df = pd.DataFrame(data_list)
        raw_count = len(df)
        df.drop_duplicates(subset=['name', 'event'], keep='first', inplace=True)
        
        # 파일명 형식: emart24_260223.csv
        filename = f"{self.brand}_{datetime.now().strftime('%y%m%d')}.csv"
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        
        duration = datetime.now() - start_ts
        print("\n" + "="*50)
        print(f"최종 결과 요약:")
        print(f" - 전체 수집 개수: {raw_count}")
        print(f" - 중복 제거 후  : {len(df)}")
        print(f" - 저장 파일명   : {filename}")
        print(f" - 소요 시간     : {duration.seconds // 60}분 {duration.seconds % 60}초")
        print("="*50)

# --- 바로 실행 가능하도록 추가된 코드 ---
if __name__ == "__main__":
    scraper = Emart24Scraper()
    scraper.run()