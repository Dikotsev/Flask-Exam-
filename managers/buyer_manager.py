from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import AuthManager
from models.buyer import BuyerModel
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum
from models.enums import userRole


class BuyerManager:
    @staticmethod
    def register(buyer_data):
        buyer_data["password"] = generate_password_hash(buyer_data["password"])
        user = BuyerModel(**buyer_data)
        db.session.add(user)
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        buyer = BuyerModel.query.filter_by(email=login_data["email"]).first()
        if not BuyerModelModel.userRole("buyer"):
            raise BadRequest("You are not register as a buyer! Please register!")
        if check_password_hash(buyer.password, login_data["password"]):
            return AuthManager.encode_token(buyer)
        return BadRequest("Wrong credentials")

