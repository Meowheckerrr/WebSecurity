import requests
import threading
import sys

def checkSatuatCode(targetURL,statueCode,response):

    if (response.status_code == statueCode):
        print(targetURL)
        print (f'Statue Code:{response.status_code}')

        for key, value in response.headers.items():
            print(f'{key}:{value}')

        print("="*40)
        
def threadings():
    maxThreading = 20 
    semaphore = threading.BoundedSemaphore(maxThreading)
   
    
    for i in range(10000):
        #Get the semaphore 
        semaphore.acquire()
        requestHandler = threading.Thread(target=sendRequestAndChecked, args=(i,semaphore))
        requestHandler.start()
        #print("Number of active threads:", threading.active_count())
    sys.exit()

#Sub Treading Jobs 
def sendRequestAndChecked(i,semaphore):

    imageFileName = str(i).zfill(4)
    url = "http://lotuxctf.com:20003/"+imageFileName+".jpg"

    #print(imageFileName)
    response = requests.get(url)
    checkSatuatCode(url,200,response)
    
    semaphore.release()  # release Semapore
    sys.exit() # Termerate a sub threading  

if __name__  == "__main__":

    try:
        print("Author: MeowHecker")
        print("Process Start ...")
        threadings()
    except:
        sys.exit()




