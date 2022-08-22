from db import db

from models.baseUser import BaseUserModel


class SellerModel(BaseUserModel):
    __tablename__ = "sellers"
    pass