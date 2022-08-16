# My first attempt at calling APIs! Currently, this can take input of the few hardcoded classes in my schedule and a couple of dorms and other buildings.
# This only supports point to point currently.
# This will eventually export data in some form, currently, it only exports the addresses and then the distance and walking time.
# bunch of imports
import requests
from datetime import datetime
import time
import googlemaps
import os
import LocationData

def distances():
    origin = input("Enter class/dorm/building you are departing from: ").lower()
    destination = input("Enter class/dorm/building you are going to: ").lower()
    if origin in LocationData.Dorms:
        origin_address = LocationData.Dorms.get(origin)
    elif origin in LocationData.cs:
        origin_address = LocationData.cs.get(origin)
    elif origin in LocationData.dtc:
        origin_address = LocationData.dtc.get(origin)
    elif origin in LocationData.math:
        origin_address = LocationData.math.get(origin)
    elif origin in LocationData.ea:
        origin_address = LocationData.ea.get(origin)
    elif origin in LocationData.other:
        origin_address = LocationData.other.get(origin)


    if destination in LocationData.Dorms:
        destination_address = LocationData.Dorms.get(destination)
    elif destination in LocationData.cs:
        destination_address = LocationData.cs.get(destination)
    elif destination in LocationData.dtc:
        destination_address = LocationData.dtc.get(destination)
    elif destination in LocationData.math:
        destination_address = LocationData.math.get(destination)
    elif destination in LocationData.ea:
        destination_address = LocationData.ea.get(destination)
    elif destination in LocationData.other:
        destination_address = LocationData.other.get(destination)
    # Continue doing this elif stuff, find a way to do it better later

    api_key = os.environ.get('GMaps_API_KEY')
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + origin_address + '&destinations=2145%' + destination_address + '&units=imperial&mode=walking&key=' + api_key

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
distances()