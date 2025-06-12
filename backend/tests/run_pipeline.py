from backend.models.demand_predictor import run_demand_predictor_pipeline
from backend.external.ddareungyee.ddareungyee_parser import parse_and_save_stock

def run_pipeline_testing(zone):
    # 1. 수요 예측값 불러오기 (해당 관리 권역만)
    predictions_dict = run_demand_predictor_pipeline(zone)

    # 2. stock 불러오기 (따릉이 API -> 모든 대여소 stock)
    stock_dict = parse_and_save_stock(start, end)

    # 3. “stationId” : {“prediction”: 00 , “stock”: 00}
    station_summary = {}

    for stationId, predictions in predictions_dict.items():
        if stationId in stock_dict.keys():
            item = {}
            item['prediction'] = predictions_dict[stationId]
            item['stock'] = stock_dict[stationId]

            station_summary[stationId] = item

    return station_summary


if __name__ == '__main__':
    zone = 1
    start = 1001
    end = 3000

    station_summary = run_pipeline_testing(zone)

    for key, value in station_summary.items():
        print(key, value)