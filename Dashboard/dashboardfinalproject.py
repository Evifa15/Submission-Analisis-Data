import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

# Set style seaborn
sns.set(style='dark')

#Preparing the day_df data
day_df = pd.read_csv("https://raw.githubusercontent.com/Evifa15/Submission/refs/heads/main/data/day.csv")
day_df.head()

# Removing unnecessary columns
drop_col = ['windspeed']

for i in day_df.columns:
  if i in drop_col:
    day_df.drop(labels=i, axis=1, inplace=True)

# Renaming column headers
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

# Converting numbers to labels
day_df['month'] = day_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weather_cond'] = day_df['weather_cond'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})


# Preparing daily_rent_df
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dateday').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df

# Preparing daily_casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dateday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Preparing daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dateday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
# Preparing season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

# Preparing monthly_rent_df
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='month').agg({
        'count': 'sum'
    })
    ordered_months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    monthly_rent_df = monthly_rent_df.reindex(ordered_months, fill_value=0)
    return monthly_rent_df

# Preparing weekday_rent_df
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Preparing workingday_rent_df
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'count': 'sum'
    }).reset_index()
    return workingday_rent_df

# Preparing holiday_rent_df
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'count': 'sum'
    }).reset_index()
    return holiday_rent_df

# Preparing weather_rent_df
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weather_cond').agg({
        'count': 'sum'
    })
    return weather_rent_df


# Creating filter components
min_date = pd.to_datetime(day_df['dateday']).dt.date.min()
max_date = pd.to_datetime(day_df['dateday']).dt.date.max()
 
# Sidebar
st.sidebar.title("About Dashboard")
st.sidebar.info(
    """
    **Bike Rental Analysis** adalah dashboard interaktif yang dirancang untuk
    menganalisis tren penggunaan sepeda berdasarkan data historis.

    Fitur utama dashboard ini:
    - Melihat pola penggunaan sepeda berdasarkan musim, waktu, dan cuaca.
    - Menyediakan insight untuk meningkatkan layanan penyewaan sepeda.

    **Dibuat oleh Evi Fauziah (m764b4kx1297)** 🌟
    """
)
    
# Getting start_date & end_date from date_input
start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df['dateday'] >= str(start_date)) & 
                (day_df['dateday'] <= str(end_date))]

# Preparing various dataframes
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)


# Creating Dashboard
# Creating title
st.markdown('<h1 style="color:#4682b4;">Dashboard of Bike Rental 🚲</h1>', unsafe_allow_html=True)

# Creating daily rental count
st.subheader('𐙚 Daily Rentals')
col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.markdown(f'<div style="border: 2px solid #4682b4; padding: 10px; border-radius: 8px; text-align: center;">'
                f'<h3>Casual User</h3>'
                f'<p style="font-size: 20px;">{daily_rent_casual}</p>'
                '</div>', unsafe_allow_html=True)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.markdown(f'<div style="border: 2px solid #4682b4; padding: 10px; border-radius: 8px; text-align: center;">'
                f'<h3>Registered User</h3>'
                f'<p style="font-size: 20px;">{daily_rent_registered}</p>'
                '</div>', unsafe_allow_html=True)

with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.markdown(f'<div style="border: 2px solid #4682b4; padding: 10px; border-radius: 8px; text-align: center;">'
                f'<h3>Total User</h3>'
                f'<p style="font-size: 20px;">{daily_rent_total}</p>'
                '</div>', unsafe_allow_html=True)

if {'casual', 'registered'}.issubset(day_df.columns):
    daily_rent_casual = day_df['casual'].sum()
    daily_rent_registered = day_df['registered'].sum()
    categories = ['Casual Users', 'Registered Users']
    rentals = [daily_rent_casual, daily_rent_registered]
    fig, ax = plt.subplots(figsize=(3, 2))
    colors = ['#add8e6', '#4682b4']  
    wedges, texts, autotexts = ax.pie(
        rentals,
        labels=categories,
        autopct='%1.1f%%', 
        startangle=90,  
        colors=colors
    )
    for text in texts:
        text.set_fontsize(4)
    for autotext in autotexts:
        autotext.set_fontsize(4)

    st.pyplot(fig)
else:
    st.error("Data harus mengandung kolom 'casual' dan 'registered'.")

# Creating visualization of weather, temperature, and humidity affect the number of bike users
palette = ["#72BCD4", "#4A90A4", "#A3C9D1"]
st.title("𐙚 Bike Usage Analysis by weather, temperature, and humidity")
st.write("This app visualizes bike usage data based on weather, temperature, and humidity.")
fig, ax = plt.subplots(2, 2, figsize=(14, 10))
sns.barplot(x='weather_cond', y='count', data=day_df, ax=ax[0, 0], palette=palette)
ax[0, 0].set_title('Bike Users by Weather Condition')
ax[0, 0].set_xlabel('Weather Condition')
ax[0, 0].set_ylabel('Number of Bike Users')
ax[0, 0].tick_params(axis='x', rotation=45)  
temp_bins = pd.cut(day_df['temp'], bins=5)  
temp_group = day_df.groupby(temp_bins)['count'].mean().reset_index()
sns.barplot(x=temp_bins.astype(str), y=temp_group['count'], ax=ax[0, 1], color=palette[0])
ax[0, 1].set_title('Average Bike Users by Temperature Range')
ax[0, 1].set_xlabel('Temperature Range')
ax[0, 1].set_ylabel('Number of Bike Users')
ax[0, 1].tick_params(axis='x', rotation=45)
hum_bins = pd.cut(day_df['hum'], bins=5)  
hum_group = day_df.groupby(hum_bins)['count'].mean().reset_index()
sns.barplot(x=hum_bins.astype(str), y=hum_group['count'], ax=ax[1, 0], color=palette[1])
ax[1, 0].set_title('Average Bike Users by Humidity Range')
ax[1, 0].set_xlabel('Humidity Range')
ax[1, 0].set_ylabel('Number of Bike Users')
ax[1, 0].tick_params(axis='x', rotation=45)
correlation_matrix = day_df[['temp', 'hum', 'count']].corr()
corr_data = correlation_matrix.stack().reset_index()
corr_data.columns = ['Variable 1', 'Variable 2', 'Correlation']
sns.barplot(x='Variable 1', y='Correlation', hue='Variable 2', data=corr_data, ax=ax[1, 1], palette=palette)
ax[1, 1].set_title('Correlation between Variables')
ax[1, 1].set_xlabel('Variable 1')
ax[1, 1].set_ylabel('Correlation')
ax[1, 1].tick_params(axis='x', rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Creating visualization of Casual and Registered users use bikes on working days, holidays, and weekdays
st.title("𐙚 Bike Usage Based on Workdays, Holidays, and Weekdays")
st.write("This app visualizes bike usage data based on working days, holidays, and weekdays.")
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 10))
blue_color = "#1f77b4"
sns.barplot(
    x='workingday',
    y='count',
    data=day_df,
    ax=axes[0],
    color=blue_color)
axes[0].set_title('Number of Bike Users Based on Working Days')
axes[0].set_xlabel('Working Day')
axes[0].set_ylabel('Number of Bike Users')
sns.barplot(
    x='holiday',
    y='count',
    data=day_df,
    ax=axes[1],
    color=blue_color)
axes[1].set_title('Number of Bike Users Based on Holidays')
axes[1].set_xlabel('Holiday')
axes[1].set_ylabel('Number of Bike Users')
sns.barplot(
    x='weekday',
    y='count',
    data=day_df,
    ax=axes[2],
    color=blue_color)
axes[2].set_title('Number of Bike Users Based on Weekdays')
axes[2].set_xlabel('Day of the Week')
axes[2].set_ylabel('Number of Bike Users')
plt.tight_layout()
st.pyplot(fig)

# Creating visualization of yearly trends in bike usage, 2011 and 2012.
day_df['month'] = pd.Categorical(day_df['month'], categories=[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)
monthly_counts = day_df.groupby(by=["month", "year"]).agg({
    "count": "sum"
}).reset_index()
monthly_counts['year'] = monthly_counts['year'].replace({0: '2011', 1: '2012'})
st.title("𐙚 Total Number of Bike Rentals by Month and Year")
st.write("This chart shows the total number of bikes rented by month for the years 2011 and 2012.")
plt.figure(figsize=(15, 8))
sns.barplot(
    data=monthly_counts,
    x="count",
    y="month",
    hue="year",
    palette={"2011": "#A3C9D1", "2012": "#1f77b4"}, 
    orient='h' 
)
plt.title("Total Number of Bikes Rented by Month and Year", fontsize=16)
plt.xlabel("Total Rentals", fontsize=12)
plt.ylabel("Month", fontsize=12)
plt.legend(title="Year", loc="upper right", fontsize=10, title_fontsize=12)
plt.tight_layout()
st.pyplot(plt)

st.write("© 2024 by Evi Fauziah (m764b4kx1297)- Machine Learning Cohort")