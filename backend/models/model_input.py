"""
수요예측 모델의 입력 데이터를 준비하는 모듈입니다
"""

import os
import datetime
import pandas as pd
from backend.data_loader import time_loader
from backend.data_loader import zone_info

BASE_DIR = os.path.dirname(__file__)

# 1. 입력 데이터프레임 생성
def prepare_input_dataframe(facility_list: list, date: datetime) -> pd.DataFrame:
    columns = ['Rental_Location_ID', 'bus_stop', 'park', 'school', 'subway', 'riverside']
    df = pd.DataFrame(facility_list, columns=columns)

    month = date.month
    hour = date.hour
    weekday = time_loader.calculate_weekday(date)

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


# 2. 전체 파이프라인 실행
def run_model_input_pipeline(zone: int) -> pd.DataFrame:
    zone_id_list = zone_info.load_zone_id(zone)
    facility_list = zone_info.load_facility_data(zone_id_list)
    date = time_loader.load_timedelta()
    input_df = prepare_input_dataframe(facility_list, date)
    return input_df


if __name__ == '__main__':
    zone = 1
    input_df = run_model_input_pipeline(zone)
    for _, row in input_df.iterrows():
        print(row)