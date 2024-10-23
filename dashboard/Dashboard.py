import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data Bike Rentals by Year and Season
data_season = {
    'year': [2011, 2011, 2011, 2011, 2012, 2012, 2012, 2012],
    'season': ['Winter', 'Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall'],
    'cnt': [147742, 347316, 413607, 321942, 305398, 541829, 632765, 507511]
}

# Membuat DataFrame untuk bike rentals by season
df_season = pd.DataFrame(data_season)

# Mengelompokkan data berdasarkan season untuk mendapatkan total rentals per season
seasonal_rentals = df_season.groupby('season').agg({'cnt': 'sum'}).reset_index()

# Mengurutkan sesuai musim untuk lebih mudah dibaca
season_order = ['Winter', 'Spring', 'Summer', 'Fall']
seasonal_rentals['season'] = pd.Categorical(seasonal_rentals['season'], categories=season_order, ordered=True)
seasonal_rentals = seasonal_rentals.sort_values('season')

# Data untuk Bike Rentals by Weekday and Holiday Status
data_weekday = {
    'weekday': [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],
    'holiday': ['Regular Day', 'Regular Day', 'Holiday', 'Regular Day', 'Holiday', 'Regular Day', 'Holiday', 
                'Regular Day', 'Holiday', 'Regular Day', 'Holiday', 'Regular Day'],
    'cnt': [338936, 331548, 49772, 393654, 1013, 384915, 5721, 396221, 3920, 415592, 6494, 341469]
}

# Membuat DataFrame untuk Bike Rentals by Weekday and Holiday Status
df_weekday = pd.DataFrame(data_weekday)

# Memisahkan data untuk hari libur dan regular day
holiday_avg = df_weekday[df_weekday['holiday'] == 'Holiday']['cnt'].mean()
regular_day_avg = df_weekday[df_weekday['holiday'] == 'Regular Day']['cnt'].mean()

# Membuat DataFrame untuk perbandingan rata-rata rentals
comparison_df = pd.DataFrame({
    'Category': ['Holiday', 'Regular Day'],
    'Average Bike Rentals': [holiday_avg, regular_day_avg]
})

# Judul Aplikasi
st.title("Bike Rentals Dashboard")

# Bagian 1: Visualisasi Total Bike Rentals by Season
st.subheader("Total Bike Rentals by Season")

# Membuat plot untuk Total Bike Rentals by Season
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.bar(seasonal_rentals['season'], seasonal_rentals['cnt'], color='skyblue')

# Menambahkan judul dan label
ax1.set_title('Total Bike Rentals by Season', fontsize=14)
ax1.set_xlabel('Season', fontsize=12)
ax1.set_ylabel('Total Rentals', fontsize=12)

# Menampilkan nilai di atas setiap bar
for index, value in enumerate(seasonal_rentals['cnt']):
    ax1.text(index, value + 20000, str(value), ha='center', fontsize=10)

# Menampilkan plot di Streamlit
st.pyplot(fig1)

# Bagian 2: Visualisasi Average Bike Rentals on Holidays vs Regular Days
st.subheader("Average Bike Rentals on Holidays vs Regular Days")

# Membuat plot untuk perbandingan rata-rata bike rentals pada hari libur dan regular day
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.bar(comparison_df['Category'], comparison_df['Average Bike Rentals'], color=['orange', 'blue'])

# Menambahkan judul dan label
ax2.set_title('Average Bike Rentals on Holidays vs Regular Days', fontsize=16)
ax2.set_xlabel('Category', fontsize=12)
ax2.set_ylabel('Average Bike Rentals', fontsize=12)

# Menampilkan plot di Streamlit
st.pyplot(fig2)

# Penjelasan tambahan
st.markdown("""
- **Total Bike Rentals by Season** menunjukkan jumlah total persewaan sepeda berdasarkan musim (Winter, Spring, Summer, Fall).
- **Average Bike Rentals on Holidays vs Regular Days** membandingkan rata-rata jumlah persewaan sepeda pada hari libur dan hari biasa.
""")
