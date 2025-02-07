from flask import Flask, request, jsonify

app = Flask(__name__)

user_database = {"username":"meowhecker","password":"admin"}

@app.route('/api/login', methods=['POST'])
def login():
    # 從請求中提取 JSON 數據
    PostData = request.get_json()
    username = PostData.get('username')
    UserPassword = PostData.get('password')
    print(username)
    print(UserPassword)
   
    if username in user_database['username']:
        if UserPassword in user_database['password']:
            print(UserPassword)
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid password"}), 401
    else:
        return jsonify({"message": "Invalid username"}), 404

    
app.run(host='0.0.0.0', port=5000, debug=True)