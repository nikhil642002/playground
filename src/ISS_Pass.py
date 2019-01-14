import geocoder
import datetime
import json
import requests

# http://open-notify.org/Open-Notify-API/ISS-Pass-Times/

g = geocoder.ip('me') # IP based location data
n = 5
result = requests.get("http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}".format(g.lat, g.lng, n))
json_pass_dates = json.loads(result.content)
print("Next {} passes of the ISS at this location ({}, {}) are:\n".format(n, g.lat, g.lng))
for response in json_pass_dates["response"]:
    print("Date: {}, Duration,: {} mins".format(datetime.datetime.fromtimestamp(response["risetime"]), response["duration"]))



