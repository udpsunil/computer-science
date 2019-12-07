import xml.etree.ElementTree as ET

input_ = """
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>
"""

stuff = ET.fromstring(input_)
lst = stuff.findall('users/user')
print('User Count: {}'.format(len(lst)))

for item in lst:
    print('Name: {}'.format(item.find('name').text))
    print('Id: {}'.format(item.find('id').text))
    print('Attribute: {}'.format(item.get("x")))