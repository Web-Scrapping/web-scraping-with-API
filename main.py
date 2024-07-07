'''
    This project analyses weather data scraped from openweathermap.org
    we use the OpenWeatherMap API to scrap 5 day weather forecast
'''

import requests
import datetime
import pandas as pd
import json
import pprint

# define and extract data
api_key = '{key}'
city = 'Boston'
base_url = 'http://api.openweathermap.org/data/2.5/forecast'
url = f"{base_url}?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

# save raw data
with open('raw-data.json', 'w') as file:
    json.dump(data, file, indent=4)

# extract data
weather_data = []
for entry in data['list']:
    timestamp = entry['dt']
    date = datetime.datetime.fromtimestamp(timestamp)   # convert to readable datetime format
    temperature = entry['main']['temp']
    humidity = entry['main']['humidity']
    description = entry['weather'][0]['description']

    weather_data.append({
        'Datetime': date,
        'Temperature': temperature,
        'Humidity': humidity,
        'Description': description
    })

# convert data to dataframe
df = pd.DataFrame(weather_data)

# save data as a csv file
df.to_csv('data-extract.csv', index=False)

# verify and clean data
print(df.info())
print(df.describe())

# visualise data
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


# Line plot of temperature over time
sns.lineplot(data=df, x='Datetime', y='Temperature', markers='o', ms=2)
plt.title('Temperature Over Time (3-hour step)')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')

# Customize date and time formatting on x-axis
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Show every day
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=3))  # Show every 3 hours as minor ticks
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))  # Date format

plt.xticks(fontsize='small', rotation=45, ha='right', va='top', rotation_mode='anchor')
plt.tight_layout()
plt.savefig('output-figures/temperature.jpg')
plt.show()

# Line plot of humidity over time
sns.lineplot(data=df, x='Datetime', y='Humidity', markers='o', ms=2)
plt.title('Humidity Over Time (3-hour step)')
plt.xlabel('Date and Time')
plt.ylabel('Humidity (%)')

# Customize date and time formatting on x-axis
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Show every day
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=3))  # Show every 3 hours as minor ticks
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))  # Date format

plt.xticks(fontsize='small', rotation=45, ha='right', va='top', rotation_mode='anchor')
plt.tight_layout()
plt.savefig('output-figures/humidity.jpg')
plt.show()

# Scatter plot of temperature vs. humidity
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Temperature', y='Humidity')
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.savefig('output-figures/temperature-vs-humidity.jpg')
plt.show()

# Box plot to show the distribution of temperatures
sns.boxplot(data=df, x='Temperature')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.savefig('output-figures/temperature-distribution.jpg')
plt.show()

# Box plot to show the distribution of humidity
sns.boxplot(data=df, x='Humidity')
plt.title('Humidity Distribution')
plt.xlabel('Humidity (%)')
plt.savefig('output-figures/humidity-distribution.jpg')
plt.show()

