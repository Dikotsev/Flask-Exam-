from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import AuthManager
from models.seller import SellerModel
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum
from models.enums import userRole


class SellerManager:
    @staticmethod
    def register(seller_data):
        seller_data["password"] = generate_password_hash(seller_data["password"])
        user = SellerModel(**seller_data)
        db.session.add(user)
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        seller = SellerModel.query.filter_by(email=login_data["email"]).first()
        if not SellerModel.userRole("seller"):
            raise BadRequest("You are not register as a seller! Please register!")
        if check_password_hash(seller.password, login_data["password"]):
            return AuthManager.encode_token(seller)
        return BadRequest("Wrong credentials")

