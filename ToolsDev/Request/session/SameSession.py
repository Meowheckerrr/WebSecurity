#CTF 
import requests

url ="http://lotuxctf.com:20001/r3que57s_ch4ll3nge"

session = requests.Session()
response = session.get(url)

# print("Request Headers:")
# for key, value in response.request.headers.items():
#     print(f"{key}: {value}")
# print("="*40)

print("===Response-1 Headers===")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print(f'HTTP Response: {response.text}')

print("="*40)


#Request2 (In Same Connection)

url2 ="http://lotuxctf.com:20001/r3que57s_ch4ll3nge" #Target URL 

response2 = session.post(url)
print("===Request-2 Headers===")
for key, value in response2.request.headers.items():
    print(f"{key}: {value}")

print("="*40)

print("===Response-2 Headers===")
for key, value in response2.headers.items():
    print(f"{key}: {value}")
print(f'HTTP Response: {response2.text}')
session.close()
