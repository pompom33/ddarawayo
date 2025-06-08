"""
Tmap API에 POST 요청을 보내고 응답 JSON을 반환
"""

import requests
from backend.utils.tmap_config import TMAP_API_KEY, TMAP_REQUEST_URL
from backend.utils.tmap_request import build_payload

def build_headers():
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "appKey": TMAP_API_KEY
    }
    return headers


def send_tmap_request(payload: dict) -> dict:
    headers = build_headers()

    request = requests.post(TMAP_REQUEST_URL, json=payload, headers=headers)

    if not request.ok:
        raise Exception(f"Tmap API 요청 실패: {request.status_code} - {request.text}")

    return request.json()


# 테스트 코드
if __name__ == "__main__":
    # 예시 경유지
    via_points = [
        {
            "viaPointId": "001",
            "viaPointName": "테스트장소",
            "viaX": "126.95042955033101",
            "viaY": "37.39952907832974",
            "viaDetailAddress": "서울시 강남구",
            "viaTime": 900,
            "wishStartTime": "202506041300",
            "wishEndTime": "202506041500"
        }
    ]

    start_time = "202506041200"
    payload = build_payload(start_time, via_points)

    result = send_tmap_request(payload)
    print(result)
