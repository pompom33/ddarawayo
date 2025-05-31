import lightgbm as lgb
import numpy as np
import csv
import os
from datetime import datetime, timedelta
import pytz

BASE_DIR = os.path.dirname(__file__)
FACILITY_PATH = os.path.join(BASE_DIR, '..', 'files', 'station_facilities.csv')
MODEL_PATH = os.path.join(BASE_DIR, '..', 'files', 'LGBMmodel.txt')

def load_facility_data():
    facility_list = []
    with open(FACILITY_PATH, 'r') as fr:
        reader = csv.reader(fr)
        next(reader)
        for row in reader:
            facility_list.append(tuple(row))
    return facility_list

def load_time_data(month, day, hour):
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

def combine_facility_with_time(facility_list, month, hour, weekday):
    combined_list = []
    for row in facility_list:
        extended_row = list(row) + [month, hour, weekday]
        combined_list.append(extended_row)
    combined_array = np.array(combined_list, dtype=float)
    return combined_array

def predict_demand_booster(booster, X, facility_list):
    predictions = booster.predict(X)
    result = []
    for i, row in enumerate(facility_list):
        result.append({
            'Rental_Location_ID': row[0],
            'predicted_demand': predictions[i]
        })
    return result

def run_full_demand_prediction(month, day, hour):
    booster = lgb.Booster(model_file=MODEL_PATH)
    facility_list = load_facility_data()
    m, h, w = load_time_data(month, day, hour)
    X = combine_facility_with_time(facility_list, m, h, w)
    predictions = predict_demand_booster(booster, X, facility_list)
    return predictions
