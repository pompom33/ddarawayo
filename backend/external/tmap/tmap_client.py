"""
Tmap API에 POST 요청을 보내고 응답 JSON을 반환
"""

import requests
from .tmap_config import TMAP_API_KEY, TMAP_REQUEST_URL

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
