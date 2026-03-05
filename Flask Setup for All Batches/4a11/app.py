from flask import Flask,render_template,request
from pymongo import MongoClient
client=MongoClient('mongodb://127.0.0.1:27017/')
database=client['registration']
collection=database['form']
app1=Flask(__name__)

@app1.route('/')
def home():
    return render_template('first.html')

@app1.route('/register')
def registration():
    return render_template('register.html')


@app1.route('/reg',methods=['post'])
def registeruser():
    a=request.form['user']
    b=request.form['password']
    c=request.form['email']
    d=request.form['cnf']
    if b!=d:
        return "please enter password correctly"
    user=collection.find_one({
        'username':a
    })
    if user:
        return "Already Existed"
    
    collection.insert_one({
        'username':a,
        'password':b,
        'email_id':c
    })
    return render_template('login.html')

    
    



if __name__=='__main__':
    app1.run(port=5500,debug=True)