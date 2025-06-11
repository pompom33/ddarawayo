from backend.data_loader import zone_info
from backend.external.ddareungyee.ddareungyee_api import fetch_ddareungyee_stock

# 모든 stationID 목록 만들기
def get_total_id_list():
    total_ids = []
    for zone in range(1, 3):  # 추후 zone 수 자동화 가능
        total_ids += zone_info.load_zone_id(zone)
    return set(total_ids)


# 관리권역 station들이 따릉이 API 내 어떤 청크에 있는지 확인
# 2025년 6월 11일 기준 <1001 ~ 3000> 내에 총 31개 대여소 존재 확인
def check_api_index(target_id_set):
    api_index_set = set()
    for i in range(1, 4001, 500):  # 나중에 max index 자동화 가능
        response = fetch_ddareungyee_stock(i, i + 499)
        items = response['rentBikeStatus']['row']

        matched = []
        for item in items:
            station_id = item['stationId']
            if station_id in target_id_set:
                matched.append(station_id)

        if matched:
            print(f"Found in chunk {i}~{i+499}: {matched} (총 {len(matched)}개)")
            api_index_set.add((i, i + 499))
    return api_index_set


if __name__ == '__main__':
    target_id_set = get_total_id_list()
    api_index_set = check_api_index(target_id_set)
    print(f"api_index_set: {api_index_set}")
    print(len(api_index_set))