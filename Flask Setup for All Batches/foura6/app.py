from flask import Flask,render_template,request,session
# create an object to the Flask class
# from pymongo import MongoClient
# client=MongoClient('mongodb://127.0.0.1:27017/')
# database=client['revanth']
# collection=database['batch3']
# collection.insert_one(
#     {
#         'email-id':'abc@gmail.com',
#         'password':'abc@12345',
#         'username':'revanth19021'
#     }
# )
# print("Data Is inserted")
from pymongo import MongoClient

client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')

database=client['foua6']
collection=database['tuesday']

app=Flask(__name__)
# second step is routing to a url

@app.route('/')
def hello():
    return render_template('first.html')

@app.route('/login')
def log():
    return render_template('login.html')

@app.route('/reg')
def register():
    return render_template('register.html')

@app.route('/registration',methods=["POST"])
def registration1():
    u=request.form['username']
    email_id=request.form['email']
    password=request.form['password']
    cnfpassword=request.form['cnf']
    if password!=cnfpassword:
        return render_template('register.html',message='Please enter both passwords correctly')
    user=collection.find_one({'username':u})
    if user:
        return "ALready Registered"
    collection.insert_one({
        'username':u,
        'password':password,
        'emailid':email_id
    })
    return "data registered"
    
@app.route('/login-verify',methods=['post'])
def loginverification():
    a=request.form.get('user')
    b=request.form.get('password')  
    user=collection.find_one({
        'username':a,
        'password':b
    })
    values = collection.find({}, {"_id": 0}) 
    if user:
        session['username']=a
        return render_template('main.html',users=values)
    return render_template('login.html')



if __name__=="__main__":
    app.run(port=7000,debug=True)

#port # host #debug=