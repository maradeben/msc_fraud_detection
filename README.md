# MSc Project

## Adaptive Classifier for Concept Drift with Web Interface for Fraud DetectionStakeholder

### Description:
Detects fraud, adapts to new scam tactics, and prioritizes costly frauds. A web app shows predictions, explanations (e.g., “Flagged due to new pattern”), and adaptation alerts, tested on public data.

### Technical Description

**Objective:** Develop an adaptive classifier for concept drift with a web interface.  
**Methodology:** 
**Dataset:** PaySim/IEEE-CIS Fraud Detection, simulating drift by altering fraud patterns.  
**Preprocessing:** Create time-based features, apply SMOTE for imbalance.  
**Model:** Random Forest/XGBoost (Scikit-learn) with periodic retraining or ADWIN (scikit-multiflow); cost-sensitive weighting (Bahnsen et al., 2013).  
**Interpretability:** SHAP for prediction explanations.  
**Web App:** Streamlit interface with input form, prediction, confidence score, SHAP visualization, optional drift alerts; deploy on Streamlit Cloud/Heroku.  
**Evaluation:** Cost-based metrics, precision, recall, F1-score; compare adaptive vs. non-adaptive.

**Tools:**
Python, Scikit-learn, scikit-multiflow, SHAP, Streamlit, Pandas, Streamlit Cloud/Heroku.  

**Literature Gaps:**
Concept drift (Dal Pozzolo et al., 2015–2018), cost-sensitive evaluation (Bahnsen et al., 2013), deployment (Dal Pozzolo et al., 2014), reproducibility (Btoush et al., 2023).  
**Feasibility:** Aligns with my ML and Streamlit experience; drift simplified via retraining.  
**MSc Contribution:** Novel adaptive, cost-sensitive system with deployable interface; publishable with visualizations (performance, SHAP).