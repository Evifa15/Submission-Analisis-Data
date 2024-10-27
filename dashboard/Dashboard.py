import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Prepare DataFrame
# Load your data here
# For example:
# All_df = pd.read_csv('your_data.csv')

# Assuming All_df is already prepared with required columns
# Example DataFrame for demonstration
data = {
    'yr_x': [0, 0, 0, 0, 1, 1, 1, 1],
    'season_x': [1, 2, 3, 4, 1, 2, 3, 4],
    'cnt_y': [4338, 5929, 4599, 4846, 5493, 4603, 5372, 4872],
    'day_type': ['Holiday', 'Regular Weekday', 'Working Day', 'Regular Weekday', 'Holiday', 'Working Day', 'Regular Weekday', 'Regular Weekday'],
    'Average Rentals': [16, 40, 15.33, 40, 16, 15.33, 40, 40]
}

All_df = pd.DataFrame(data)

# Step 2: Create Filter Components
st.sidebar.header("Filters")
year_filter = st.sidebar.selectbox("Select Year:", options=[0, 1])
season_filter = st.sidebar.selectbox("Select Season:", options=[1, 2, 3, 4])

# Filter data based on selections
filtered_data = All_df[(All_df['yr_x'] == year_filter) & (All_df['season_x'] == season_filter)]

# Step 3: Enhance the Dashboard with Various Data Visualizations
st.title("Bike Rentals Dashboard")

# Visualization 1: Total bike rentals by year and season
st.subheader("Total Bike Rentals by Year and Season")
year_season_rentals = All_df.groupby(["yr_x", "season_x"], observed=False)["cnt_y"].sum().reset_index()
sns.barplot(x='season_x', y='cnt_y', hue='yr_x', data=year_season_rentals, palette='viridis')
plt.title("Total Bike Rentals by Year and Season")
st.pyplot(plt)

# Visualization 2: Average bike rentals by day type
st.subheader("Average Bike Rentals by Day Type")
average_rentals = All_df.groupby("day_type", observed=False)["Average Rentals"].mean().reset_index()
sns.barplot(x='day_type', y='Average Rentals', data=average_rentals, palette=["#72BCD4", "#D3D3D3", "#B0C4DE"])
plt.title("Average Bike Rentals by Day Type")
plt.xlabel("Type of Day")
plt.ylabel("Average Rentals")
st.pyplot(plt)

# Optionally, you can display the filtered data as a table
st.subheader("Filtered Data")
st.write(filtered_data)

