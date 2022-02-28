import requests

api_url = 'http://numbersapi.com/{}/math?json=true' 
with open('dataset_24476_3.txt', 'r') as ouf:
    for line in ouf:
        link = api_url.format(line.strip())
        result = requests.get(link)
        print(result.json())
