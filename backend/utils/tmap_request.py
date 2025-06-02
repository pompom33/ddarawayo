import os
from dotenv import load_dotenv
import requests

load_dotenv() # .env 파일을 자동으로 찾아 읽어옴

TMAP_API_KEY = os.getenv("TMAP_API_KEY")
TMAP_REQUEST_URL = os.getenv("TMAP_REQUEST_URL")

# endpoint (여기로 request 보냄)
url = TMAP_REQUEST_URL

def build_payload():
    payload = {
        "reqCoordType": "WGS84GEO",
        "resCoordType": "WGS84GEO",
        "startName": "%EC%B6%9C%EB%B0%9C",
        "startX": "126.977613738705",
        "startY": "37.56523875839218",
        "startTime": "201607010900",
        "endName": "%EB%8F%84%EC%B0%A9",
        "endX": "127.12668555134137",
        "endY": "37.42007356038663",
        "searchOption": "0",
        "carType": "4",
        "truckType": "1",
        "truckWidth": "250",
        "truckHeight": "340",
        "truckWeight": "35500",
        "truckTotalWeight": "26000",
        "truckLength": "880"
        # "viaPoints": []
    }
    return payload

def build_headers():
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "appKey": TMAP_API_KEY
    }
    return headers


if __name__ == "__main__":
    payload = build_payload()
    headers = build_headers()
    print(url)
    print("repr of key:", repr(TMAP_API_KEY))
    response = requests.post(url, json=payload, headers=headers)

    print(response.text)