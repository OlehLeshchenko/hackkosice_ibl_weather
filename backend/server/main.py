from datetime import timedelta
from datetime import datetime
import requests
import json


def fetch_and_download():

        # Construct the filename for each iteration

        url = "https://climathon.iblsoft.com/data/netatmo/edr/collections/publicdata/radius"


        start_datetime = datetime.strptime("2023-10-05T06:20:00Z", "%Y-%m-%dT%H:%M:%SZ")
        end_datetime = datetime.strptime("2023-10-15T06:20:00Z", "%Y-%m-%dT%H:%M:%SZ")

        current_datetime = start_datetime
        i = 1
        while current_datetime <= end_datetime:
            print(f"File #{i}")
            filename = f'data/data{i}.json'
            params = {
                "coords": "POINT(17.1785 48.1628)",
                "crs": "CRS:84",
                "within": "50",
                "within-units": "km",
                "datetime": current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                with open(filename, 'w') as file:
                    json.dump(data, file)
                i += 1
            else:
                print(f"Error fetching data for {current_datetime}: {response.status_code} - {response.reason}")
            current_datetime += timedelta(hours=4)






def parse_and_print_temperature():
    for i in range(27):

        filename = f'data/data{i+1}.json'
        with open(filename, 'r') as file:
            data = json.load(file)
            time_of_measurement = data.get('features', [])['properties']['measures'].get('temperature', {}).get('time_of_measurement',
                                                                                                                'N/A')
            print(f"----- Day {time_of_measurement} ------")
            temperature_measurements = data.get('ranges', {}).get('temperature', {}).get('values', [])

            # Access to coordinates and timestamps
            coordinates = data.get('domain', {}).get('axes', {}).get('composite', {}).get('values', [])
            time_stamps = data.get('domain', {}).get('axes', {}).get('t', {}).get('values', [])

            features = data.get('features', [])

            for feature in features:
                # Extracting coordinates
                coordinates = feature['geometry']['coordinates']

                # Extracting temperature measurement
                temperature = feature['properties']['measures'].get('temperature', {}).get('value', 'N/A')

                # Extracting time of temperature measurement
                time_of_measurement = feature['properties']['measures'].get('temperature', {}).get('time_of_measurement',
                                                                                                   'N/A')

                print(f"Coordinates: {coordinates}, Temperature: {temperature}°C, Time of Measurement: {time_of_measurement}")


import json
import pandas as pd


def analyze_weather_data(file_paths):
    """
    Analyzes weather data from JSON files.

    Args:
    - file_paths (list): A list of strings representing paths to JSON files.

    Returns:
    - DataFrame with summary statistics.
    """
    # Initialize a list to hold data from all files
    all_data = []

    # Load and append data from each file
    for path in file_paths:
        with open(path) as file:
            data = json.load(file)["features"]
            all_data.extend(data)

    # Flatten the data
    flattened_data = []
    for feature in all_data:
        feature_data = feature['properties']
        measures_data = feature_data.pop('measures', {})
        for measure_key, measure_val in measures_data.items():
            feature_data[measure_key] = measure_val.get('value')
        flattened_data.append(feature_data)

    # Convert to DataFrame
    df = pd.json_normalize(flattened_data)

    # Calculate summary statistics
    summary_stats = df.describe()

    return summary_stats


def analyze_temperature(file_paths):
    """
    Analyzes temperature data from JSON files.

    Args:
    - file_paths (list): A list of strings representing paths to JSON files.

    Returns:
    - DataFrame with temperature summary statistics.
    """
    # Initialize a list to hold data from all files
    all_data = []

    # Load and append data from each file
    for path in file_paths:
        with open(path) as file:
            data = json.load(file)["features"]
            all_data.extend(data)

    # Extract temperature data
    temperatures = []
    for feature in all_data:
        properties = feature['properties']
        measures = properties.get('measures', {})
        temperature = measures.get('temperature', {}).get('value')
        if temperature is not None:
            temperatures.append(temperature)

    # Convert to DataFrame
    df_temp = pd.DataFrame(temperatures, columns=['Temperature'])

    # Calculate summary statistics
    summary_stats = df_temp.describe()

    return summary_stats


# Example usage
file_paths = [
    'data/data1.json',
    'data/data2.json',
    'data/data3.json',
    'data/data4.json',
    'data/data5.json',
    'data/data6.json',
    'data/data7.json',
    'data/data8.json',
    'data/data9.json',
    'data/data10.json',
    'data/data11.json',
    'data/data12.json',
    'data/data13.json',
    'data/data14.json',
    'data/data15.json',
    'data/data16.json',
    'data/data17.json',
    'data/data18.json',
    'data/data19.json',
    'data/data20.json',
    'data/data21.json',
    'data/data22.json',
    'data/data23.json',
    'data/data24.json',
    'data/data25.json',
    'data/data26.json',
    'data/data27.json',
    # Add all your file paths here
]
summary_statistics = analyze_weather_data(file_paths)
print(summary_statistics)

temperature_statistics = analyze_temperature(file_paths)
print(temperature_statistics)


