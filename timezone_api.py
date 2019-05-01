import requests
import urllib3
import time
from datetime import datetime
import json


#Using Amdoren API

api_key = 'dRCi5M3LNtMbrPgqUwyangqG3DRbKF'

base_url = 'https://www.amdoren.com/api/'

timezone_url = 'https://www.amdoren.com/api/timezone.php?api_key=dRCi5M3LNtMbrPgqUwyangqG3DRbKF'


def check_time_zone(location):
    call_url = timezone_url + '&loc=' + location

    time_string = requests.get(call_url).json()['time']

    timestamp = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")

    return timestamp.hour

def get_all_locations():
    call_url = base_url + 'locations.php?api_key=' + api_key

    response = requests.get(call_url)
    print(response.status_code)
    return response.json()