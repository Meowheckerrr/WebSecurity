from flask import Flask, request, render_template, redirect, url_for, flash
import os


app = Flask(__name__)
app.secret_key = "meowKEy"
messageFile = './message.txt'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        if name and message:
            with open(messageFile, 'a') as f:
                f.write(f'Name: {name}\nMessage: {message}\n\n')
            flash('Message sent successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please enter both name and message.', 'error')
            
    return render_template('message.html')


@app.route('/admin')
def admin():
    if os.path.exists(messageFile):
        with open(messageFile, 'r') as f:
            messages = f.read()
    else:
        messages = 'No messages yet.'
    
    return render_template('admin.html', messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)