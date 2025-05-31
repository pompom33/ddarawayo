from backend.models import demand_predictor

def test_predict_demand():
    model = demand_predictor.load_model()
    facility_list = demand_predictor.load_facility_data()
    month, hour, weekday = demand_predictor.load_time(5, 29, 14)
    input_df = demand_predictor.prepare_input_dataframe(facility_list, month, hour, weekday)
    predictions_df = demand_predictor.predict_demand(model, input_df)

    print("\n===== 예측 결과 출력 =====")
    print(predictions_df.head(5))

if __name__ == "__main__":
    test_predict_demand()
