import streamlit as st
st.title("Insurance Prediction")
from src.prediction import Insurance_prediction
Age=st.number_input("Enter Age")
Annual_Income_LPA=st.number_input("Enter Annual Income in LPA")
Policy_Term_Years=st.number_input("Enter Policy Term in Years")
Sum_Assured_Lakhs=st.number_input("Enter Sum Assured in Lakhs")
if st.button("Predict"):
    obj=Insurance_prediction()
    result=obj.prediction(Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs)
    st.success(f"The predicted Annual Premium in Thousands is:  {result[0]:.2f}")
