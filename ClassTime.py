# My first attempt at calling APIs!
# bunch of imports
import requests
from datetime import datetime
import time
import googlemaps
import os
import config


api_key = os.environ.get('GMaps_API_KEY')

url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=South%Mid%Quads&destinations=2145%Technological%Institute&units=imperial&mode=walking&key=' + api_key

response = requests.request("GET", url)

split = response.text.splitlines()
for line in split:
    stripped = line.strip()
    if stripped.startswith('"origin_addresses"'):
        print("From " + stripped[24:len(stripped) - 4])
    if stripped.startswith('"destination_addresses"'):
        print("To " + stripped[29:len(stripped) - 4])
    if stripped.startswith('"text"'):
        print (stripped[10:len(stripped) - 2])
#print(response.text)