import streamlit as st
st.set_page_config(page_title="Fraud Detection App", page_icon="🟢", layout="centered")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scripts.model_utils import load_model, predict_with_explainer, get_feature_names
from scripts.theme import set_green_theme

def main():
	set_green_theme()
	st.title("Fraud Detection Web App")
	st.markdown("""
	#### Enter transaction details below to check for fraud risk.
	""")

	# Load model and explainer
	model = load_model()
	try:
		import shap
		explainer = shap.TreeExplainer(model)
	except ImportError:
		explainer = None
	feature_names = get_feature_names()

	def input_form():
		with st.form("fraud_form"):
			amount = st.slider("Amount", min_value=0.0, max_value=100000.0, value=1000.0, step=10.0)
			oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=5000.0)
			newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=4000.0)
			oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=2000.0)
			newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=3000.0)
			hour = st.selectbox("Hour of Transaction", options=list(range(24)), index=12)
			isMerchant = st.radio("Is Destination a Merchant?", options=["Yes", "No"], index=1)
			submit = st.form_submit_button("Check Fraud Risk")
		errors = []
		if newbalanceOrig > oldbalanceOrg:
			errors.append("New Balance Origin cannot be greater than Old Balance Origin.")
		if newbalanceDest < oldbalanceDest:
			errors.append("New Balance Destination cannot be less than Old Balance Destination.")
		return {
			"amount": amount,
			"oldbalanceOrg": oldbalanceOrg,
			"newbalanceOrig": newbalanceOrig,
			"oldbalanceDest": oldbalanceDest,
			"newbalanceDest": newbalanceDest,
			"hour": hour,
			"isMerchant": 1 if isMerchant == "Yes" else 0,
			"errors": errors,
			"submit": submit
		}

	user_input = input_form()

	if user_input["submit"]:
		if user_input["errors"]:
			for err in user_input["errors"]:
				st.error(err)
		else:
			input_df = pd.DataFrame([{k: v for k, v in user_input.items() if k in feature_names}])
			pred, shap_values = predict_with_explainer(model, explainer, input_df)
			if pred == 1:
				st.markdown("<div style='background-color:#b2f7b2;padding:1em;border-radius:10px;text-align:center;'><h2 style='color:#006400;'>Likely Fraudulent Transaction</h2></div>", unsafe_allow_html=True)
			else:
				st.markdown("<div style='background-color:#e6ffe6;padding:1em;border-radius:10px;text-align:center;'><h2 style='color:#228B22;'>Not Likely Fraud</h2></div>", unsafe_allow_html=True)
			st.markdown("#### Why this prediction?")
			fig, ax = plt.subplots(figsize=(8, 3))
			shap_df = pd.DataFrame({
				'Feature': feature_names,
				'SHAP Value': shap_values[1][0] if isinstance(shap_values, list) else shap_values[0]
			})
			sns.barplot(x='SHAP Value', y='Feature', data=shap_df, ax=ax, palette='Greens')
			ax.set_title('Feature Impact on Prediction')
			st.pyplot(fig)
			st.markdown("<small>Positive values push towards fraud, negative towards non-fraud.</small>", unsafe_allow_html=True)

if __name__ == "__main__":
	main()
# Streamlit web app entry point
