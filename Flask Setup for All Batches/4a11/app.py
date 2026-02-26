from flask import Flask,render_template

app1=Flask(__name__)

@app1.route('/')
def home():
    return render_template('first.html')


@app1.route('/name')
def name():
    return render_template('second1.html')

@app1.route('/emailid')
def email():
    return "abc@123gmail.com"

if __name__=='__main__':
    app1.run(port=5500,debug=True)