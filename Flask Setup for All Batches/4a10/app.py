from flask import Flask,render_template
from pymongo import MongoClient

client=MongoClient('mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/')
database=client['foura10']
collection=database['foura10_2']

    
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('first.html')

@app.route('/revanth')
def home1():
    return render_template('second.html')

@app.route('/register')
def registration():
    return render_template('register.html')


@app.route('/login')
def loginpage():
    return render_template('login.html')

if __name__=='__main__':
    app.run(port=5500,debug=True)