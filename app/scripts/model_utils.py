import joblib
import pandas as pd
from pathlib import Path

def load_model(model_path=None):
    if model_path is None:
        model_path = Path("models/dtc/model_11.pkl")
    return joblib.load(model_path)

def get_feature_names():
    return ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'hour', 'isMerchant']

def predict_with_explainer(model, explainer, input_df):
    pred = model.predict(scale_data(input_df))[0]
    shap_values = explainer.shap_values(input_df)
    return pred, shap_values

def scale_data(data):
    """ scale input using scaler model"""
    features = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'hour']
    to_scale = data[features]

    # load scaler model
    scaler = joblib.load("models/scaler.pkl")
    scaled_data = scaler.transform(to_scale)

    scaled_data = pd.DataFrame(scaled_data, columns=to_scale.columns)
    
    # bring isMerchant back in
    scaled_data['isMerchant'] = data['isMerchant']

    return scaled_data
