import re

import requests


first_link = input()
second_link = input()
request_link = requests.get(first_link).text
pattern = r"href=\"([\w\:\/\.]+)"
search = re.findall(pattern, request_link)
inner_links = []
for link in search:
    get_link = requests.get(link).text.strip()
    inner_links += re.findall(pattern, get_link.replace('stepic.org', 'stepik.org'))

if second_link in inner_links:
    print('Yes')
else:
    print('No')
