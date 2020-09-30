import requests

payload = {'key1': 'v1', 'key2': 'v2'}

r = requests.get('http://httpbin.org/get', params=payload)
print(r.status_code)
print(r.text)
print(r.json())

print('###############################################')
r = requests.post('http://httpbin.org/post', data=payload)
print(r.status_code)
print(r.text)
print(r.json())

print('###############################################')
r = requests.put('http://httpbin.org/put', data=payload)
print(r.status_code)
print(r.text)
print(r.json())

print('###############################################')
r = requests.delete('http://httpbin.org/delete', data=payload)
print(r.status_code)
print(r.text)
print(r.json())
