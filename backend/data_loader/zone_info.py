import os
import csv
from typing import Dict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, '..', 'files')

# 1. zone별 대여소ID 불러오기
def load_zone_id(zone: str) -> list[str]:
    zone_file = f'{zone}_station_id_list.txt'
    zone_id_path = os.path.join(FILES_DIR, zone_file)

    zone_id_list = []
    with open(zone_id_path, 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            zone_id_list.append(line.strip())
    return zone_id_list


# 2. zone별 대여소 이름 및 위도 경도 데이터 불러오기
def load_LatLonName(zone_id_list) -> Dict[str, Dict[str, str]]:
    station_LatLonName_file = 'station_name_latlon.csv'
    station_LatLonName_path = os.path.join(FILES_DIR, station_LatLonName_file)

    station_LatLonName_dict = {}
    with open(station_LatLonName_path, 'r', encoding='utf-8-sig') as fr:
        reader = csv.DictReader(fr)

        for row in reader:
            stationID = row['Station_ID']
            if stationID in zone_id_list: # 해당 zone만 선별
                station_LatLonName_dict[stationID] = {
                    "Latitude": row['Latitude'],
                    "Longitude": row['Longitude'],
                    "Station_name": row['Station_name'].strip()
                }

        return station_LatLonName_dict


# 3. zone별 대여소 주변 시설 정보
def load_facility_data(zone_id_list) -> list:
    facility_file = 'station_facilities.csv'
    facility_path = os.path.join(FILES_DIR, facility_file)

    facility_list = []
    with open(facility_path, 'r') as fr:
        reader = csv.reader(fr)
        next(reader)
        for row in reader:
            stationID = row[0]
            if stationID in zone_id_list:  # 해당 zone만 선별
                facility_list.append(tuple(row))
    return facility_list


if __name__ == '__main__':
    zone = 'zone1'
    zone_id_list = load_zone_id(zone)
    station_LatLonName_dict = load_LatLonName(zone_id_list)
    facility_list = load_facility_data(zone_id_list)
    print(len(facility_list))
    print('\n', facility_list)