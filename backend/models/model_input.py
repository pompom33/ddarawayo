"""
수요예측 모델의 입력 데이터를 준비하는 모듈입니다
"""

import os
import csv
from datetime import datetime, timedelta
import pytz
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
FACILITY_PATH = os.path.join(BASE_DIR, '..', 'files', 'station_facilities.csv')


# 1. 주변 시설 정보 불러오기 (캐싱용)
def load_facility_data(facility_path):
    facility_list = []
    with open(facility_path, 'r') as fr:
        reader = csv.reader(fr)
        next(reader)
        for row in reader:
            facility_list.append(tuple(row))
    return facility_list


# 2. 현재 시간 구하기
def load_timedelta():
    kst = pytz.timezone('Asia/Seoul')
    now_kst = datetime.now(kst)
    one_hour_later = now_kst + timedelta(hours=1)
    return one_hour_later


# 3. 주중/주말 여부 계산
def calculate_weekday(date):
    if date.weekday() < 5:
        weekday = 1
    else:
        weekday = 0
    return weekday


# 4. 입력 데이터프레임 생성
def prepare_input_dataframe(facility_list, date):
    columns = ['Rental_Location_ID', 'bus_stop', 'park', 'school', 'subway', 'riverside']
    df = pd.DataFrame(facility_list, columns=columns)

    month = date.month
    hour = date.hour
    weekday = calculate_weekday(date)

    df['month'] = month
    df['hour'] = hour
    df['weekday'] = weekday

    numeric_cols = ['bus_stop', 'park', 'school', 'subway', 'month', 'hour']
    categorical_cols = ['Rental_Location_ID', 'riverside', 'weekday']

    for col in numeric_cols:
        df[col] = df[col].astype('int')
    for col in categorical_cols:
        df[col] = df[col].astype('category')

    return df


# 5. 전체 파이프라인 실행
def run_model_input_pipeline():
    facility_list = load_facility_data(facility_path=FACILITY_PATH)
    date = load_timedelta()
    input_df = prepare_input_dataframe(facility_list, date)
    return input_df