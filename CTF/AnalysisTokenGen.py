import datetime
import hashlib

# url = "https://0ae900ed033f23288166aceb000b003c.web-security-academy.net/login2"

username = "admin"
print("DateTime",datetime.datetime.now())
value = datetime.datetime.now()
print("prifix",str(value)[:-4])
lnk = str(value)[:-4] + " . " + username.upper()
lnk = hashlib.sha1(lnk.encode("utf-8")).hexdigest()

print(lnk)