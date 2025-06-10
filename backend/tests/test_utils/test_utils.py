# parser 테스트

from backend.external.tmap.tmap_request import *
from backend.external.tmap.tmap_client import send_tmap_request
# from backend.external.tmap.tmap_parser import *


if __name__ == "__main__":
    # 1. 출발 시간 계산
    start_time = load_startTime()

    # 2. 경유지 정보 구성
    via_points = build_viaPoints(move_info)

    # 3. payload 구성
    payload = build_payload(start_time, via_points)

    # 4. API 요청 및 응답
    response = send_tmap_request(payload)

    # 5. 응답 파싱
    # summary = parse_route_summary(response)
    # via_points_info = parse_via_points(response)

    print(response)