import pytest
import pandas as pd
from backend.models  import demand_predictor

def test_load_model():
    model = demand_predictor.load_model()
    assert model is not None

def test_load_facility_data():
    facility_data = demand_predictor.load_facility_data()
    assert len(facility_data) > 0
    assert isinstance(facility_data[0], tuple)

def test_calculate_weekday():
    month, hour, weekday = demand_predictor.calculate_weekday(5, 29, 14)
    assert month == 5
    assert hour == 14
    assert weekday in [0, 1]

def test_prepare_input_dataframe():
    facility_data = demand_predictor.load_facility_data()
    month, hour, weekday = demand_predictor.calculate_weekday(5, 29, 14)
    df = demand_predictor.prepare_input_dataframe(facility_data, month, hour, weekday)

    assert isinstance(df, pd.DataFrame)
    expected_columns = [
        'Rental_Location_ID', 'bus_stop', 'park', 'school', 'subway',
        'riverside', 'month', 'hour', 'weekday'
    ]
    for col in expected_columns:
        assert col in df.columns

def test_predict_demand():
    model = demand_predictor.load_model()
    facility_data = demand_predictor.load_facility_data()
    month, hour, weekday = demand_predictor.calculate_weekday(5, 29, 14)
    input_df = demand_predictor.prepare_input_dataframe(facility_data, month, hour, weekday)
    predictions_df = demand_predictor.predict_demand(model, input_df)
    assert 'predicted_demand' in predictions_df.columns

# def test_run_demand_prediction_pipeline():