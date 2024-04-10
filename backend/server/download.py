import requests
from datetime import datetime, timedelta


def fetch_hourly_temperature(url, start_datetime_str, end_datetime_str):
    start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%dT%H:%M:%SZ")
    end_datetime = datetime.strptime(end_datetime_str, "%Y-%m-%dT%H:%M:%SZ")

    current_datetime = start_datetime
    while current_datetime <= end_datetime:
        params = {
            "coords": "POINT(17.1785 48.1628)",
            "crs": "CRS:84",
            "within": "2",
            "within-units": "km",
            "datetime": current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()

        else:
            print(f"Error fetching data for {current_datetime}: {response.status_code} - {response.reason}")
        current_datetime += timedelta(hours=1)


# Example usage with your specified date range
url = "https://climathon.iblsoft.com/data/netatmo/edr/collections/publicdata/radius"
fetch_hourly_temperature(url, "2023-10-05T06:20:00Z", "2023-10-15T06:20:00Z")
