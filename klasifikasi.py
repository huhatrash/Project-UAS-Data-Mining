import streamlit as st
import numpy as np
import pickle
import pandas as pd
import os
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def run_klasifikasi():
    st.title("Klasifikasi Diabetes")
    st.markdown("""
    Model ini digunakan untuk memprediksi apakah pasien mengidap diabetes berdasarkan parameter medis.
    """)

    if not os.path.exists("model_klasifikasi.pkl"):
        st.error("Model belum ditemukan. Silakan latih model terlebih dahulu.")
        return

    model = pickle.load(open("model_klasifikasi.pkl", "rb"))
    df = pd.read_csv("diabetes.csv")
    X = df.drop(columns=["Outcome"])
    y = df["Outcome"]
    y_pred = model.predict(X)

    st.subheader("Metrik Klasifikasi")
    st.code(classification_report(y, y_pred))

    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)

    st.subheader("Input Data Baru")
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input("Pregnancies", 0)
        glucose = st.number_input("Glucose", 0)
        blood_pressure = st.number_input("Blood Pressure", 0)
        skin_thickness = st.number_input("Skin Thickness", 0)
    with col2:
        insulin = st.number_input("Insulin", 0)
        bmi = st.number_input("BMI", 0.0)
        dpf = st.number_input("Diabetes Pedigree Function", 0.0)
        age = st.number_input("Age", 0)

    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

    if st.button("Prediksi"):
        prediction = model.predict(input_data)
        hasil = "✅ Diabetes" if prediction[0] == 1 else "❎ Tidak Diabetes"
        st.success(f"Hasil Prediksi: {hasil}")