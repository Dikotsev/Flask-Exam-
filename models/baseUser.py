from db import db



class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    phone = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    post_code = db.Column(db.String(200), nullable=False)