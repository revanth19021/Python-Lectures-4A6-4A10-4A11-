from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = "mysecretkey"   # Required for flash messages

@app.route('/')
def home():
    return render_template("hello1.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']

    if username == "admin":
        flash("Login Successful!", "success")
    else:
        flash("Invalid Username!", "error")
        
        
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)