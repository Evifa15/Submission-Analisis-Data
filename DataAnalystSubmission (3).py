# -*- coding: utf-8 -*-
"""DataAnalystSubmission.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19zxrVUbEG2UUBcOUhcXVXBEO_LPGQFKW

# **Data Analysis Project: [Bike Sharing Dataset]**

- **Nama:** Evi Fauziah
- **Email:** Evifauziah2022@gmail.com
- **ID Dicoding:** EviFauziah

# **Defining Business Questions**

1. Do weather, temperature, and humidity affect the number of bike users?
2. How do Casual and Registered users use bikes on working days, holidays, and weekdays?
3. What are the yearly trends in bike usage, and is 2011 or 2012 more popular?

# **Import All Packages/Libraries Used**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
from scipy import stats

"""# **Data Wrangling**

## 1. Gathering Data

At this step, we will process the data that has been collected. Since I am using the Bike Sharing Dataset, I will import the day.csv and hour.csv files.

**Loading the day table**
"""

day_df = pd.read_csv("https://raw.githubusercontent.com/Evifa15/Submission/refs/heads/main/data/day.csv")
day_df.head()

"""**Loading the hour table**"""

hour_df = pd.read_csv("https://raw.githubusercontent.com/Evifa15/Submission/refs/heads/main/data/hour.csv")
hour_df.head()

"""**Insight**

---
*   The dataset has been loaded, containing daily and hourly tables with data on bike usage, weather conditions, seasons, working days, and holidays.
*  The data is ready for analysis to uncover bike usage patterns based on weather, working days, season, and time, providing insights into rental trends.

## Assessing Data

Assume day_df and hour_df are already loaded.
Check the structure of the data

**1. Assess the day_df data**
"""

day_df.info()

"""As we can see above, there is one data type in the column that doesn't match. The data that needs to be corrected is the 'dteday' column, which should be of datetime type.

**Check for missing values**
"""

day_df.isna().sum()

"""There are no missing values.

**Check for duplicate data**
"""

print("Jumlah duplikasi data: ", day_df.duplicated().sum())

"""There are 0 duplicate data, meaning all the data is unique.

**Check for inconsistent values**
"""

day_df.describe()

"""There are no anomalies in the statistical values.

**2. Assess the hour_df data**
"""

hour_df.info()

"""**Check for missing values**"""

day_df.isna().sum()

"""There are no missing values.

**Check for duplicate data**
"""

print("Jumlah duplikasi data: ", day_df.duplicated().sum())

"""There are 0 duplicate data, meaning all the data is unique.

**Check for inconsistent values**
"""

day_df.describe()

"""There are no anomalies in the statistical values.

**3. Check for outliers using Z-score for day_df and hour_df**
"""

print("\nChecking for Outliers using Z-score:")
# For hour_df
z_scores_hour = stats.zscore(hour_df[['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']])
outliers_hour = (abs(z_scores_hour) > 3).sum(axis=0)  # Counting outliers where Z-score > 3
print("Number of outliers in each column (hour_df):")
print(outliers_hour)
# For day_df
z_scores_day = stats.zscore(day_df[['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']])
outliers_day = (abs(z_scores_day) > 3).sum(axis=0)  # Counting outliers where Z-score > 3
print("Number of outliers in each column (day_df):")
print(outliers_day)

"""**4. Display invalid values if any of day_df and hour_df**"""

print("\nChecking for Outliers using Z-score:")
# For hour_df
z_scores_hour = stats.zscore(hour_df[['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']])
outliers_hour = abs(z_scores_hour) > 3  # Identifying where Z-scores exceed 3
# Displaying the rows with outliers in hour_df
outlier_data_hour = hour_df[outliers_hour.any(axis=1)]
print("Outliers in hour_df:")
print(outlier_data_hour)
# For day_df
z_scores_day = stats.zscore(day_df[['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']])
outliers_day = abs(z_scores_day) > 3  # Identifying where Z-scores exceed 3
# Displaying the rows with outliers in day_df
outlier_data_day = day_df[outliers_day.any(axis=1)]
print("Outliers in day_df:")
print(outlier_data_day)

"""**Insight**

---


*   **Insight 1:**
day_df: No missing or duplicate data, but the 'dteday' column needs conversion to datetime for analysis accuracy.
*   **Insight 2:**hour_df: No missing or duplicate data; outliers found in several columns, particularly in 'casual' and 'windspeed'.

## Cleaning Data

**1. Removing unnecessary tablest**

We will start by removing the 'hr' table. The reason is that it is not relevant to the business question we have established. Moreover, the only difference between the 'hr' and 'day' tables is the 'hr' column; the rest of the data is identical
"""

del hour_df

"""**2. Deleting several columns that will not be used**

The columns to be dropped are:

a. instant: As the record index does not provide any additional useful information.

b. windspeed: There are no business questions related to the effect of wind speed on bike rental counts.
"""

drop_col = ['instant', 'windspeed']

for i in day_df.columns:
  if i in drop_col:
    day_df.drop(labels=i, axis=1, inplace=True)

day_df.head()

"""**3. Modifying some details of the columns**"""

#Renaming column titles
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

day_df.head()

#Renaming to 'description
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

# Change data type to datetime
 day_df['dateday'] = pd.to_datetime(day_df.dateday)

# Change data type to categorical
day_df['season'] = day_df.season.astype('category')
day_df['year'] = day_df.year.astype('category')
day_df['month'] = day_df.month.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weather_cond'] = day_df.weather_cond.astype('category')

day_df.info()

"""**Insight**

---

*   **Insight 1:** Removing irrelevant tables and columns improves data analysis efficiency and focuses on the main business question.
*  **Insight 2:**  Changing column data types to categorical optimizes memory usage and speeds up processing for further analysis.

# **Exploratory Data Analysis (EDA)**

## **Data Exploration**

**1. Grouping bike renters (both casual and registered) by month**
"""

day_df.groupby(by='month').agg({
    'count': ['max', 'min', 'mean', 'sum']
})

"""The month with the highest average and largest total is June, while the month with the smallest average and total is January

**2. Grouping bike renters (both casual and registered) by weather condition**
"""

day_df.groupby(by='weather_cond').agg({
    'count': ['max', 'min', 'mean', 'sum']
})

"""Bike renters tend to rent during clear or cloudy weather. Very few rent when it’s snowing, and none when the weather is severe.

**3. Grouping bike renters (both casual and registered) by holiday**
"""

day_df.groupby(by='holiday').agg({
    'count': ['max', 'min', 'mean', 'sum']
})

"""Bike renters prefer to rent bikes on regular days rather than during holidays

**4. Compare bike renters on weekdays vs weekends**
"""

day_df.groupby(by='weekday').agg({
    'count':['max','min','mean']
})

"""The order of average bike renters from highest to lowest is: Friday (Fri), Thursday (Thu), Saturday (Sat), Wednesday (Wed), Tuesday (Tue), Monday (Mon), and Sunday (Sun)

**5. Grouping bike renters (both casual and registered) by working day**
"""

day_df.groupby(by='workingday').agg({
    'count': ['max', 'min', 'mean']
})

"""Based on the results above, the highest number of bike rentals occurs on working days compared to non-working days. However, we can also see that the results differ somewhat, though not significantly.

**6. Kelompokkan penyewa sepeda (baik casual dan registered) berdasarkan season**
"""

day_df.groupby(by='season').agg({
    'casual': 'mean',
    'registered': 'mean',
    'count': ['max', 'min', 'mean']
})

"""Based on the analysis above, both Casual and Registered bike renters prefer the fall season, as shown by the average. The least preferred season is spring, with the lowest average.

**7. Grouping temp, hum, and humidity by season**
"""

day_df.groupby(by='season').agg({
    'temp': ['max', 'min', 'mean'],
    'atemp': ['max', 'min', 'mean'],
    'hum': ['max', 'min', 'mean']
})

"""In Spring, temp and humidity have the lowest averages, while Fall shows the highest values for temp and humidity.

**8. Relationship between casual renters, registered renters, and count**
"""

fig, ax = plt.subplots(figsize=(10,6))
correlation_matrix = day_df.corr(numeric_only=True)
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

sns.heatmap(
    correlation_matrix,
    annot=True,
    mask=mask,
    cmap="coolwarm",
    center=0,
    fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

"""**Based on the analysis above, the following conclusions can be drawn:**

1. Humidity (hum) has a weak correlation with temp and atemp, at 0.13 and 0.14.
2. Casual renters show a moderate correlation with temp and atemp (0.54), and a slight negative correlation with hum (-0.08).
3. There is a very strong correlation between atemp and temp with a value of 0.99.
4. Count shows a strong correlation with temp, atemp, casual, and registered, with values of 0.63, 0.63, 0.67, and 0.95, and a slight negative correlation with hum (-0.10).
6. Registered renters follow a similar pattern to casual renters, with a moderate correlation of 0.40 with casual.

## Insight
---
**Insight 1:**Bike renters tend to rent more during clear or cloudy weather, with very few renting during snow or severe weather.

**Insight 2:**More bike rentals occur on working days than on holidays, although the difference is not significant.

# **Visualization & Explanatory Analysis**

**1. Do weather, temperature, and humidity affect the number of bike users?**
"""

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define a unified blue color palette
palette = ["#72BCD4", "#4A90A4", "#A3C9D1"]

# Create a figure and axis for the plots
fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# Bar plot for weather conditions vs count of bike users
sns.barplot(x='weather_cond', y='count', data=day_df, ax=ax[0, 0], palette=palette)
ax[0, 0].set_title('Bike Users by Weather Condition')
ax[0, 0].set_xlabel('Weather Condition')
ax[0, 0].set_ylabel('Number of Bike Users')
ax[0, 0].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for readability

# Bar plot for temperature (grouped) vs count of bike users
temp_bins = pd.cut(day_df['temp'], bins=5)  # Create temperature bins
temp_group = day_df.groupby(temp_bins)['count'].mean().reset_index()
sns.barplot(x=temp_bins.astype(str), y=temp_group['count'], ax=ax[0, 1], color=palette[0])
ax[0, 1].set_title('Average Bike Users by Temperature Range')
ax[0, 1].set_xlabel('Temperature Range')
ax[0, 1].set_ylabel('Number of Bike Users')
ax[0, 1].tick_params(axis='x', rotation=45)

# Bar plot for humidity (grouped) vs count of bike users
hum_bins = pd.cut(day_df['hum'], bins=5)  # Create humidity bins
hum_group = day_df.groupby(hum_bins)['count'].mean().reset_index()
sns.barplot(x=hum_bins.astype(str), y=hum_group['count'], ax=ax[1, 0], color=palette[1])
ax[1, 0].set_title('Average Bike Users by Humidity Range')
ax[1, 0].set_xlabel('Humidity Range')
ax[1, 0].set_ylabel('Number of Bike Users')
ax[1, 0].tick_params(axis='x', rotation=45)

# Bar plot for correlation matrix values (as a proxy to heatmap)
correlation_matrix = day_df[['temp', 'hum', 'count']].corr()
corr_data = correlation_matrix.stack().reset_index()
corr_data.columns = ['Variable 1', 'Variable 2', 'Correlation']
sns.barplot(x='Variable 1', y='Correlation', hue='Variable 2', data=corr_data, ax=ax[1, 1], palette=palette)
ax[1, 1].set_title('Correlation between Variables')
ax[1, 1].set_xlabel('Variable 1')
ax[1, 1].set_ylabel('Correlation')
ax[1, 1].tick_params(axis='x', rotation=45)

# Adjust layout for better spacing
plt.tight_layout()
plt.show()

"""**2. How do Casual and Registered users use bikes on working days, holidays, and weekdays?**"""

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 10))

# Blue color
blue_color = "#1f77b4"

# Based on working day
sns.barplot(
    x='workingday',
    y='count',
    data=day_df,
    ax=axes[0],
    color=blue_color)
axes[0].set_title('Number of Bike Users Based on Working Days')
axes[0].set_xlabel('Working Day')
axes[0].set_ylabel('Number of Bike Users')

# Based on holidays
sns.barplot(
    x='holiday',
    y='count',
    data=day_df,
    ax=axes[1],
    color=blue_color)
axes[1].set_title('Number of Bike Users Based on Holidays')
axes[1].set_xlabel('Holiday')
axes[1].set_ylabel('Number of Bike Users')

# Based on weekdays
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
plt.show()

"""**3. What are the yearly trends in bike usage, and is 2011 or 2012 more popular?**




"""

# Mengatur bulan sebagai kategori terurut
day_df['month'] = pd.Categorical(day_df['month'], categories=[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    ordered=True)

# Mengelompokkan data berdasarkan bulan dan tahun
monthly_counts = day_df.groupby(by=["month", "year"]).agg({
    "count": "sum"
}).reset_index()

# Mengubah nilai year 0 dan 1 menjadi tahun yang lebih jelas
monthly_counts['year'] = monthly_counts['year'].replace({0: '2011', 1: '2012'})

# Membuat figure untuk visualisasi
plt.figure(figsize=(15, 8))

# Membuat horizontal bar chart dengan palette warna berbeda untuk tahun 2011 dan 2012
sns.barplot(
    data=monthly_counts,
    x="count",
    y="month",
    hue="year",
    palette={"2011": "#A3C9D1", "2012": "#1f77b4"},  # Biru muda untuk 2011, biru tua untuk 2012
    orient='h'  # Mengatur orientasi menjadi horizontal
)

# Menambahkan elemen visual
plt.title("Total Number of Bikes Rented by Month and Year", fontsize=16)
plt.xlabel("Total Rentals", fontsize=12)
plt.ylabel("Month", fontsize=12)
plt.legend(title="Year", loc="upper right", fontsize=10, title_fontsize=12)
plt.tight_layout()

# Menampilkan grafik
plt.show()

"""## Insight
---
1. Weather Conditions and Bike Usage. Users tend to rent more bikes in moderate weather conditions, with clear skies contributing to higher rental numbers.

2. Temperature vs Bike User. As temperature increases, bike usage shows a slight uptick, with peak usage in mid-range temperatures.

3. Humidity vs Bike Usage. Humidity has a negative correlation with bike rentals, where higher humidity leads to fewer users.

4. Correlation between Variables. Temperature and humidity exhibit a mild negative correlation with bike usage, while temperature and bike usage are more positively correlated.

5. Working Day Impact. Bike usage is slightly higher on working days, reflecting commuting patterns and increased activity during weekdays.

6. Holiday Bike Usage. Bike rentals drop during holidays, possibly due to fewer people commuting or leisure activities influencing rental patterns.

7. Weekday Patterns. Bike usage peaks during weekdays, especially on Monday to Friday, aligning with typical workweek commuting habits.

8. Monthly Rental Trends. Rentals are higher during warmer months, with December and January showing a significant decrease in bike usage.

# **Conclusion**
1. Do weather, temperature, and humidity affect the number of bike users?
Conclusion for question number 1: The Impact of Weather, Temperature, and Humidity on Bike  significantly influence bike usage. Clear weather encourages more cycling, while adverse conditions like rain reduce usage. Moderate temperatures increase bike users, as extreme heat or cold deters them. High humidity negatively impacts biking, with fewer users compared to comfortable, low-humidity conditions. Correlation analysis confirms these findings, showing a positive relationship between temperature and bike usage, and a negative one with humidity. These insights highlight the importance of favorable weather and environmental comfort in promoting cycling, offering valuable guidance for city planners and bike-sharing programs to optimize biking during ideal conditions.


2. How do Casual and Registered users use bikes on working days, holidays, and weekdays?
Conclusion for number 2: Bike Usage by Casual and registered users exhibit distinct bike usage patterns. On working days, registered users dominate, reflecting their reliance on bikes for commuting. Casual users, however, contribute less, likely favoring recreational activities. Conversely, holidays see a surge in casual users, highlighting leisure-focused usage, while registered users decrease their activity. Across weekdays, registered users maintain high usage from Monday to Friday, peaking during workdays, while casual users prefer weekends for biking. These patterns emphasize the functional role of bikes for registered users and a recreational role for casual users, providing valuable insights for targeted bike-sharing strategies and infrastructure planning.


3. What are the yearly trends in bike usage, and is 2011 or 2012 more popular?
Conclusion for number 3: Bike usage shows clear yearly and seasonal trends. Rentals in 2012 were significantly higher than in 2011, reflecting growing popularity. Monthly trends reveal peaks during summer and early fall (June to September), driven by favorable weather and outdoor activities, while winter months (December to February) see a decline. The consistent rise in 2012 suggests increased adoption of bike-sharing services or improved infrastructure. These findings emphasize the seasonal nature of biking and highlight 2012 as the more popular year for bike rentals, offering valuable insights for planning and promoting biking initiatives during peak periods.
"""