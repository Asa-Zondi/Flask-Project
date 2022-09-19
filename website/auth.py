from flask import Blueprint, render_template, request, flash
from .models import Report

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 5:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created', category='success')
    return render_template("signup.html")


@auth.route('/report', methods=['get', 'post'])
def signup():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        othername = request.form.get('othername')
        agev = request.form.get('agev')
        genderv = request.form.get('genderv')
        phonenumber = request.form.get('phonenumber')
        abuse = request.form.get('abuse')
        dates = request.form.get('dates')
        first = request.form.get('first')
        last = request.form.get('last')
        oname = request.form.get('oname')
        age = request.form.get('age')
        gender = request.form.get('gender')

        if len(firstname) < 3:
            flash('Enter first name of victim!', category='error')
        elif abuse == "defilement":
            flash('')
        elif abuse == "rape":
            flash('Report to police station immediately', category="success")
        elif abuse == "verbal":
            flash('You are advised to visit the victim supposrt unit at your nearest police station where you will receive councilling', category="success")
        ##elif len(lastname) < 3:
                ##flash('Enter first name of victim!', category='error')
        else:
            #add user to database
            flash('Report Successfully submitted', category='success')


    return render_template("report.html")
