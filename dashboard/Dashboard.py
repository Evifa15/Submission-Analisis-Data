import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load data (use st.cache_data for caching data)
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    return day_df, hour_df

day_df, hour_df = load_data()

# Title of the Dashboard
st.title('Bike Rental Analysis Dashboard')
st.header("Evi Fauziah M764B4KX1297")

# Display Descriptive Statistics for day_df
st.subheader("Descriptive Statistics for Day Data:")
st.write(day_df.describe())

# Display Descriptive Statistics for hour_df
st.subheader("Descriptive Statistics for Hour Data:")
st.write(hour_df.describe())

# Creating 'day_type' column (Holiday, Weekday, Weekend) based on weekday and holiday columns
# Example logic for creating day_type:
def create_day_type(row):
    if row['holiday'] == 1:
        return 'Holiday'
    elif row['weekday'] in [0, 6]:  # Assuming 0 is Sunday and 6 is Saturday
        return 'Weekend'
    else:
        return 'Regular Weekday'

# Apply the function to create 'day_type' column
day_df['day_type'] = day_df.apply(create_day_type, axis=1)

# Merge the dataframes
All_df = pd.merge(left=day_df, right=hour_df, how="left", left_on="instant", right_on="instant")

# Grouping by Year and Season to analyze bike rental variations
year_season_rentals = All_df.groupby(["yr_x", "season_x"], observed=False)["cnt_y"].sum().reset_index()
season_names = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
year_season_rentals["season_name"] = year_season_rentals["season_x"].map(season_names)

st.subheader("Total bike rentals by year and season:")
st.write(year_season_rentals)

# Grouping by Day type
average_rentals = All_df.groupby("day_type", observed=False)["cnt_y"].mean().reset_index()
average_rentals.columns = ['Type of Day', 'Average Rentals']

st.subheader("Average bike rentals by day type:")
st.write(average_rentals)

# Plotting Total Bike Rentals by Season and Year
st.subheader("Total Bike Rentals by Season and Year")
fig, ax = plt.subplots(figsize=(14, 7))
colors = ["#72BCD4", "#D3D3D3"]
sns.barplot(y="season_name", x="cnt_y", hue="yr_x", data=year_season_rentals, palette=colors[:year_season_rentals['yr_x'].nunique()], ax=ax)
ax.set_xlabel("Total Rentals")
ax.set_ylabel("Season")
ax.set_title("Total Bike Rentals by Season and Year", fontsize=15)
ax.tick_params(axis='x', labelsize=12)
ax.legend(title="Year", fontsize=12)
plt.tight_layout()
st.pyplot(fig)

# Plotting Average Rentals by Day Type
st.subheader("Average Bike Rentals by Day Type")
plt.figure(figsize=(10, 6))
sns.barplot(y='Type of Day', x='Average Rentals', data=average_rentals, palette=["#72BCD4", "#D3D3D3", "#B0C4DE"], hue='Type of Day', legend=False)
plt.ylabel("Type of Day")
plt.xlabel("Average Rentals")
plt.title("Average Bike Rentals by Day Type", fontsize=15)
plt.tight_layout()
st.pyplot(plt)
