from flask import Flask,render_template,request,session
from pymongo import MongoClient
client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')
database=client['registration']
collection=database['form']
app1=Flask(__name__)
app1.secret_key='revanth@1234'
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
        return render_template('register.html',message="please enter both password correctly")
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

    
@app1.route('/login')
def logining():
    return render_template('login.html') 

@app1.route('/login_verify',methods=['post'])
def loginuser():
    a=request.form.get('username')
    b=request.form.get('password')
    user=collection.find_one({
        'username':a,
        'password':b
    })
    values=collection.find()
    if user:
        session['username']=user['username']
        return render_template('main.html',username=session['username'],users=values)
    return render_template('login.html')


if __name__=='__main__':
    app1.run(port=5500,debug=True)