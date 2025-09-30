# Fraud Detection MSc Project

## Overview
This project implements a fraud detection pipeline using the PaySim dataset, including data subsampling, preprocessing, model training, drift adaptation, SHAP explanations, and evaluation. A Streamlit app is provided for interactive exploration.

## Structure
- `data/`: Raw and processed datasets
- `scripts/`: Data processing and modeling scripts
- `models/`: Saved models and explainers
- `outputs/`: Visualizations
- `app/`: Streamlit web app

## Setup
1. Install dependencies: `pip install -r app/requirements.txt`
2. Run preprocessing and training scripts in `scripts/`
3. Launch the app: `streamlit run app/app.py`

## Deployment
See `deploy.sh` for deployment instructions (Streamlit Cloud/Heroku).
