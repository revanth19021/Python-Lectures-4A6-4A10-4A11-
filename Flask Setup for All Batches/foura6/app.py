from flask import Flask,render_template
# create an object to the Flask class
app=Flask(__name__)

# second step is routing to a url

@app.route('/')
def hello():
    return "hello"

@app.route('/raj')
def waste():
    return "Waste fellow"

if __name__=="__main__":
    app.run(port=5000,debug=True)

#port # host #debug=