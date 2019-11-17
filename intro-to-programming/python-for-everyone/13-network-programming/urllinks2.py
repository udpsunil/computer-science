import urllib.request, urllib.response, urllib.error
from bs4 import BeautifulSoup


def follow_index(url, follow):
    follow -= 1
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup("a")
    for index, tag in enumerate(tags):
        if index == follow:
            return tag.get("href", None)


url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))
print('Retrieving: {}'.format(url))
for _ in range(count):
    final_url = follow_index(url, position)
    print('Retrieving: {}'.format(final_url))
    url = final_url

