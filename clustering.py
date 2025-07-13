import streamlit as st
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def run_clustering():
    st.title("📍 Clustering Lokasi Gerai Kopi")

    st.markdown("*Mengelompokkan lokasi gerai kopi berdasarkan fitur numerik menggunakan algoritma K-Means.*")

    if not os.path.exists("model_kmeans.pkl") or not os.path.exists("lokasi_gerai_kopi_clean.csv"):
        st.error("❌ Model clustering atau data tidak ditemukan.")
        return

    model = pickle.load(open("model_kmeans.pkl", "rb"))
    df = pd.read_csv("lokasi_gerai_kopi_clean.csv")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    # Prediksi cluster
    cluster_labels = model.predict(X_scaled)
    df['Cluster'] = cluster_labels

    # Visualisasi
    st.subheader("Visualisasi Hasil Clustering")
    if df.shape[1] >= 2:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(x=df.iloc[:, 0], y=df.iloc[:, 1], hue=cluster_labels, palette="Set2", s=100, ax=ax)
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel(df.columns[1])
        ax.set_title("Visualisasi Cluster")
        st.pyplot(fig)

    # Input Data Baru
    st.subheader("Input Data Baru")
    col1, col2 = st.columns(2)
    input_vals = []

    for i, col in enumerate(df.columns[:-1]):
        with col1 if i % 2 == 0 else col2:
            val = st.number_input(f"{col}", min_value=0.0, step=1.0)
            input_vals.append(val)

    input_data = scaler.transform([input_vals])

    if st.button("Prediksi Cluster"):
        cluster = model.predict(input_data)
        st.success(f"📌 Data termasuk dalam **Cluster {cluster[0]}**")
