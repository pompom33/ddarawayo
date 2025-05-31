import pytest
import lightgbm as lgb
import numpy as np
from backend.models import model_input

def test_load_facility_data():
    facility_list = demand_predictor.load_facility_data()
    assert len(facility_list) > 0
    assert isinstance(facility_list[0], tuple)

def test_load_time_data():
    month, hour, weekday = demand_predictor.load_time_data(5, 29, 14)
    assert month == 5
    assert hour == 14
    assert weekday in [0, 1]

def test_combine_facility_with_time():
    facility_list = demand_predictor.load_facility_data()
    month, hour, weekday = demand_predictor.load_time_data(5, 29, 14)
    combined_array = demand_predictor.combine_facility_with_time(facility_list, month, hour, weekday)
    assert isinstance(combined_array, np.ndarray)
    assert combined_array.shape[1] == len(facility_list[0]) + 3  # 기존 열 + m, h, w

def test_run_full_demand_prediction():
    predictions = demand_predictor.run_full_demand_prediction(5, 29, 14)
    assert isinstance(predictions, list)
    assert len(predictions) > 0
    assert 'Rental_Location_ID' in predictions[0]
    assert 'predicted_demand' in predictions[0]
