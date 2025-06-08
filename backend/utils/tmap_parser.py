def parse_route_summary(response: dict) -> dict:
    """
    전체 경로 요약 정보 추출 (총 거리, 총 시간, 총 요금 등)
    """
    props = response.get("properties", {})
    return {
        "totalDistance": props.get("totalDistance"),
        "totalTime": props.get("totalTime"),
        "totalFare": props.get("totalFare")
    }


def parse_via_points(response: dict) -> list[dict]:
    """
    각 경유지 도착 정보 추출
    """
    features = response.get("features", [])
    parsed_points = []

    for feature in features:
        props = feature.get("properties", {})
        parsed = {
            "index": props.get("index"),
            "viaPointId": props.get("viaPointId"),
            "viaPointName": props.get("viaPointName"),
            "arriveTime": props.get("arriveTime"),
            "completeTime": props.get("completeTime"),
            "distance": props.get("distance"),
            "deliveryTime": props.get("deliveryTime"),
            "waitTime": props.get("waitTime"),
            "pointType": props.get("pointType")
        }
        parsed_points.append(parsed)

    return parsed_points
