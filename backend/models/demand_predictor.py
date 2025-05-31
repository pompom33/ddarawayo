import os
import pickle
import csv
from datetime import datetime, timedelta
import pytz
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = './LGBMmodel.pkl'
FACILITY_PATH = './station_facilities.csv'

# 1. LGBM모델 불러오기
def load_model(model_path=MODEL_PATH):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# 2. 주변 시설 정보 불러오기 (캐싱용)
def load_facility_data():
    facility_list = []
    facility_path = os.path.join(BASE_DIR, FACILITY_PATH)
    with open(facility_path, 'r') as fr:
        reader = csv.reader(fr)
        next(reader)
        for row in reader:
            facility_list.append(tuple(row))
    return facility_list

# 3. 주중/주말 여부 계산
def calculate_weekday(month, day, hour):
    kst = pytz.timezone('Asia/Seoul')
    now_kst = datetime.now(kst)
    one_hour_later = now_kst + timedelta(hours=1)
    year = one_hour_later.year
    date = datetime(year, month, day, hour) + timedelta(hours=1)
    if date.weekday() < 5:
        weekday = 1
    else:
        weekday = 0
    return month, hour, weekday

# 4. 입력 데이터프레임 생성
def prepare_input_dataframe(facility_list, month, hour, weekday):
    columns = ['Rental_Location_ID', 'bus_stop', 'park', 'school', 'subway', 'riverside']
    df = pd.DataFrame(facility_list, columns=columns)

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

# 5. 수요 예측
def predict_demand(model, input_df):
    feature_cols = [
        'Rental_Location_ID', 'bus_stop', 'park', 'school', 'subway', 'riverside', 'month', 'hour', 'weekday'
    ]
    X = input_df[feature_cols]
    predictions = model.predict(X)

    predictions_df = input_df[['Rental_Location_ID']].copy()
    predictions_df['predicted_demand'] = predictions

    return predictions_df

# 6. 전체 파이프라인 실행
def run_demand_prediction_pipeline(model, facility_list, month, day, hour):
    weekday = calculate_weekday(month, day, hour)
    input_df = prepare_input_dataframe(facility_list, month, hour, weekday)
    pred_fin_df = predict_demand(model, input_df)
    return pred_fin_df