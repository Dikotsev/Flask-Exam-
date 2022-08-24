from db import db
from sqlalchemy import func

from models.seller import ProductModel, SellerModel
from models.buyer import BuyerModel
from models.enums import sellState





class PurchaseModel(db.Model):
    __tablename__ = purchases

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    created_on = db.Column( db.DateTime, nullable=False, server_default=func.now())
    product_id = db.Column(db.Integer, db.ForeignKey("ProductModel"), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey("BuyerModel"), nullable=False)
    transaction_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(sellState), nullable=False, default=sellState.pending)


class TransactionModel(db.Model):
    __tablename__ = transactions
    id = db.Column(db.Integer, primary_key=True, nullable=False)