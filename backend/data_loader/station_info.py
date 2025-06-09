import csv

# 1. 대여소 주변 시설 정보
def load_facility_data(facility_path):
    facility_list = []
    with open(facility_path, 'r') as fr:
        reader = csv.reader(fr)
        next(reader)
        for row in reader:
            facility_list.append(tuple(row))
    return facility_list