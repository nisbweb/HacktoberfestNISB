
from tkinter.messagebox import NO
from flask import Flask, session, render_template, request, redirect
import pyrebase
login = Flask(__name__)
config = {
  'apiKey': "AIzaSyCaApKPyFhOhcBQ7mobXxjYN84ErEuNht0",
  'authDomain': "nisb-lib.firebaseapp.com",
  'projectId': "nisb-lib",
  'storageBucket': "nisb-lib.appspot.com",
  'messagingSenderId': "807484217566",
  'appId': "1:807484217566:web:295ec5a65c9af6aec28a4f",
  'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)

auth1 = firebase.auth()

login.secret_key = 'shr'     

@login.route('/', methods=['POST','GET'])
def index():
    if 'user1' in session:   
        return render_template('index.html')
    if request.method=='POST':
        email=request.form.get('email')
        
        password=request.form.get('pass')       
        print(email,password)
        try:
            user1 = auth1.sign_in_with_email_and_password(email,password)
            # print("step 1 done")
            # return "step 1 done"
            session['user1'] = email
            return render_template('index.html')
        except:
            return 'Failed to login<br>Incorrect password or Email'    
    return render_template("home.html")

@login.route('/signup', methods=['POST','GET'])
def signup():
    email1 = request.form.get('email1')
    password1 = request.form.get('password1')
    if email1 is None or password1 is None:
        return 'Error missing email or password'
    else:
        try:
            user = auth1.create_user_with_email_and_password(email1,password1)
            return redirect('/')
        except:
            return 'failed'
             
@login.route('/logout',methods=['POST','GET'])
def logout():
    session.pop('user1',None)
    return redirect('/')

if __name__ ==  '__main__':
    login.run(port=1111)




