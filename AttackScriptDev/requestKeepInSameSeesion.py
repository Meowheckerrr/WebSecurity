#CTF 
import requests

url ="http://lotuxctf.com:20001/r3que57s_ch4ll3nge"

session = requests.Session()

response = session.get(url)

print("Request Headers:")
for key, value in response.request.headers.items():
    print(f"{key}: {value}")

print("="*40)


for key, value in response.headers.items():
    print(f"{key}: {value}")
print(response.text)


#Request2 Post 
print("/"*40)

url2 ="http://lotuxctf.com:20001/r3que57s_ch4ll3nge"

response2 = session.post(url)


print("Request2 Headers:")
for key, value in response2.request.headers.items():
    print(f"{key}: {value}")

print("="*40)


for key, value in response2.headers.items():
    print(f"{key}: {value}")
print(response2.text)

session.close()
