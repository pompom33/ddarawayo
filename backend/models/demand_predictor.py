import os
import pickle

from backend.models import model_input

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, '..', 'files', 'LGBMmodel.pkl')

# 1. LGBM모델 불러오기
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# 2. input data 불러오기
def load_model_input():
    input_df = model_input.run_model_input_pipeline()
    return input_df

# 3. 수요 예측
def predict_demand(model, df):
    feature_cols = [
        'Rental_Location_ID', 'bus_stop', 'park', 'school', 'subway', 'riverside', 'month', 'hour', 'weekday'
    ]
    X = df[feature_cols]
    predictions = model.predict(X)

    predictions_df = df[['Rental_Location_ID']].copy()
    predictions_df['predicted_demand'] = predictions

    return predictions_df

# 4. 전체 파이프라인 실행
def run_demand_predictor_pipeline():
    model_path = MODEL_PATH
    model = load_model(model_path)
    input_df = load_model_input()
    result_df = predict_demand(model, df=input_df)
    return result_df

# 테스트용
# if __name__ == "__main__":
#     result = run_demand_predictor_pipeline()
#     print(result)