import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from datetime import datetime, timedelta
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import BadRequest, Unauthorized

from models.buyer import BuyerModel
from models.seller import SellerModel
from models.admin import AdminModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(hours=1)}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized("Missing token")
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise Unauthorized("Token expired")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")


auth = HTTPTokenAuth()


@auth.verify_token
def verify_buyer(token):
    user_id = AuthManager.decode_token(token)
    return BuyerModel.query.filter_by(id=user_id).first()


@auth.verify_token
def verify_seller(token):
    user_id = AuthManager.decode_token(token)
    return SellerModel.query.filter_by(id=user_id).first()


@auth.verify_token
def verify_admin(token):
    user_id = AuthManager.decode_token(token)
    return AdminModel.query.filter_by(id=user_id).first()
