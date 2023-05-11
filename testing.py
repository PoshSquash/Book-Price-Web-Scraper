import requests
import time

# Test the request.
time.sleep(0.8)
url = 'http://127.0.0.1:5000/price'
name = 'Redwall'
r = requests.get(url, params={'name': name})
print(r)
print(r.text)