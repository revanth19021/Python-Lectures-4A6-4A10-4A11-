from flask import Flask,render_template,request,redirect,url_for,session
from pymongo import MongoClient

client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')
database=client['foura10']
collection=database['foura10_2']

app=Flask(__name__)
app.secret_key='revanth'
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
        return render_template('register.html',message="please enter Correct password")
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
    # return redirect(url_for('log'))
    return render_template('login.html')

@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/login-verify',methods=['post'])
def loginverification():
    a=request.form['username']
    # b=request.form['password']
    user=collection.find_one({
        'username':a
    })
    
    values=collection.find_one({'username':a},{'_id':0})
    if user:
        session['username']=a
        return render_template('second.html',users=values)
    
    return render_template('login.html')
    
        

if __name__=='__main__':
    app.run(port=5500,debug=True)