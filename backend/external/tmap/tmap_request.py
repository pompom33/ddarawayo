"""
경유지 정보 리스트를 Tmap API에서 요구하는 형식으로 변환 (요청 파라미터 조립)
"""

from datetime import datetime
from backend.data_loader import time_loader

def load_startTime()-> str:
    start_dt = time_loader.load_timedelta() # 예측하려는 시간(현재+1시간)
    dt = datetime.strptime(f"{start_dt}", '%Y-%m-%d %H:%M:%S.%f%z')
    start_time = dt.strftime('%Y%m%d%H%M')
    return start_time


# 실제 move_info에 따라 차후 수정되어야 함
def mock_move_info():
    move_info = [
        {
            "viaPointId": "001",
            "viaPointName": "장소 A",
            "viaX": "126.95",
            "viaY": "37.39",
            "viaDetailAddress": "서울 강남구",
            "viaTime": 600,
            "wishStartTime": "202506041400",
            "wishEndTime": "202506041600"
        },
        {
            "viaPointId": "002",
            "viaPointName": "장소 B",
            "viaX": "126.96",
            "viaY": "37.40",
            "viaDetailAddress": "서울 서초구",
            "viaTime": 900,
            "wishStartTime": "202506041700",
            "wishEndTime": "202506041900"
        }
    ]
    return move_info


def build_viaPoints(move_info: list[dict]) -> list:
    via_points = []
    for info in move_info:
        via_point = {
            "viaPointId":        info["viaPointId"],
            "viaPointName":      info["viaPointName"],
            "viaX":              info["viaX"],
            "viaY":              info["viaY"],
            "viaDetailAddress":  info["viaDetailAddress"],
            "viaPoiId":          info.get("viaPoiId", ""),
            "viaTime":           info["viaTime"],
            "wishStartTime":     info["wishStartTime"],
            "wishEndTime":       info["wishEndTime"]
        }
        via_points.append(via_point)
    return via_points


def build_payload(start_time: str, via_points: list) -> dict:
    payload = {
        "reqCoordType": "WGS84GEO",
        "resCoordType": "WGS84GEO",
        "startName": "%EC%B6%9C%EB%B0%9C%EC%84%BC%ED%84%B0", # 출발센터
        "startX": "127.0717955", # 출발센터(경도)
        "startY": "37.4957886", # 출발센터(위도)
        "startTime": start_time,
        "endName": "%EB%8F%84%EC%B0%A9%EC%84%BC%ED%84%B0", #도착센터
        "endX": "127.0717955", # 도착센터(경도)
        "endY": "37.4957886", # 도착센터(위도)
        "searchOption": "0", # 경로 탐색 옵션: 교통최적+추천(0) / 누리님은 "2"로 했었음
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


if __name__ == "__main__":
    start_time = load_startTime()
    move_info = mock_move_info()
    via_points = build_viaPoints(move_info)
    payload = build_payload(start_time, via_points)

    print("\n----viapoints----")
    for item in via_points:
        for key, value in item.items():
            print(f"{key}: {value}")
        print()