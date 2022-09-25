from flask import Blueprint, render_template, request, flash, redirect, url_for

from . import db
from .models import Report
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist. Sign up to make a report!', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email =request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        age1 = request.form.get('age1')
        gender = request.form.get('gender')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!', category='error')
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif password1 != password2 :
            flash('Passwords don\'t match', category='error')

        else:
            new_user = User(email=email, firstName=firstName, lastName=lastName, age1=age1, gender=gender, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            #flash('Account created!', category='success')
            #return redirect(url_for('views.home'))
            flash("You have successfully signed up and can now make a report!", category='success')
            return redirect(url_for('auth.report'))

    return render_template("signup.html", user=current_user)

@auth.route('/about')
@login_required
def about():
    return render_template("about.html", user=current_user)

@auth.route('/report', methods=['get', 'post'])
@login_required
def report():
    if request.method == 'POST':
        #phonenumber = request.form.get('phonenumber')
        abuse = request.form.get('abuse')
        dates = request.form.get('dates')
        first = request.form.get('first')
        last = request.form.get('last')
        oname = request.form.get('oname')
        age = request.form.get('age')
        gender = request.form.get('gender')
        date = request.form.get('date')
        user_id = request.form.get(str(User.id))



#method implemented for user inputs and how they are executed.
        if abuse == "defilement":
            flash('Considering the severity of the type of abuse, you are advised to VISIT NEAREST POLICE STATION IMMEDIATELY!', category="success")
            persit_db(abuse, dates, first, last, oname, age, gender, date, user_id)
        elif abuse == "rape":
            flash('Considering the severity of the type of abuse, you are advised to VISIT NEAREST POLICE STATION IMMEDIATELY! A docket will be opened for you and an expert doctor will take up your case to attest this report!', category="success")
            persit_db(abuse, dates, first, last, oname, age, gender, date,user_id)
        elif abuse == "verbal":
            flash('You are advised to visit the victim supposrt unit at your nearest police station where you will receive counselling and be helpeded greatly!', category="success")
            persit_db(abuse, dates, first, last, oname, age, gender, date, user_id)
        elif abuse == "battery":
            flash('If this is the first instance, you are advised to get counseling. If this is a regular occurence, visit you nearest police station where you will be helped accordingly!', category="success")
            persit_db(abuse, dates, first, last, oname, age, gender, date, user_id)

        else:
            #create_report(new_report, remember=True)
            flash('Report Successfully submitted', category='success')


    return render_template("report.html", user=current_user)

def persit_db(abuse, dates, first, last, oname, age, gender, date, user_id):
    new_report = Report(abuse=abuse, dates=dates, first=first, last=last, oname=oname, age=age, gender=gender,
                        date=date, user_id=User)
    db.session.add(new_report)
    db.session.commit()
