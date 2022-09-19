from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

#class User(db.Model, UserMixin):
 #      id = db.Column(db.Integer, primary_key=True)
 #      email = db.Column(db.String(150), unique=True)
 #      password = db.Column(db.String(150))
 #      firstName = db.Column(db.String(150))
 #      reports = db.relationship('Report')

class Report(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       firstname = db.Column(db.String(150))
       lastname = db.Column(db.String(150))
       othername = db.Column(db.String(150))
       agev = db.Column(db.Integer)
       gender = db.Column(db.String)
       phonenumber = db.Column(db.Integer)
       abuse = db.Column(db.String)
       dates = db.Column(db.DateTime)
       first = db.Column(db.String(150))
       last = db.Column(db.String(150))
       oname = db.Column(db.String(150))
       age = db.Column(db.Integer)
       gender = db.Column(db.String)