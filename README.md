# Weather Data Analysis Project

Welcome to the Weather Data Analysis Project! This initiative leverages the OpenWeatherMap API to fetch and analyze a 
5-day weather forecast for a specified city, offering insightful visualizations to understand weather patterns better.

## Project Overview

This project encompasses the following key objectives:
1. **Data Retrieval**: Fetch weather data using the OpenWeatherMap API.
2. **Data Processing**: Clean and process the raw data into a structured format.
3. **Data Storage**: Save the processed data for future analysis.
4. **Data Visualization**: Create visual representations of the weather data to reveal trends and patterns.

## Project Structure

Here's a high-level overview of the project structure:

```
weather-data-analysis/
│
├── data/
│   ├── raw-data.json           # Raw weather data fetched from the API
│   └── data-extract.csv        # Processed weather data in CSV format
│
├── figures/
│   ├── temperature.jpg                 # Line plot of temperature over time
│   ├── humidity.jpg                    # Line plot of humidity over time
│   ├── temperature-vs-humidity.jpg     # Scatter plot of temperature vs. humidity
│   ├── temperature-distribution.jpg    # Box plot of temperature distribution
│   └── humidity-distribution.jpg       # Box plot of humidity distribution
│
├── scripts/
│   └── weather_analysis.py         	# Main script for data fetching, processing, and visualization
│
├── README.md		         # This file, provides an overview and instructions for the project
└── requirements.txt             # List of required packages
```

## File Descriptions

### `weather_analysis.py`

This is the main script driving the project, and it performs several critical functions:

- **Data Retrieval**: Fetches weather data from OpenWeatherMap.
- **Data Storage**: Saves raw JSON data for reference.
- **Data Processing**: Extracts essential fields and transforms them into a pandas DataFrame.
- **Data Storage**: Saves the cleaned data into a CSV file.
- **Data Visualization**: Generates and saves various plots to visually represent the data.
- **Error Handling**: Manages potential errors gracefully, ensuring robust operation.

### `data/`

- `raw-data.json`: This file contains the raw JSON data fetched from the OpenWeatherMap API.
- `data-extract.csv`: This CSV file holds the cleaned and processed weather data.

### `figures/`

This directory contains visualizations generated from the weather data:
- `temperature.jpg`: A line plot showing temperature trends over time.
- `humidity.jpg`: A line plot displaying humidity levels over time.
- `temperature-vs-humidity.jpg`: A scatter plot illustrating the relationship between temperature and humidity.
- `temperature-distribution.jpg`: A box plot depicting the distribution of temperatures.
- `humidity-distribution.jpg`: A box plot illustrating the distribution of humidity levels.

### `requirements.txt`

This file lists the Python libraries required to run the project. Use this file to install dependencies efficiently.

## Detailed Steps

### Data Retrieval

The script begins by constructing the API endpoint URL using the base URL, city name, and API key. It then sends a GET 
request to fetch the weather data.

### Data Storage

The fetched raw data is saved as `raw-data.json` to maintain a record of the unprocessed data.

### Data Processing

The script extracts relevant fields from the JSON data, such as date, temperature, humidity, and weather description. 
This data is then stored in a pandas DataFrame for easy manipulation and analysis.

### Data Storage

The processed DataFrame is saved as `data-extract.csv`, providing a structured dataset for further analysis.

### Data Visualization

The script generates several plots to visualize the weather data:

1. **Line Plot of Temperature Over Time**: Shows temperature changes over the forecast period.
2. **Line Plot of Humidity Over Time**: Displays humidity variations over time.
3. **Scatter Plot of Temperature vs. Humidity**: Illustrates the relationship between temperature and humidity.
4. **Box Plot of Temperature Distribution**: Highlights the spread and central tendency of temperature data.
5. **Box Plot of Humidity Distribution**: Showcases the distribution of humidity levels.

### Error Handling

The script includes robust error handling mechanisms to manage:
- Network issues during data fetching.
- JSON decoding errors.
- File I/O errors during data storage.
- Data extraction issues if the API response structure changes.

## How to Run the Project

### Prerequisites

Ensure you have the following installed:
- The required Python libraries listed in `requirements.txt`.

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/mrowurakwarteng/Web-Scrapping/web-scraping-with-API.git
   cd web-scraping-with-API
   ```

2. **Install the Required Packages**:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Script

1. Open `weather_analysis.py`.
2. Replace the `api_key` variable with your OpenWeatherMap API key.
3. Optionally, change the `city` variable to analyze weather data for a different city.
4. Run the script:

   ```sh
   python weather_analysis.py
   ```

### Error Handling

The script is equipped with comprehensive error handling to ensure smooth execution. Any errors encountered during the 
process will be printed to the console with detailed messages.

## Results

After executing the script, you will find:
- Raw weather data in `data/raw-data.json`.
- Processed weather data in `data/data-extract.csv`.
- Various visualizations in the `figures/` directory.


## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgements

- **OpenWeatherMap**: For providing the weather data API.


---