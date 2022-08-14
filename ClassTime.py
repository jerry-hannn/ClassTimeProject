# My first attempt at calling APIs!
import requests
from datetime import datetime
import time
import googlemaps
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('GooogleMapsApiKey')
print(os.environ)
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=South%Mid%Quads&destinations=2145%Technological%Institute&units=imperial&mode=walking&key='# + api_key

payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)