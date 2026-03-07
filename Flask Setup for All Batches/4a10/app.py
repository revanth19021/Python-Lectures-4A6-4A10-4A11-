from flask import Flask,render_template,request
from pymongo import MongoClient

client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')
database=client['foura10']
collection=database['foura10_2']

    
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('first.html')



@app.route('/register')
def registration():
    return render_template('register.html')


@app.route('/registration',methods=['post'])
def registeruser():
    #a= request.form.get('email')
    a=request.form['email']
    b=request.form['password']
    c=request.form['cnfpass']
    d=request.form['username']
    # cchecking the password 
    if b!=c:
        return "Please enter correct password"
    # Existed user 
    user=collection.find_one({
        'username':d
    })
    
    if user:
        return "Already Exisisted User"
    
    collection.insert_one({
        'email_id':a,
        'password':b,
        'username':d
    })
    return "Registered Successfully"

@app.route('/login')
def log():
    return render_template('login.html')

@app.route('/login-verify',methods=['post'])
def loginverification():
    a=request.form['username']
    # b=request.form['password']
    user=collection.find_one({
        'username':a
    })
    
    if user:
        return render_template('second.html')
    
    return render_template('login.html')
    
    
    
    
    
    


if __name__=='__main__':
    app.run(port=5500,debug=True)