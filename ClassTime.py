# My first attempt at calling APIs!
import requests
url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key=AIzaSyBImgfFw09uTSDp_KhP7egw5zAym8Ah3ks"

payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)