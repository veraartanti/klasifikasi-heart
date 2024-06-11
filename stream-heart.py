import streamlit as st
import pickle
import numpy as np

# Load saved model
with open('deseaseheart.sav', 'rb') as file:
    model = pickle.load(file)

# # Load scaler
# with open('scaler.sav', 'rb') as file:
#     scaler = pickle.load(file)

# Title of the web app
st.title('Klasifikasi Penyakit Hati')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')
    resting_bp = st.text_input('Resting BP')
    restecg = st.text_input('Restecg')
    oldpeak = st.text_input('Oldpeak')
    thal = st.text_input('Thal')
with col2:
    sex = st.text_input('Gender')
    cholestoral = st.text_input('Cholestoral')
    max_hr = st.text_input('Max HR')
    slope = st.text_input('Slope')
    num_major_vessels = st.text_input('Num Major Vessels')
with col3:
    chest_pain_type = st.text_input('Chest Pain Type')
    fasting_blood_sugar = st.text_input('Fasting Blood Sugar')
    exang = st.text_input('Exang')

heart_diagnosis =''

# membuat tombol prediksi
if st.button('Klasifikasi Penyakit Hati'):
    heart_prediction = model.predict([[age, sex, chest_pain_type, resting_bp, 
        cholestoral, fasting_blood_sugar, restecg,
        max_hr, exang, oldpeak, slope, num_major_vessels, 
        thal]])

    if (heart_prediction[0]==1):
        heart_diagnosis = 'Pasien Mengalami Penyakit Hati'
    else:
        heart_diagnosis = 'Pasien Tidak Terindikasi Penyakit Hati'
st.success(heart_diagnosis)
