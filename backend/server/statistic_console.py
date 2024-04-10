import sqlite3
import pandas as pd

# Path to your database file
db_path = 'weather_data_2.db'


def getAllStatisticAvg():
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Convert the 'station_measurements' table to a DataFrame
    query = "SELECT * FROM station_measurements;"
    df = pd.read_sql_query(query, conn)

    # Close the connection to the database
    conn.close()

    # Calculate average temperature, humidity, and pressure
    avg_temperature = df['temperature'].mean()
    avg_humidity = df['humidity'].mean()
    avg_pressure = df['pressure'].mean()

    # Find the maximum gust strength and its angle
    max_gust_strength = df['gust_strength'].max()
    max_gust_angle = df.loc[df['gust_strength'].idxmax(), 'gust_angle']

    # Count the number of measurements per country
    measurements_per_country = df['country'].value_counts().to_dict()

    # Print the statistics
    print(f"Average Temperature: {avg_temperature:.2f}°C")
    print(f"Average Humidity: {avg_humidity:.2f}%")
    print(f"Average Pressure: {avg_pressure:.2f} hPa")
    print(f"Maximum Gust Strength: {max_gust_strength} with Angle: {max_gust_angle} degrees")
    print("Measurements Per Country:", measurements_per_country)


def getMonthlyStatisticAvg():
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Convert the 'station_measurements' table to a DataFrame
    query = "SELECT * FROM station_measurements;"
    df = pd.read_sql_query(query, conn)

    # Close the connection to the database
    conn.close()

    # Convert 'time_of_measurement' to datetime
    df['time_of_measurement'] = pd.to_datetime(df['time_of_measurement'])

    # Extract year and month from 'time_of_measurement'
    df['year_month'] = df['time_of_measurement'].dt.to_period('M')

    # Initialize a dictionary to store the statistics by year and month
    stats_by_year_month = {}

    # Iterate through each year and month in the data
    for period in df['year_month'].unique():
        period_data = df[df['year_month'] == period]

        # Calculate statistics for this period
        avg_temperature = period_data['temperature'].mean()
        avg_humidity = period_data['humidity'].mean()
        avg_pressure = period_data['pressure'].mean()
        max_gust_strength = period_data['gust_strength'].max()
        max_gust_angle = period_data.loc[period_data['gust_strength'].idxmax(), 'gust_angle']

        # Store the statistics in the dictionary
        stats_by_year_month[str(period)] = {
            'Average Temperature': avg_temperature,
            'Average Humidity': avg_humidity,
            'Average Pressure': avg_pressure,
            'Maximum Gust Strength': max_gust_strength,
            'Maximum Gust Angle': max_gust_angle
        }

    # Print the statistics by year and month
    for year_month, stats in stats_by_year_month.items():
        print(f"Year and Month: {year_month}")
        for stat_name, value in stats.items():
            print(f"{stat_name}: {value:.4f}")
        print("----------")

def print_extreme_weather_days(df):
    # Define the metrics to examine
    metrics = ['temperature', 'pressure', 'humidity']

    # Loop through each metric to find and print the days with the highest and lowest values
    for metric in metrics:
        # Find the row with the highest value for the current metric
        max_row = df.loc[df[metric].idxmax()]

        # Find the row with the lowest value for the current metric
        min_row = df.loc[df[metric].idxmin()]

        # Print the dates and values for the highest and lowest
        print(f"Highest {metric.capitalize()}: {max_row[metric]} on {max_row['time_of_measurement']}")
        print(f"Location: {max_row['city']}, {max_row['country']}")
        print(f"Lowest {metric.capitalize()}: {min_row[metric]} on {min_row['time_of_measurement']}")
        print(f"Location: {min_row['city']}, {min_row['country']}")
        print("----------")




conn = sqlite3.connect(db_path)

    # Convert the 'station_measurements' table to a DataFrame
query = "SELECT * FROM station_measurements;"
df = pd.read_sql_query(query, conn)


# getMonthlyStatisticAvg()
# print("==========")
# getAllStatisticAvg()
# print("==========")
# print_extreme_weather_days(df)

