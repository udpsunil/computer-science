import urllib.request, urllib.response, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = "http://py4e-data.dr-chuck.net/json?key=42&"

address = input("Enter location: ")

url = service_url + urllib.parse.urlencode({"address": address})

print("Retrieving :{}".format(url))

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved {} characters".format(len(data)))
data = json.loads(data)


print(data["results"][0]['place_id'])

