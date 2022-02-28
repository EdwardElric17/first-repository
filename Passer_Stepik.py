import requests
import re

# a = str(input())
# b = str(input())

res = requests.get('https://python-scripts.com/requests')
print(res.status_code)
# if res.status_code == 200:
#     a_html = res.text
# for line in a_html:
#     print(line)
    # link = re.search(r'', line)