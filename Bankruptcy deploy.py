import streamlit as st
import pandas as pd
from pickle import load

model = load(open('Bankruptcy.pkl','rb'))

st.title(" Bankruptcy Prevention")



st.subheader(" Enter the Company Features: ")
industrial_risk = st.selectbox("Industrial_Risk",[0,0.5,1])
management_risk = st.selectbox("Management_Risk",[0,0.5,1])
financial_flexibility = st.selectbox("Financial_Flexibility",[0,0.5,1])
credibility = st.selectbox("Credibility",[0,0.5,1])
competitiveness = st.selectbox("Competitiveness",[0,0.5,1])
operating_risk = st.selectbox(" Operating_Risk ",[0,0.5,1])

def predict():
    input = {
    "industrial_risk":[industrial_risk],
    "management_risk":[management_risk],
    "financial_flexibility" :[financial_flexibility],
    "credibility":[credibility],
    "competitiveness":[competitiveness],
    "operating_risk":[operating_risk]}

    input = pd.DataFrame(input)
    prediction = model.predict(input)[0]
    if prediction == 1:
        st.title(":red[Bankrupt]")
    else:
        st.title(":green[Non-Bankrupt]")
    

if st.button(" Predict Bankrupty"):
     result =  predict()