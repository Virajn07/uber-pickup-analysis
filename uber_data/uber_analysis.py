# STEP 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

# STEP 2: Load and combine all CSVs (set your own path)
folder_path = ""  # 👈 Replace with your extracted ZIP folder path
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Combine all monthly CSV files
df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)

# STEP 3: Basic info
print("Shape of dataset:", df.shape)
print("Columns:", df.columns)
print(df.head())

# STEP 4: Convert Date/Time column and create new features
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Hour'] = df['Date/Time'].dt.hour
df['Day'] = df['Date/Time'].dt.day
df['Weekday'] = df['Date/Time'].dt.weekday
df['Month'] = df['Date/Time'].dt.month
df['Date'] = df['Date/Time'].dt.date

# STEP 5: Hourly Pickups
plt.figure(figsize=(10,5))
df['Hour'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("Uber Pickups by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Pickups")
plt.grid(True)
plt.show()

# STEP 6: Weekday Pickups
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.figure(figsize=(10,5))
sns.countplot(x='Weekday', data=df)
plt.xticks(ticks=range(7), labels=days)
plt.title("Uber Pickups by Weekday")
plt.show()

# STEP 7: Monthly Pickups
plt.figure(figsize=(10,5))
df['Month'].value_counts().sort_index().plot(kind='bar', color='orange')
plt.title("Uber Pickups by Month")
plt.xlabel("Month")
plt.ylabel("Number of Pickups")
plt.show()

# STEP 8: Time Series of Daily Pickups
df_ts = df.groupby('Date').size()
plt.figure(figsize=(14,6))
df_ts.plot()
plt.title("Uber Pickups per Day")
plt.xlabel("Date")
plt.ylabel("Number of Pickups")
plt.grid(True)
plt.show()

# STEP 9: Scatter of Pickup Locations
plt.figure(figsize=(10,8))
plt.scatter(df['Lon'], df['Lat'], s=1, alpha=0.4)
plt.title("Uber Pickups Location Scatter (NYC Area)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()

# STEP 10: Base analysis (optional)
plt.figure(figsize=(10,5))
sns.countplot(x='Base', data=df)
plt.title("Uber Pickups by Base")
plt.xlabel("Base Number")
plt.ylabel("Pickups")
plt.xticks(rotation=45)
plt.show()
