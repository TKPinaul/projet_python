from . import db
from flask_login import UserMixin 
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(150), nullable=False)
    prenom = db.Column(db.String(150), nullable=False)
    mail = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(50), nullable=False)
