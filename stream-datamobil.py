import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Analisis Data Mobil")

# Membaca data dari GitHub
url = "https://raw.githubusercontent.com/apriyantodwiherlambang/datamobil/main/DataMobil.csv"
try:
    df = pd.read_csv(url)
    
    # Menampilkan data
    st.subheader("Data Mobil")
    st.write(df.head())

    # Memilih kolom untuk analisis
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if numeric_columns.any():
        st.subheader("Analisis Data Numerik")

        column = st.selectbox("Pilih kolom untuk visualisasi", numeric_columns)

        # Histogram
        st.write(f"Histogram kolom {column}")
        fig, ax = plt.subplots()
        ax.hist(df[column].dropna(), bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel(column)
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)

        # Statistik deskriptif
        st.write("Statistik deskriptif")
        st.write(df[column].describe())

    else:
        st.warning("Data tidak memiliki kolom numerik untuk dianalisis.")

    # Analisis data kategorikal
    categorical_columns = df.select_dtypes(include=['object']).columns
    if categorical_columns.any():
        st.subheader("Analisis Data Kategorikal")

        cat_column = st.selectbox("Pilih kolom kategorikal", categorical_columns)

        # Frekuensi nilai unik
        st.write(f"Frekuensi nilai unik pada kolom {cat_column}")
        st.write(df[cat_column].value_counts())

        # Diagram batang
        st.write(f"Diagram batang kolom {cat_column}")
        fig, ax = plt.subplots()
        df[cat_column].value_counts().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
        ax.set_xlabel(cat_column)
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)

    else:
        st.warning("Data tidak memiliki kolom kategorikal untuk dianalisis.")

except Exception as e:
    st.error(f"Terjadi kesalahan saat membaca data: {e}")
