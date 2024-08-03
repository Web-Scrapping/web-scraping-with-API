'''
    This project analyses weather data scraped from openweathermap.org
    we use the OpenWeatherMap API to scrap 5 day weather forecast
'''

import requests
import datetime
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Define and extract data
api_key = '<>'
city = 'Boston'
base_url = 'http://api.openweathermap.org/data/2.5/forecast'
url = f"{base_url}?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit(1)

# Save raw data
try:
    with open('../data/raw-data.json', 'w') as file:
        json.dump(data, file, indent=4)
except IOError as e:
    print(f"Error writing raw data to file: {e}")
    exit(1)

# Extract data
weather_data = []
try:
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
except KeyError as e:
    print(f"Key error while extracting data: {e}")
    exit(1)

# Convert data to dataframe
try:
    df = pd.DataFrame(weather_data)
except ValueError as e:
    print(f"Error creating DataFrame: {e}")
    exit(1)

# Save data as a CSV file
try:
    df.to_csv('../data/data-extract.csv', index=False)
except IOError as e:
    print(f"Error writing data to CSV file: {e}")
    exit(1)

# Verify and clean data
print(df.info())
print(df.describe())

# Visualize data

# Line plot of temperature over time
try:
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
    plt.savefig('../figures/temperature.jpg')
    plt.show()
except Exception as e:
    print(f"Error during temperature plot generation: {e}")
    exit(1)

# Line plot of humidity over time
try:
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
    plt.savefig('../figures/humidity.jpg')
    plt.show()
except Exception as e:
    print(f"Error during humidity plot generation: {e}")
    exit(1)

# Scatter plot of temperature vs. humidity
try:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='Temperature', y='Humidity')
    plt.title('Temperature vs Humidity')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Humidity (%)')
    plt.savefig('../figures/temperature-vs-humidity.jpg')
    plt.show()
except Exception as e:
    print(f"Error during scatter plot generation: {e}")
    exit(1)

# Box plot to show the distribution of temperatures
try:
    sns.boxplot(data=df, x='Temperature')
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.savefig('../figures/temperature-distribution.jpg')
    plt.show()
except Exception as e:
    print(f"Error during temperature distribution plot generation: {e}")
    exit(1)

# Box plot to show the distribution of humidity
try:
    sns.boxplot(data=df, x='Humidity')
    plt.title('Humidity Distribution')
    plt.xlabel('Humidity (%)')
    plt.savefig('../figures/humidity-distribution.jpg')
    plt.show()
except Exception as e:
    print(f"Error during humidity distribution plot generation: {e}")
    exit(1)
