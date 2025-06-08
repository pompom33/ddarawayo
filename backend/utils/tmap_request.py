"""
경유지 정보 리스트를 Tmap API에서 요구하는 형식으로 변환 (요청 파라미터 조립)
"""

from datetime import datetime

from backend.models import model_input

def load_startTime():
    start_dt = model_input.load_timedelta() # 예측하려는 시간(현재+1시간)
    dt = datetime.strptime(f"{start_dt}", '%Y-%m-%d %H:%M:%S.%f%z')
    start_time = dt.strftime('%Y%m%d%H')
    return start_time


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
        via_point["viaTime"] = viaTime # 단위(초)
        via_point["wishStartTime"] = wishStartTime
        via_point["wishEndTime"] = wishEndTime

        via_points.append(via_point)
    return via_points


def build_payload(start_time, via_points):
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
    # 테스트용 데이터
    viaPointId= "test01"
    viaPointName= "name01"
    viaX= "126.95042955033101"
    viaY= "37.39952907832974"
    viaDetailAddress= "2001동, 1001호"
    viaTime= 900 # 단위(초)
    wishStartTime= "201606301700"
    wishEndTime= "201606301900"

    start_time = load_startTime()
    move_info = mock_move_info()
    via_points = build_viaPoints(move_info)
    payload = build_payload(start_time, via_points)

    print("\n----viapoints----")
    for item in via_points:
        for key, value in item.items():
            print(f"{key}: {value}")
        print()