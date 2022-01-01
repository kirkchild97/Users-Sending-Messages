from flask import request, session, flash, redirect, render_template, url_for
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app import app

b = Bcrypt(app)

@app.route('/')
def register_login_page():
    return render_template('loginPage.html')

@app.route('/try_register', methods = ['POST'])
def register_user():
    # Validation First
    data = {
        'first_name' : request.form['f_name'],
        'last_name' : request.form['l_name'],
        'email' : request.form['email'],
        'password' : [
            request.form['password'],
            request.form['con_password']
        ]
    }
    if User.register_validation(data):
        data['password'] = b.generate_password_hash(data['password'])
        User.save_user(data)
        return redirect('/registersuccess')
    else:
        return redirect('/')

@app.route('/registersuccess')
def register_success():
    return render_template('registersuccess.html')

@app.route('/try_login', methods = ['POST'])
def login_user():
    pass

@app.route('/user_page/<user_id>')
def user_wall(user_id):
    # Login information should be validated and proper info in session
    pass

@app.route('/user_page/<user_id>/message/send', methods = ['POST'])
def send_message(user_id):
    pass

@app.route('/user_page/<user_id>/message/delete', methods = ['POST'])
def delete_message(user_id):
    # Ensure the user has the authority to delete message
    pass

@app.route('/hackwarning')
def unauthorized_access_warning():
    # Get IP address to scare the hacker :)
    pass