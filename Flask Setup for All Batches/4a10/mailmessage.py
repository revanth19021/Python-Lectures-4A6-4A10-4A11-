from flask import Flask,render_template

from flask_mail import Mail,Message

app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='sairevanth.naga40337@paruluniversity.ac.in'
app.config['MAIL_PASSWORD']='ldajzhbrzgllammx'

mail=Mail(app)

@app.route('/')
def home():
    return render_template('mailpage.html')

@app.route('/send-mail')
def send_mail():
    msg=Message(
        subject='test mail',
        sender=app.config['MAIL_USERNAME'],
        recipients=['20jr1a0556@gmail.com']
    )
    msg.body='HELLO! REVANTH'
    mail.send(msg)
    return "Mail Sent Successfully!"


if __name__ == '__main__':
    app.run(debug=True)