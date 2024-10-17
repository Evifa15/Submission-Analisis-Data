import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')



# 1. Memastikan tema
st.set_page_config(page_title="Bike Rentals Dashboard", layout="wide")

# 2. Menyiapkan data sewa sepeda
data_2010 = {
    'year': [2010] * 10,
    'total_rentals': [4401, 4459, 5260, 4073, 5698, 1162, 4098, 4758, 6824, 5312]
}

data_2011 = {
    'year': [2011] * 10,
    'total_rentals': [36, 27, 26, 16, 12, 12, 12, 11, 11, 10]
}

# Membuat DataFrames untuk setiap tahun
df_2010 = pd.DataFrame(data_2010)
df_2011 = pd.DataFrame(data_2011)

# Menghitung total rentals untuk setiap tahun
total_rentals_2010 = df_2010['total_rentals'].sum()
total_rentals_2011 = df_2011['total_rentals'].sum()

# Mengompilasi DataFrame untuk visualisasi
summary_df = pd.DataFrame({
    'Year': ['2010', '2011'],
    'Total Rentals': [total_rentals_2010, total_rentals_2011]
})

# Judul dashboard
st.title('Bike Rentals Dashboard')
st.subheader('Overview of Bike Rentals in 2010 and 2011')

# Menampilkan DataFrame
st.write("Summary of Total Rentals:")
st.dataframe(summary_df)  # Menampilkan tabel dengan format yang baik

# Menampilkan Pie Chart
labels = ['Working Days', 'Non-Working Days']
sizes = [500, 231]  # Misalkan ini adalah jumlah sewa untuk hari kerja dan non-kerja

# Membuat Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart of Working vs Non-Working Days')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
st.pyplot(plt)  # Menampilkan Pie Chart di Streamlit

# Menampilkan Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(summary_df['Year'], summary_df['Total Rentals'], color=['blue', 'orange'])
plt.title('Total Bike Rentals in 2010 vs 2011')
plt.xlabel('Year')
plt.ylabel('Total Rentals')
plt.ylim(0, max(summary_df['Total Rentals']) * 1.1)  # Batas sumbu y
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(plt)  # Menampilkan Bar Chart di Streamlit



