import requests


# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"url": 'https%3A%2F%2Fwww.popsci.com%2Fscience%2Fomicron-coronavirus-variant%2F'}, json={"query": "helloooo"}) ##emulates HTTP get request
#print(get_response.text)
print(get_response.json())



