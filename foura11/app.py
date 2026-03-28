from flask import Flask,render_template,request,jsonify
from pymongo import MongoClient

client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')

database=client['registration']
collection=database['form']

app=Flask(__name__)

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
    
    collection.insert_one({
        'username':username,
        'password':password,
        'email':email
    })
    return "Registration Successful"
@app.route('/login_verify',methods=['POST'])
def log():
    username=request.form.get('username')
    password=request.form.get('password')
    
    user=collection.find_one({
        'username':username,
        'password':password
    })
    if user:
        return "Login Successful"
    return "Invalid Credentials"

@app.route('/getusers',methods=['GET'])
def getusers():
    data=list(collection.find({},{'_id':0}))
    return jsonify(data)

@app.route('/updateuser',methods=['PUT'])
def updateuser():
    data=request.json
    username=data.get('username')
    new_password=data.get('password')
    new_email=data.get('email')
    
    collection.update_one({'username':username},{'$set':{
        'password':new_password,
        'email':new_email
        
    }})
    
    return "Updated successfully"
    # update_one({filter},{operator:{updated values}})
    
@app.route('/deleteuser',methods=['DELETE'])
def deleteuser():
    data=request.json
    
    username=data.get('username')
    collection.delete_one({'username':username})
    
    return "Deleted Successfully"


if __name__=='__main__':
    app.run(port=7000,debug=True)

