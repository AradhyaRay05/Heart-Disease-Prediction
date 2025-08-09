import streamlit as st
import tensorflow as tf
import joblib
import numpy as np
import keras

model = tf.keras.models.load_model('model.keras')
scaler = joblib.load('scaler.pkl')

st.title('Heart Disease Prediction')
st.write('Enter the patient\'s information to predict the likelihood of heart disease.')
age = st.slider('Age', min_value=0, max_value=120, value=50)
sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3])
trestbps = st.slider('Resting Blood Pressure (trestbps)', min_value=0, max_value=300, value=120)
chol = st.slider('Cholesterol (chol)', min_value=0, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', options=[0, 1])
restecg = st.selectbox('Resting Electrocardiographic Results (restecg)', options=[0, 1, 2])
thalach = st.slider('Maximum Heart Rate Achieved (thalach)', min_value=0, max_value=250, value=150)
exang = st.selectbox('Exercise Induced Angina (exang)', options=[0, 1])
oldpeak = st.slider('ST depression induced by exercise relative to rest (oldpeak)', min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox('Slope of the peak exercise ST segment (slope)', options=[0, 1, 2])
ca = st.selectbox('Number of major vessels (0-3) colored by flourosopy (ca)', options=[0, 1, 2, 3])
thal = st.selectbox('Thal', options=[0, 1, 2, 3])

if st.button('Predict'):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    scaled_input_data = scaler.transform(input_data)
    prediction_probability = model.predict(scaled_input_data)
    prediction = 1 if prediction_probability > 0.5 else 0
    if prediction == 1:
        st.error('Prediction: Heart Disease Detected')
    else:
        st.success('Prediction: No Heart Disease Detected')
