import requests
import urllib3
import time
import datetime
import json


#Using Amdoren API

api_key = dRCi5M3LNtMbrPgqUwyangqG3DRbKF

base_url = https://www.amdoren.com/api/

api_url = https://www.amdoren.com/api/timezone.php?api_key=dRCi5M3LNtMbrPgqUwyangqG3DRbKF


def check_time_zone(location):
    call_url = api_url + '&loc' + location

    response = requests.get(call_url)
    print(response.status_code)
    return response.json()


def get_all_locations():
    call_url = base_url + 'locations.php?api_key=' + api_key

    response = requests.get(call_url)
    print(response.status_code)
    return response.json()