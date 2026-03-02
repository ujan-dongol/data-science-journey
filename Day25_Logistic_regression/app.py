import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("C:/Users/Asus/Desktop/datascience/Day25_Logistic_regression/models/logistic_model.pkl")
scaler = joblib.load("C:/Users/Asus/Desktop/datascience/Day25_Logistic_regression/models/scaler.pkl")

st.title("Titanic Survival Prediction App")

st.write("Enter passenger details below:")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 1, 80, 25)
fare = st.number_input("Fare", min_value=0.0, value=10.0)

sex_encoded = 0 if sex == "male" else 1

if st.button("Predict Survival"):
    passenger = np.array([[pclass, sex_encoded, age, fare]])
    passenger_scaled = scaler.transform(passenger)
    prediction = model.predict(passenger_scaled)

    if prediction[0] == 1:
        st.success("Passenger would SURVIVE!")
    else:
        st.error("Passenger would NOT survive.")