import urllib.request, urllib.response, urllib.error
import xml.etree.ElementTree as ET

service_url = input("Enter location: ")

uh = urllib.request.urlopen(service_url)

data = uh.read()
print("Retrieved {} characters".format(len(data)))

xml_tree = ET.fromstring(data)

results = xml_tree.findall('.//comment')
count_list = [int(result.find('count').text) for result in results]
print('Count: {}'.format(len(count_list)))
print('Sum: {}'.format(sum(count_list)))
