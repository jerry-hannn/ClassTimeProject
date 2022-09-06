# My first attempt at calling APIs!
# This now supports going to multiple locations in a row. 
# This will eventually export data in some form, currently, it only exports the addresses and then the distance and walking time.

# bunch of imports
from locale import setlocale #not strictly necessary for this
import requests
from datetime import datetime #not stricly necessary for this.
import time #hopefully trying to get this to output something more useful with this, not stricly necessary for this version
import googlemaps #API for distance and time
import os #for env variable
import LocationData #database

#some vars for later
destinationList = []
origin_address = None
destination_address = None

#sets location to something in the database
#would like to make this less hardcoded soon.
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

#api call and strip down JSON
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

#this takes input until done is typed
def takeInput():
    while True:
        next = input("Enter your first location, next location, or type Done:")
        if next.lower() == "done":
            break
        else:
            destinationList.append(next.lower())

#main code run starts here
takeInput()
for i in range(len(destinationList) - 1):
    origin_address = setLocation(destinationList[i])
    destination_address = setLocation(destinationList[i + 1])
    distances()