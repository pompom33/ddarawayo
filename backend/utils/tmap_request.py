from datetime import datetime
import requests

from backend.models import model_input
from tmap_config import TMAP_API_KEY, TMAP_REQUEST_URL


def load_startTime():
    start_dt = model_input.load_timedelta()
    dt = datetime.strptime(f"{start_dt}", '%Y-%m-%d %H:%M:%S.%f%z')
    start_time = dt.strftime('%Y%m%d%H')
    return start_time

def build_payload(start_time, via_points):
    payload = {
        "reqCoordType": "WGS84GEO",
        "resCoordType": "WGS84GEO",
        "startName": "%EC%B6%9C%EB%B0%9C%EC%84%BC%ED%84%B0", # 출발센터
        "startX": "127.0717955",
        "startY": "37.4957886",
        "startTime": start_time,
        "endName": "%EB%8F%84%EC%B0%A9%EC%84%BC%ED%84%B0", #도착센터
        "endX": "127.0717955",
        "endY": "37.4957886",
        "searchOption": "0", # 경로 탐색 옵션: 교통최적+추천 / 누리님은 "2"로 했었음
        "carType": "4", # 대형화물차
        "truckType": "1", # 화물자동차
        "truckWidth": "250",
        "truckHeight": "340",
        "truckWeight": "35500",
        "truckTotalWeight": "26000",
        "truckLength": "880",
        "viaPoints": via_points
    }
    return payload

def mock_move_info():
    move_info = [1, 2, 3]
    return move_info


def build_viaPoints(move_info):
    via_points = []
    for i in range(len(move_info)):
        via_point = {} # 초기화

        via_point["viaPointId"] = viaPointId
        via_point["viaPointName"] = viaPointName
        via_point["viaX"] = viaX
        via_point["viaY"] = viaY
        via_point["viaDetailAddress"] = viaDetailAddress
        via_point["viaTime"] = viaTime
        via_point["wishStartTime"] = wishStartTime
        via_point["wishEndTime"] = wishEndTime

        via_points.append(via_point)
    return via_points


def build_headers():
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "appKey": TMAP_API_KEY
    }
    return headers


if __name__ == "__main__":
    # 테스트용 데이터
    viaPointId= "test01"
    viaPointName= "name01"
    viaX= "126.95042955033101"
    viaY= "37.39952907832974"
    viaDetailAddress= "2001동, 1001호"
    viaTime= 600
    wishStartTime= "201606301700"
    wishEndTime= "201606301900"

    start_time = load_startTime()
    move_info = mock_move_info()
    via_points = build_viaPoints(move_info)
    payload = build_payload(start_time, via_points)
    headers = build_headers()

    print("\n----viapoints----")
    print(via_points)