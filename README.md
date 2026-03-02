Threat Intelligence Insights and Recommendation Engine
A streamlit-bsed decision support tool that analyzes cyber incident data to recommend optimal defense strategies, estimate resolution efficiency and provide threat intelligence insights for cybersecurity planning

This project focuses on descriptive and prescriptive analysis

Traditional cybersecurity models often struggle with "noisy" data leading to low predictive accuracy. This project address the challenge by implementing a Hybrid Intelligence System
1. Predictive Baseline: a Random Forest model that assess the risk level of an incoming threat
2. Prescriptive Engine: A strategy optimizer that maps current attack signatures to historically successful protocols, identifying the optimal solution for incident response

Technical Stack
Python, Pandas, NumPy, Streamlit, Plotly Express, Scikit-Learn(Random Forest and XGBoost)

Observation:
During development it was observed that high entropy in incident data limited standalone model accuract to approximately 43%. By pivoting to a prescriptive strategy engine, the system provides historically acurate defense recommendations.

Deployed on Streamlit Cloud: https://cyberec.streamlit.app
