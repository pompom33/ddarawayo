from datetime import datetime
from backend.data_loader import zone_info
import requests

# sample url
url = 'http://openapi.seoul.go.kr:8088/sample/xml/CardSubwayStatsNew/1/5/20220301'

response = requests.get(url)
print(response.content)


# 1. 현재 대여 가능 자전거 수
def load_stock(zone_id_list):
    zone_id_tuple = tuple(zone_id_list)

    # user input 시간만 stock 불러옴
    input_date = datetime(2023, month, day)
    input_date = str(input_date.strftime('%Y-%m-%d'))
    input_time = int(hour)

    # Bigquery에서 해당 기간 stock 내역 불러옴
    # stock_list = []
    # query = """
    #     SELECT *
    #     FROM `multi-final-project.Final_table_NURI.2023_available_stocks_fin`
    #     WHERE Date = '{input_date}'
    #         AND Time = {input_time}
    #         AND Rental_location_ID IN {zone_id_tuple}
    # """.format(
    #     input_date=input_date,
    #     input_time=input_time,
    #     zone_id_tuple=zone_id_tuple
    # )
    # query_job = client.query(query)
    # results = query_job.result()

    for row in results:
        stock_list.append(dict(row))

    return stock_list  # 순서 X


# 2. 대여소별 충분/부족 여부
def find_station_status(merged_result): #abundant, deficient labeling 하기
    # 1. 순서대로 status 구하기
    for stationid, item in merged_result.items():
        stock = item["stock"]
        predicted_rental = item['predicted_rental']
        status = stock - (predicted_rental + 3) # 예측된 수요량보다 3개 더 많아야 함
        if status < 0:
            merged_result[stationid]["status"] = 1
        else:
            merged_result[stationid]["status"] = "abundant"

    # 2. 임의로 center 정보 추가
    merged_result["center"] = {
            "predicted_rental": 0,
            "stock": 0,
            "status": "abundant"
        }
    station_status_dict = merged_result
    session['station_status_dict'] = station_status_dict

    return station_status_dict # center 까지 포함 (필수) # 순서 X


if __name__ == '__main__':
    zone = 'zone1'
    zone_id_list = zone_info .load_zone_id(zone)