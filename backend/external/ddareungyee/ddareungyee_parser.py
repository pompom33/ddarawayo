"""
따릉이 API로부터 실시간 대여소별 재고량을 불러오는 모듈입니다.
"""

from backend.external.ddareungyee.ddareungyee_api import fetch_ddareungyee_stock

# 1. 실시간 대여 가능 자전거 수 (관리 권역 선별X)
def parse_and_save_stock(start, end):
    stock_dict = {}

    for i in range(start, end, 500):  # 500은 청크 단위
        response = fetch_ddareungyee_stock(start=i, end=i+499)
        items = response['rentBikeStatus']['row']

        for item in items:
            stationId = item['stationId']
            stock = item['parkingBikeTotCnt']
            stock_dict[stationId] = stock

    return stock_dict


if __name__ == '__main__':
    start = 1001
    end = 3000
    stock_dict = parse_and_save_stock(start, end)
    for key, value in stock_dict.items():
        print(key, value)

