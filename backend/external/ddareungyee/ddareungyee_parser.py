from ddareungyee_api import fetch_ddareungyee_stock

# 1. 실시간 대여 가능 자전거 수 (관리 권역 선별X)
def parse_stock(start, end):
    response = fetch_ddareungyee_stock(start, end)
    items = response['rentBikeStatus']['row']

    stock_dict = {}
    for item in items:
        stationId = item['stationId']
        stock = item['parkingBikeTotCnt']
        stock_dict[stationId] = stock

    return stock_dict


if __name__ == '__main__':
    start = 1001
    end = 3000
    cnt = 1

    for i in range(start, end, 500): #500은 청크 단위
        stock_dict = parse_stock(i, i+499)
        for key, value in stock_dict.items():
            print(f"{cnt} - {key}: {value}")
            cnt += 1