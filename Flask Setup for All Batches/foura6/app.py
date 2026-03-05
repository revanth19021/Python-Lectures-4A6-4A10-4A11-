from flask import Flask,render_template,request
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
        return "Please enter Same password"
    user=collection.find_one({'username':u})
    if user:
        return "ALready Registered"
    collection.insert_one({
        'username':u,
        'password':password,
        'emailid':email_id
    })
    return "data registered"
    
    

if __name__=="__main__":
    app.run(port=5000,debug=True)

#port # host #debug=