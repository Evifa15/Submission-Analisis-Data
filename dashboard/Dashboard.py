import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSS Styles for Enhanced UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    /* General background */
    .main {
        background-color: #f7f9fc;
    }

    /* Header styles */
    .header {
        padding: 20px;
        text-align: center;
        background-color: #ffffff;
    }
    .header-title {
        color: #4A90E2;
        font-weight: 700;
        font-size: 2.5rem;
    }
    .header-subtitle {
        color: #666;
        font-size: 1.1rem;
    }

    /* Sidebar and content styles */
    .css-1d391kg { 
        background-color: #ffffff; 
    }
    </style>
""", unsafe_allow_html=True)

# Data Preparation
data = {
    'yr_x': [0, 0, 0, 0, 1, 1, 1, 1],
    'season_x': [1, 2, 3, 4, 1, 2, 3, 4],
    'cnt_y': [4338, 5929, 4599, 4846, 5493, 4603, 5372, 4872],
    'season_name': ['Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter'],
    'day_type': ['Holiday', 'Regular Weekday', 'Working Day', 'Regular Weekday', 'Holiday', 'Working Day', 'Regular Weekday', 'Regular Weekday'],
    'Average Rentals': [16, 40, 15.33, 40, 16, 15.33, 40, 40]
}
All_df = pd.DataFrame(data)

# Frame 1: Header
with st.container():
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.markdown('<div class="header-title">🚴 Bike Rentals Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="header-subtitle">Analyze seasonal and daily trends in bike rentals.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.header("Filters")
year_filter = st.sidebar.selectbox("Select Year:", options=All_df['yr_x'].unique())
season_filter = st.sidebar.selectbox("Select Season:", options=All_df['season_x'].unique())

# Filtered Data based on Sidebar selections
filtered_data = All_df[(All_df['yr_x'] == year_filter) & (All_df['season_x'] == season_filter)]

# Frame 2: Visualizations and Filtered Data Table
with st.container():
    col1, col2 = st.columns([1, 1])

    # Visualization 1: Total bike rentals by year and season
    with col1:
        st.subheader("Total Bike Rentals by Year and Season")
        year_season_rentals = All_df.groupby(["yr_x", "season_x", "season_name"], observed=False)["cnt_y"].sum().reset_index()
        year_season_rentals_filtered = year_season_rentals[year_season_rentals['yr_x'] == year_filter]
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(y="season_name", x="cnt_y", hue="yr_x", data=year_season_rentals_filtered, palette=["#4A90E2", "#D3D3D3"], ax=ax)
        ax.set_xlabel("Total Rentals")
        ax.set_ylabel("Season")
        ax.set_title("Total Bike Rentals by Season and Year", fontsize=15)
        st.pyplot(fig)

    # Visualization 2: Average bike rentals by day type
    with col2:
        st.subheader("Average Bike Rentals by Day Type")
        average_rentals = All_df.groupby("day_type", observed=False)["Average Rentals"].mean().reset_index()
        average_rentals.columns = ['Type of Day', 'Average Rentals']
        average_rentals_filtered = average_rentals  # No filter needed for average rentals
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(y='Type of Day', x='Average Rentals', data=average_rentals_filtered, palette=["#4A90E2", "#D3D3D3", "#B0C4DE"], ax=ax)
        ax.set_title("Average Bike Rentals by Day Type", fontsize=15)
        st.pyplot(fig)

    # Filtered Data Table
    st.subheader("Filtered Data")
    st.write(filtered_data)
