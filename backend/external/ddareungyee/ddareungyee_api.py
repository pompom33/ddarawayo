import os
import requests
from dotenv import load_dotenv

load_dotenv()

DDAREUNGYEE_API_KEY = os.getenv("DDAREUNGYEE_API_KEY")
DDAREUNGYEE_REQUEST_BASE_URL = os.getenv("DDAREUNGYEE_REQUEST_BASE_URL")

def fetch_ddareungyee_stock(start, end):
    start_index = start
    end_index = end
    url = f"{DDAREUNGYEE_REQUEST_BASE_URL}/{DDAREUNGYEE_API_KEY}/json/bikeList/{start_index}/{end_index}/"

    if not DDAREUNGYEE_API_KEY or not DDAREUNGYEE_REQUEST_BASE_URL:
        raise ValueError("따릉이 API 환경변수 누락!")

    response = requests.get(url)

    if not response.ok:
        raise Exception(f"API 요청 실패: {response.status_code} - {response.text}")

    return response.json()

if __name__ == "__main__":
    start = 1
    end = 5
    result = fetch_ddareungyee_stock(start, end)

    rows = result['rentBikeStatus']['row']
    for row in rows:
        for key, value in row.items():
            print(f"{key}: {value}")
        print()
