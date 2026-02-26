from flask import Flask,render_template
from pymongo import MongoClient

client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')
database=client['foura10']
collection=database['foura10_2']

collection.insert_one(
    {
        'username':'revanth',
        'password':'abc@1234'
    }
)

user=collection.find({
    'username':'revanth12344',
    'password':'abc@1234'
})
if user:
    print("Welcome the user")
else:
    print("No user found")
    
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('first.html')

@app.route('/revanth')
def home1():
    return render_template('second.html')

if __name__=='__main__':
    app.run(port=5500,debug=True)