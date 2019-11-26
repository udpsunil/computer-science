import urllib.request, urllib.response, urllib.error
import json

service_url = input("Enter location: ")

uh = urllib.request.urlopen(service_url)

data = uh.read()
print("Retrieved {} characters".format(len(data)))

data = json.loads(data)

count_list = [int(result['count']) for result in data['comments']]
print('Count: {}'.format(len(count_list)))
print('Sum: {}'.format(sum(count_list)))
