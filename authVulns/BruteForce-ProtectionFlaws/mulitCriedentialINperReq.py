import json

def create_json_with_multiple_passwords(username, passwords):

    user_data = {
        "username": username,
        "password": passwords
    }
    return user_data


with open('list.txt', 'r') as f:
    content = f.read()
    possible_passwords = content.split()

print(possible_passwords)

username = "carlos"
user_credentials = create_json_with_multiple_passwords(username, possible_passwords)

json_data = json.dumps(user_credentials)
print(json_data)

