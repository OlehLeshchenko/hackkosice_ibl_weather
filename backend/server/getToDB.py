import sqlite3

import requests
from datetime import datetime, timedelta

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('weather_data_2.db')
c = conn.cursor()

# Create a simplified table
c.execute('''CREATE TABLE IF NOT EXISTS station_measurements
             (station_id TEXT,
              city TEXT,
              country TEXT,
              latitude REAL,
              longitude REAL,
              humidity REAL,
              pressure REAL,
              temperature REAL,
              wind_angle REAL,
              wind_strength REAL,
              gust_angle REAL,
              gust_strength REAL,
              time_of_measurement TEXT)''')



def fetch_hourly_temperature(url, start_datetime_str, end_datetime_str):
    start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%dT%H:%M:%SZ")
    end_datetime = datetime.strptime(end_datetime_str, "%Y-%m-%dT%H:%M:%SZ")

    current_datetime = start_datetime
    current_datetime += timedelta(hours=6)
    i = 1
    while current_datetime <= end_datetime:
        params = {
            "coords": "POINT(17.1785 48.1628)",
            "crs": "CRS:84",
            "within": "1000",
            "within-units": "km",
            "datetime": current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"Record {i}")
            i += 1
            for feature in data['features']:
                station_id = feature['properties']['station_id']
                place = feature['properties']['place']
                measures = feature['properties']['measures']

                # Extract measurement values, using None for missing measures to handle optional data
                humidity = measures.get('humidity', {}).get('value')
                pressure = measures.get('pressure', {}).get('value')
                temperature = measures.get('temperature', {}).get('value')
                wind_angle = measures.get('wind_angle', {}).get('value')
                wind_strength = measures.get('wind_strength', {}).get('value')
                gust_angle = measures.get('gust_angle', {}).get('value')
                gust_strength = measures.get('gust_strength', {}).get('value')
                # Assuming all measures have the same time for simplicity; adjust as needed
                time_of_measurement = measures.get('humidity', {}).get('time_of_measurement')

                # Insert data into the table
                c.execute('''INSERT OR REPLACE INTO station_measurements
                             (station_id, city, country, latitude, longitude, humidity, pressure, temperature,wind_angle,wind_strength, gust_angle, gust_strength, time_of_measurement)
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                          (station_id, place['city'], place['country'], place['location'][1], place['location'][0],
                           humidity, pressure, temperature,wind_angle, wind_strength, gust_angle, gust_strength, time_of_measurement))
                conn.commit()

        else:
            print(f"Error fetching data for {current_datetime}: {response.status_code} - {response.reason}")
        current_datetime += timedelta(hours=24)
    conn.close()


url = "https://climathon.iblsoft.com/data/netatmo/edr/collections/publicdata/radius"
fetch_hourly_temperature(url, "2023-10-01T06:20:00Z", "2024-03-15T06:20:00Z")










# Commit changes and close the connection

