from db import db

from models.baseUser import BaseUserModel
from models.enums import userRole,sellState


class SellerModel(BaseUserModel):
    __tablename__ = "sellers"

    role = db.Column(db.Enum(userRole), default=userRole.seller, nullable=False)



class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_on = db.Column( db.DateTime, nullable=False, server_default=func.now())
    status = db.Column( db.Enum(sellState), nullable=False, default=sellState.listed)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.id"), nullable=False)
    seller = db.relationship("SellerModel")


