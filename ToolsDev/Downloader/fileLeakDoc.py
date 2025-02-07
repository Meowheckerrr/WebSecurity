import requests

def httpGetResponse(url=None,Headers=None):

    response = requests.get(url, headers=Headers, allow_redirects=True)
    return response

url = "https://Hacker.com/DownloadFile.ashx?ID=383403"
Headers = {'Cookie':'CbcCht_FontSize=12; CbcCht_FontSize=12; _ga_4L5WM8QRCG=GS1.1.1729227591.1.0.1729227595.0.0.0; ASP.NET_SessionId=HackSession'} # Modify it!

httpPesponse = httpGetResponse(url,Headers)

with open("downloaded.doc", "wb") as pdf_file:
    pdf_file.write(httpPesponse.content)
