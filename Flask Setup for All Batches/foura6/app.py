from flask import Flask,render_template
# create an object to the Flask class
from pymongo import MongoClient
client=MongoClient('mongodb://127.0.0.1:27017/')
database=client['revanth']
collection=database['batch3']
collection.insert_one(
    {
        'email-id':'abc@gmail.com',
        'password':'abc@12345',
        'username':'revanth19021'
    }
)
print("Data Is inserted")
app=Flask(__name__)
# second step is routing to a url

@app.route('/')
def hello():
    return render_template('first.html')

# @app.route('/hello')
# def hello():
#     return "revanth"
    
if __name__=="__main__":
    app.run(port=5000,debug=True)

#port # host #debug=