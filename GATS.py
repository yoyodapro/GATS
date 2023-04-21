import datetime
from astral.sun import sun
from astral import LocationInfo
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from typing import Tuple
from requests import get

def get_current_utc() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)

def get_location() -> Tuple[float, float]:
    try:
        ip = get('https://api.ipify.org').text
        coordinates = get(f'https://ipapi.co/{ip}/latlong/').text
        lat, lon = map(float, coordinates.strip().split(','))
        return lat, lon
    except (GeocoderTimedOut, ValueError):
        return 0.0, 0.0

def solar_noon(lat: float, lon: float, date: datetime.date) -> datetime.datetime:
    location = LocationInfo(lat, lon)
    s = sun(location.observer, date=date)
    return s['noon']

def local_mean_time(utc_time: datetime.datetime, lat: float, lon: float) -> datetime.datetime:
    solar_noon_date = solar_noon(lat, lon, utc_time.date())
    time_difference = utc_time - solar_noon_date
    return utc_time + time_difference

def gats_time() -> datetime.datetime:
    lat, lon = get_location()
    utc_time = get_current_utc()
    local_time = local_mean_time(utc_time, lat, lon)
    return local_time

if __name__ == "__main__":
    local_time = gats_time()
    print(f"Local GATS Time: {local_time}")
