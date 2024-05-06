# Requests library Support HTTP/HTTPS reqeust  
import requests
import threading
import sys

#Setting 
maxThreading = 20 
wordlistPath = './parameterWordlist.txt'


# Original Request (Testing)
FuzzingParameters = "testing"
url = 'http://10.10.46.163:8080/password_reset?'+FuzzingParameters+"=testValue"
response = requests.get(url)
OriginBodyLength = len(response.text)
print("Origin response length: " + str(OriginBodyLength)) # Record (Response Length)


def readWordlistToList(filePath):
    
    list = []
    try:
        with open(filePath, "r") as wordlist:

            for line in wordlist:
                list.append(line.rstrip()) # Remove "/n"    

            #print("List:", list)
            wordlist.close()
        
        return list
    except FileNotFoundError:
        print("File not found:", filePath)
    except Exception as e:
        print("Error", e)




def sendRequestFuzzingParameter(parameter,semaphore):
    
    FuzzingParameters = parameter
    url = 'http://10.10.46.163:8080/password_reset?'+FuzzingParameters+"=testValue"
    response = requests.get(url)

    if len(response.text) != OriginBodyLength:
        print("Parameter Found!!!!")
        print(FuzzingParameters)
        print(response.text)
        sys.exit()

    semaphore.release()
    sys.exit()

#----------------------------------------------------

# Fuzzing Parameters!

def threadings(maxThreading,parameters):
    print("Start Fuzz Parameter")
    semaphore = threading.BoundedSemaphore(maxThreading)
    
    for parameter in parameters:
        semaphore.acquire()
        requestHandler = threading.Thread(target=sendRequestFuzzingParameter, args=(parameter,semaphore))
        requestHandler.start()
        # print("Number of active threads:", threading.active_count())

    sys.exit()

#main
parameters = readWordlistToList(wordlistPath)
threadings(maxThreading,parameters)
sys.exit()