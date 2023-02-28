from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p1>logout</p1>"


@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST' :
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        passwrod2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('firstName must be greather than 1 character ', category='error')
        elif password1 != passwrod2:
             flash('passwords don\'t matches ', category='error')
        elif len(password1) < 7:
            flash('password1 must be at least 7 characters ', category='error')
        else:
            flash('account created !', category='success')

    return render_template("sign_up.html")
 







