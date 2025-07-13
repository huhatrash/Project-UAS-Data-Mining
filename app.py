import streamlit as st
from klasifikasi import run_klasifikasi
from clustering import run_clustering

st.set_page_config(
    page_title="Aplikasi Diabetes & Clustering",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "halaman" not in st.session_state:
    st.session_state.halaman = "Beranda"

st.markdown("""
    <style>
    .stApp {
        background-color: #141414;
        color: white;
    }

    .css-6qob1r {
        background-color: #141414 !important;
        padding: 2rem 1.5rem;
        border-right: 2px solid #00d4ff;
    }

    h1, h2, h3 {
        color: #00d4ff;
    }

    .sidebar-button {
        display: block;
        width: 100%;
        background-color: #2d2d2d;
        color: white;
        padding: 10px 16px;
        margin-bottom: 10px;
        text-align: left;
        cursor: pointer;
        font-size: 16px;
        transition: background 0.3s, color 0.3s;
    }

    .sidebar-button:hover {
        background-color: #b9ff66 !important;
        color: #b9ff66;
        font-weight: normal;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## Navigasi")

if st.sidebar.button("MainPage", key="beranda", use_container_width=True):
    st.session_state.halaman = "Beranda"

if st.sidebar.button("Clasification", key="klasifikasi", use_container_width=True):
    st.session_state.halaman = "Klasifikasi"

if st.sidebar.button("Clustering", key="clustering", use_container_width=True):
    st.session_state.halaman = "Clustering"

if st.session_state.halaman == "Beranda":
    st.title("Tampilan Klasifikasi diabetes dan clustering kmeans ")
    st.markdown("---")
    st.markdown("""
    - **Nama:** Alfa Haliza  
    - **NIM:** 22146039
    - Aplikasi ini dibangun untuk memenuhi project akhir mata kuliah Data Mining.
    """)

elif st.session_state.halaman == "Klasifikasi":
    run_klasifikasi()

elif st.session_state.halaman == "Clustering":
    run_clustering()
