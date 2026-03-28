from flask import Flask,render_template,request,jsonify

from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')

db=client['registration']

collection=db['form']


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register_verify',methods=['GET','POST'])
def registration():
    if request.method=='POST':
        a=request.form.get('username')
        b=request.form.get('password')
        c=request.form.get('email')
    
        collection.insert_one({
        'username':a,
        'password':b,
        'email':c
        })
    
    return "Registered Successfully"

@app.route('/login_verify',methods=['GET','POST'])
def log():
    if request.method=='POST':
        a=request.form.get('username')
        b=request.form.get('password')
        
        user=collection.find_one(
            {
                'username':a,
                'password':b
            }
        )
        if user:
            return "User is present"
    return 'invalid'
    
@app.route('/users',methods=['GET'])
def users1():
    users=list(collection.find({},{'_id':0}))
    return jsonify(users)

@app.route('/updateuser',methods=['PUT'])
def updateuser():
   data=request.json
   a=data.get('username')
   b=data.get('password')
   c=data.get('email')
   
   user=collection.update_one(
       {'username':a},
       {'$set':{
           'password':b,
           'email':c
       }
       
   })
   if user:
       return "User is updated"
   return "No user is found"

@app.route('/delete_user',methods=['DELETE'])
def deleting():
    data=request.json
    
    a=data.get('username')
    
    user=collection.delete_one({'username':a})
    
    if user:
        return "Deleted Successfully"
    return "No User found"


if __name__=='__main__':
    app.run(debug=True)