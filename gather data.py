import requests
import urllib.parse
import cdsapi
from datetime import date, datetime,timedelta

today = date.today()
yesterday = date.today() - timedelta(days=1)


address = 'Rotterdam'
scope = 0.1
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
response = requests.get(url).json()

area_of_interest = [float(response[0]["lat"])+scope, float(response[0]["lon"])-1.5*scope,
                    float(response[0]["lat"])-scope ,float(response[0]["lon"])+1.5*scope]


c = cdsapi.Client()
try:
    date = '{}/{}'.format(today,today)
    c.retrieve(
        'cams-europe-air-quality-forecasts',
        {
            'variable': [
                'alder_pollen', 'birch_pollen', 'dust',
                'grass_pollen', 'mugwort_pollen', 'non_methane_vocs',
                'olive_pollen', 'ozone', 'particulate_matter_10um',
                'ragweed_pollen',
            ],
            'model': 'ensemble',
            'level': '0',
            'date': '2021-06-17/2021-06-19',
            'type': 'forecast',
            'time': '00:00',
            'leadtime_hour': [
                '0', '12', '24',
                '4', '8',
            ],
            'area': area_of_interest,
            'format': 'netcdf',
        },
        'download.nc')
except:
    date = '{}/{}'.format(yesterday,yesterday)
    c.retrieve(
        'cams-europe-air-quality-forecasts',
        {
            'variable': [
                'alder_pollen', 'birch_pollen', 'dust',
                'grass_pollen', 'mugwort_pollen', 'non_methane_vocs',
                'olive_pollen', 'ozone', 'particulate_matter_10um',
                'ragweed_pollen',
            ],
            'model': 'ensemble',
            'level': '0',
            'date': '2021-06-17/2021-06-19',
            'type': 'forecast',
            'time': '00:00',
            'leadtime_hour': [
                '0', '12', '24',
                '4', '8',
            ],
            'area': area_of_interest,
            'format': 'netcdf',
        },
        'download.nc')

