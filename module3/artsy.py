import requests
import json

token = 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MjFiY2RiZmNjYmJjNzAwMGQ2ZTU5NTgiLCJleHAiOjE2NDY2NDA0NjAsImlhdCI6MTY0NjAzNTY2MCwiYXVkIjoiNjIxYmNkYmZjY2JiYzcwMDBkNmU1OTU4IiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYyMWM4MmNjZmQzYjQ5MDAwYzY1YjgwZSJ9.KyBWjo5H_75Rmd3hOh9WDm0o0VeM1cl83rH3RCPYZOs'
headers = {"X-Xapp-Token" : token}
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)
j = json.loads(r.text)