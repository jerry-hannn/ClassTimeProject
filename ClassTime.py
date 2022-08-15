# My first attempt at calling APIs!
# bunch of imports
import requests
from datetime import datetime
import time
import googlemaps
import os
import LocationData

def distances():
    origin = input("Enter class/dorm you are departing from: ")
    destination = input("Enter class/dorm you are going to: ")
    if origin in LocationData.Dorms:
        origin_address = LocationData.Dorms.get(origin)
    elif origin in LocationData.cs:
        origin_address = LocationData.cs.get(origin)
    elif origin in LocationData.dtc:
        origin_address = LocationData.dtc.get(origin)
    # Continue doing this elif stuff, find a way to do it better later

    api_key = os.environ.get('GMaps_API_KEY')
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=South%Mid%Quads&destinations=2145%Technological%Institute&units=imperial&mode=walking&key=' + api_key

    response = requests.request("GET", url)

    split = response.text.splitlines()
    for line in split:
        stripped = line.strip()
        if stripped.startswith('"origin_addresses"'):
            print("From " + stripped[24:len(stripped) - 4])
        elif stripped.startswith('"destination_addresses"'):
            print("To " + stripped[29:len(stripped) - 4])
        elif stripped.startswith('"text"'):
            print (stripped[10:len(stripped) - 2])
#print(response.text)