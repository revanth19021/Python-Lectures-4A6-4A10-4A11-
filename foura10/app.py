from flask import Flask, render_template,redirect,request,jsonify
from pymongo import MongoClient
client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')

database=client['registration']
collection=database['form']


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register_verify',methods=['POST'])
def registration():
    username=request.form.get('username')
    password=request.form.get('password')
    email=request.form.get('email')
    
    collection.insert_one(
        {
            'username':username,
            'password':password,
            'email':email
        }
    )
    return "Registered Successfully"

@app.route('/login_verify',methods=['POST'])
def log():
    username=request.form.get('username')
    password=request.form.get('password')
    user=collection.find_one(
        {
            'username':username,
            'password':password
        }
    )
    if user:
        return "Logged in Successfully"
    return "Invalid Credentials"

@app.route('/users',methods=['GET'])
def userdetails():
    user=list(collection.find({},{'_id':0}))
    return jsonify(user)
    
@app.route('/update_user',methods=['PUT'])
def update_user():
    data=request.json
    username=data.get('username')
    new_password=data.get('password')
    new_email=data.get('email')
    
    user=collection.update_one(
        {'username':username},
        {
            '$set':{
                'password':new_password,
                'email':new_email
            }
        }
    )
    if user:
        return "Details updated successfully"
    return "No Userfound"


@app.route('/delete_user',methods=['DELETE'])
def deleting():
    data=request.json
    username=data.get('username')
    user=collection.delete_one({'username':username})
    if user:
        return "Details deleted successfully"
    return "no user is found"

if __name__=='__main__':
    app.run(debug=True)