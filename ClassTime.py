# My first attempt at calling APIs!
import requests
from datetime import datetime
import time
import googlemaps

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=South%Mid%Quads&destinations=2145%Technological%Institute&units=imperial&mode=walking&key=AIzaSyBImgfFw09uTSDp_KhP7egw5zAym8Ah3ks"

payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)