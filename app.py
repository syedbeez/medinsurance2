import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title of the app
st.title("Medical Insurance Cost Prediction")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)

children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

smoker = st.radio("Smoker", ["No", "Yes"])

region_northwest = st.checkbox("Northwest")

region_southeast = st.checkbox("Southeast")

region_southwest = st.checkbox("Southwest")

# Convert categorical inputs
smoker = 1 if smoker == "Yes" else 0

# Prepare input for prediction
input_data = np.array([[age, bmi, children, smoker, region_northwest, region_southeast, region_southwest]])

# Predict
if st.button("Predict Medical Charges"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Medical Charges: ${prediction:.2f}")
