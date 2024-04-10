from fastapi import FastAPI
import sqlite3
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

db_path = 'weather_data_2.db'


allowed_origins = [
    "http://localhost:3000",  # Assuming your frontend runs on this origin
    "http://127.0.0.1:3000"
]

# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Allow specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/statistics/average")
async def get_all_statistic_avg():
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM station_measurements;"
    df = pd.read_sql_query(query, conn)
    conn.close()

    avg_temperature = round(df['temperature'].mean(),2)
    avg_humidity = round(df['humidity'].mean(),2)
    avg_pressure = round(df['pressure'].mean(),2)
    max_gust_strength = df['gust_strength'].max()
    max_gust_angle = df.loc[df['gust_strength'].idxmax(), 'gust_angle']
    measurements_per_country = df['country'].value_counts().to_dict()
    measurements_per_country_text = ", ".join(f"{country}: {count}" for country, count in measurements_per_country.items())

    response = {
        "Average Temperature": avg_temperature,
        "Average Humidity": avg_humidity,
        "Average Pressure": avg_pressure,
        "Maximum Gust Strength": max_gust_strength,
        "Maximum Gust Angle": max_gust_angle,
        "Measurements Per Country": measurements_per_country_text
    }

    print(response)

    # Returning the response. FastAPI automatically converts the dictionary to a JSON response.
    return response

@app.get("/statistics/monthly")
async def get_monthly_statistic_avg():
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM station_measurements;"
    df = pd.read_sql_query(query, conn)
    conn.close()

    df['time_of_measurement'] = pd.to_datetime(df['time_of_measurement'])
    df['year_month'] = df['time_of_measurement'].dt.to_period('M')

    stats_by_year_month = {}
    for period, period_data in df.groupby('year_month'):
        avg_temperature = period_data['temperature'].mean()
        avg_humidity = period_data['humidity'].mean()
        avg_pressure = period_data['pressure'].mean()
        max_gust_strength = period_data['gust_strength'].max()
        max_gust_angle = period_data.loc[period_data['gust_strength'].idxmax(), 'gust_angle']

        stats_by_year_month[str(period)] = {
            'Average Temperature': avg_temperature,
            'Average Humidity': avg_humidity,
            'Average Pressure': avg_pressure,
            'Maximum Gust Strength': max_gust_strength,
            'Maximum Gust Angle': max_gust_angle
        }

    return stats_by_year_month

@app.get("/statistics/extreme-weather")
async def get_extreme_weather_days():
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM station_measurements;"
    df = pd.read_sql_query(query, conn)
    metrics = ['temperature', 'pressure', 'humidity']
    extreme_weather_days = {}

    for metric in metrics:
        max_row = df.loc[df[metric].idxmax()]
        min_row = df.loc[df[metric].idxmin()]

        extreme_weather_days[metric] = {
            "Highest": {"Value": max_row[metric], "Date": max_row['time_of_measurement'],
                        "Location": f"{max_row['city']}, {max_row['country']}"},
            "Lowest": {"Value": min_row[metric], "Date": min_row['time_of_measurement'],
                       "Location": f"{min_row['city']}, {min_row['country']}"}
        }

    return extreme_weather_days

