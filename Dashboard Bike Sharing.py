import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv("CleanData.csv")

# Title
st.title("Dashboard Analisis Penyewaan Sepeda")

# Sidebar filters
st.sidebar.header("Filter")
temp_category = st.sidebar.selectbox("Pilih Kategori Suhu", ["All"] + list(day_df['temp_cat'].unique()))

# Filter data
if temp_category != "All":
    filtered_df = day_df[day_df['temp_cat'] == temp_category]
else:
    filtered_df = day_df

# Show data preview
st.subheader("Tabel Data Penyewaan Sepeda")
st.dataframe(filtered_df.head())

# Visualisasi Penyewaan Sepeda Berdasarkan Hari Kerja dan Hari Libur
st.subheader("Banyaknya Penyewa Sepeda Pada Hari Kerja dan Hari libur")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    y='cnt',
    x='workingday',
    data=filtered_df.groupby('workingday')['cnt'].sum().reset_index(),
    ax=ax
)
ax.set_xlabel("Hari (0 = Libur, 1 = Kerja)")
ax.set_ylabel("Jumlah Pengguna")
st.pyplot(fig)

# Visualisasi Pengaruh Suhu terhadap Penyewaan Sepeda
st.subheader("Pengaruh Suhu Pada Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    y='cnt',
    x='ntemp',
    data=filtered_df.groupby('ntemp')['cnt'].sum().reset_index(),
    ax=ax
)
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Pengguna")
st.pyplot(fig)

# Menampilkan Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(filtered_df[['cnt', 'casual', 'registered']].describe())
