"""
1. 요청 payload를 구성하고
2. API에 요청을 보내고
3. 응답을 파싱해
4. 필요한 형태로 리턴하는 파이프라인 역할입니다.
"""

from backend.utils.tmap_request import *
from backend.utils.tmap_client import send_tmap_request
from backend.utils.tmap_parser import parse_route_summary, parse_via_points

def get_route_result(move_info: list[dict]) -> dict:
    # 1. 출발 시간 계산
    start_time = load_startTime()

    # 2. 경유지 정보 구성
    via_points = build_viaPoints(move_info)

    # 3. payload 구성
    payload = build_payload(start_time, via_points)

    # 4. API 요청 및 응답
    response = send_tmap_request(payload)

    # 5. 응답 파싱
    summary = parse_route_summary(response)
    via_points_info = parse_via_points(response)

    # 6. 결과 반환
    return {
        "summary": summary,
        "viaPoints": via_points_info
    }

if __name__ == '__main__':
    move_info = mock_move_info()
    result = get_route_result(move_info)
    print(result)
