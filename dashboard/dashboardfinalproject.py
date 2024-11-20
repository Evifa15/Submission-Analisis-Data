import pandas as pd
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

    
# Creating monthly rental count
st.subheader('𐙚 Monthly Rentals')
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(
    monthly_rent_df.index,  
    monthly_rent_df['count'],  
    color='#4682b4',  
    height=0.6 
)
for index, value in enumerate(monthly_rent_df['count']):
    ax.text(value + 1, index, str(value), va='center', fontsize=16) 
ax.set_xlabel('Total Rentals', fontsize=16)
ax.set_ylabel('Month', fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
st.pyplot(fig)


# Creating rental count based on weather conditions
st.subheader('𐙚 Weatherly Rentals')
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(
    weather_rent_df.index,  
    weather_rent_df['count'],  
    color='#4682b4',  
    alpha=0.8,  
)
for index, value in enumerate(weather_rent_df['count']):
    ax.text(index, value + 1, str(value), ha='center', va='bottom', fontsize=16)  
ax.set_xlabel('Weather Condition', fontsize=16)
ax.set_ylabel('Total Rentals', fontsize=16)
ax.tick_params(axis='x', labelsize=16, rotation=45)  
ax.tick_params(axis='y', labelsize=16)
st.pyplot(fig)

# Assuming workingday_rent_df, holiday_rent_df, and weekday_rent_df are defined
st.subheader('Weekday, Workingday, and Holiday Rentals')
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))
colors1 = ["#add8e6", "#4682b4"]  
colors2 = ["#add8e6", "#4682b4"]  

# Based on workingday
axes[0].pie(
    workingday_rent_df['count'],
    labels=workingday_rent_df['workingday'].apply(lambda x: 'Working Day' if x == 1 else 'Non-working Day'),
    autopct='%1.1f%%',
    startangle=90,
    colors=colors1,
    wedgeprops=dict(width=1.0)
)
axes[0].set_title('Number of Rents based on Working Day')

# Based on holiday
axes[1].pie(
    holiday_rent_df['count'],
    labels=holiday_rent_df['holiday'].apply(lambda x: 'Holiday' if x == 1 else 'Non-holiday'),
    autopct='%1.1f%%',
    startangle=90,
    colors=colors2,
    wedgeprops=dict(width=0.4)
)
axes[1].set_title('Number of Rents based on Holiday')
plt.tight_layout()
st.pyplot(fig)

# Based on Weekday
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting a point line chart
sns.lineplot(
    x='weekday', 
    y='count', 
    data=weekday_rent_df, 
    marker='o',         # Adding points on the line
    color='blue',       # Line color blue
    linewidth=2,        # Line width
    markersize=8,       # Point size
    ax=ax
)

# Add values on the points
for index, row in enumerate(weekday_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

# Set titles and labels
ax.set_title('Number of Rents based on Weekday', fontsize=16)
ax.set_xlabel('Weekday', fontsize=14)
ax.set_ylabel('Total Rentals', fontsize=14)

# Customize tick parameters
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Adjust layout for better presentation
plt.tight_layout()

# Display the chart in Streamlit
st.pyplot(fig)