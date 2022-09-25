from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class User(db.Model, UserMixin):
       id = db.Column(db.Integer, primary_key=True)
       email = db.Column(db.String(150), unique=True, nullable=False)
       firstName = db.Column(db.String(150))
       lastName = db.Column(db.String(150))
       age1 = db.Column(db.Integer)
       gender = db.Column(db.String)
       address = db.Column(db.String)
       province = db.Column(db.String)
       phonenumber = db.Column(db.Integer)
       password = db.Column(db.String(150))
       reports = db.relationship('Report')

class Report(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       abuse = db.Column(db.String, nullable=False)
       dates = db.Column(db.DateTime)
       first = db.Column(db.String(150))
       last = db.Column(db.String(150))
       oname = db.Column(db.String(150))
       age = db.Column(db.Integer)
       gender = db.Column(db.String)
       date = db.Column(db.DateTime(timezone=True), default=func.now())
       user_id = db.Column(db.Integer, db. ForeignKey('user.id'))



