import joblib
import pandas as pd
import shap
from pathlib import Path

def load_model(model_path=None):
    if model_path is None:
        model_path = Path("models/dtc/model_11.pkl")
    return joblib.load(model_path)

def get_feature_names():
    return ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'hour', 'isMerchant']

def predict_with_explainer(model, explainer, input_df):
    pred = model.predict(input_df)[0]
    shap_values = explainer.shap_values(input_df)
    return pred, shap_values
