import urllib.request, urllib.response, urllib.error
import json

service_url = "https://maps.googleapis.com/maps/api/geocode/json?key=<MAPS_API_KEY>&"

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    url = service_url + urllib.parse.urlencode({"address": address})

    print("Retrieving :{}".format(url))

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved {} characters".format(len(data)))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("=== Failure to Retrieve ===")
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lon = js["results"][0]["geometry"]["location"]["lng"]

    print("lat: {}, lon: {}".format(lat, lon))
    location = js["results"][0]["formatted_address"]
    print(location)
