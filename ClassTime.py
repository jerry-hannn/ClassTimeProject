# My first attempt at calling APIs! Currently, this can take input of the few hardcoded classes in my schedule and a couple of dorms and other buildings.
# This only supports point to point currently.
# This will eventually export data in some form, currently, it only exports the addresses and then the distance and walking time.
# bunch of imports
from locale import setlocale
import requests
from datetime import datetime
import time
import googlemaps
import os
import LocationData

def setLocation(location):
    if location in LocationData.Dorms:
        location_address = LocationData.Dorms.get(location)
    elif location in LocationData.cs:
        location_address = LocationData.cs.get(location)
    elif location in LocationData.dtc:
        origin_address = LocationData.dtc.get(location)
    elif location in LocationData.math:
        location_address = LocationData.math.get(location)
    elif location in LocationData.ea:
        location_address = LocationData.ea.get(location)
    elif location in LocationData.other:
        location_address = LocationData.other.get(location)
    return location_address

def distances():

    api_key = os.environ.get('GMaps_API_KEY')
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + origin_address + '&destinations=' + destination_address + '&units=imperial&mode=walking&key=' + api_key

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
origin_address = setLocation(input("Enter class/dorm/building you are departing from: ").lower())
destination_address = setLocation(input("Enter class/dorm/building you are going to: ").lower())
distances()