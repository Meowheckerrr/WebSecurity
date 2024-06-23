from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# 用于存储消息的简单列表
messages = []

@app.route('/')
def home():
    return '''
        <h1>Welcome to the Guestbook</h1>
        <a href="/message">Leave a message</a><br>
        <a href="/admin">Admin View</a>
    '''

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        message = request.form['message']
        if message:
            # 将消息存储在列表中
            messages.append({'message': message})
            return redirect(url_for('home'))
        else:
            return 'Please enter a message.'
    return '''
        <h1>Leave a Message</h1>
        <form action="/message" method="post">
            <label for="message">Message:</label><br>
            <textarea id="message" name="message"></textarea><br>
            <input type="submit" value="Submit">
        </form>
        <a href="/">Back to Home</a>
    '''

@app.route('/admin')
def admin():
    # 生成包含所有消息的 HTML
    messages_html = ''
    for msg in messages:
        messages_html += f"Message: {msg['message']}<br><br>"
    
    return render_template_string(f'''
        <h1>Admin View</h1>
        <div>{messages_html}</div>
        <a href="/">Back to Home</a>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)