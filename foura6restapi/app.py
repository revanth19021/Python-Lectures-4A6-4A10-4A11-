from flask import render_template, request, Flask, jsonify
from pymongo import MongoClient

client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')

database=client['registration']
collection=database['form']
app=Flask(__name__)


@app.route('/')
def hello():
    return "Welcome to home page"

@app.route('/register')
def open1():
    return render_template('register.html')

@app.route('/register_verify', methods=['POST'])
def registration():
    username=request.form.get('username')
    password=request.form.get('password')
    collection.insert_one({
        'username':username,
        'password':password
    })
    
    return "Registered successfully"


@app.route('/login')
def hell111():
    return render_template('login.html')


@app.route('/login_verify',methods=['POST'])
def log():
    username=request.form.get('username')
    password=request.form.get('password')
    user=collection.find_one({
        'username':username,
        'password':password
    })
    
    if user:
        return "Login Success"
    return "Invalid Credentials"



@app.route('/getusers',methods=['GET'])
def users():
    data=list(collection.find({},{'_id':0}))
    
    return jsonify(data)

@app.route('/updateuser',methods=['PUT'])
def updateuser():
    data=request.json
    # two scenarios 
    # request.form.get()
    username=data.get('username')
    new_password=data.get('password')
    user=collection.update_one({'username':username},{'$set':{'password':new_password}})
    
    if user:
        return "Updated Successfully"
    else:
        return "Not found"
    
    # update({filter},{operator:{updation value}})
    
@app.route('/deleteuser',methods=['DELETE'])
def deleteuser():
    data=request.json
    username=data.get('username')
    
    user=collection.delete_one({'username':username})
    
    if user:
        return "Deleted successfully"
    return "No User FOund"
if __name__=='__main__':
    app.run(port=6600,debug=True)
    
    
