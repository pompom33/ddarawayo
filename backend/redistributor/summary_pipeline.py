"""
대여소별로 재고량(stock)과 예상 수요값(prediction), 상태(abundant)를 구하는 파이프라인입니다.
'center'(출발센터) 데이터로 입력합니다.
"""

import math
from backend.models.demand_predictor import run_demand_predictor_pipeline
from backend.external.ddareungyee.ddareungyee_parser import parse_and_save_stock

# 1. 대여소별로 재고량(stock)과 예상 수요값(prediction) 불러오기
def get_demand_stock(zone: int, start: int, end: int) -> dict[str, dict[str, int]]:
    # 1. 수요 예측값 불러오기 (해당 관리 권역만)
    predictions_dict = run_demand_predictor_pipeline(zone)

    # 2. stock 불러오기 (따릉이 API -> 모든 대여소 stock)
    stock_dict = parse_and_save_stock(start, end)

    # 3. “stationId” : {“prediction”: 00 , “stock”: 00}
    station_summary = {}

    for stationId, predictions in predictions_dict.items():
        if stationId in stock_dict.keys():
            station_summary[stationId] = {
                'prediction': math.ceil(predictions_dict[stationId]),
                'stock': stock_dict[stationId]
            }

    return station_summary


# 2. 대여소별 상태 라벨링하기(abundant: 1, deficient: 0)
def station_status_labeler(station_summary: dict) -> dict:
    for stationId, summary in station_summary.items():
        stock = summary["stock"]
        prediction = summary["prediction"]

        # 예측 수요량보다 최소 3개 이상 여유 있어야 충분(abundant)하다고 판단
        status = stock - (prediction + 3)

        if status > 0:
            summary["abundant"] = 1
        else:
            summary["abundant"] = 0

    return station_summary


# 3. center 정보 추가
def add_center(station_summary):
    station_summary["center"] = {
            "prediction": 0,
            "stock": 0,
            "abundant": 1
        }

    return station_summary

def generate_station_summary(zone: int, start: int, end: int) -> dict:
    station_summary = get_demand_stock(zone, start, end)
    station_summary = station_status_labeler(station_summary)
    station_summary = add_center(station_summary)
    return station_summary


if __name__ == '__main__':
    zone = 1
    start = 1001
    end = 3000

    station_summary = generate_station_summary(zone, start, end)
    for key, value in station_summary.items():
        print(key, value)