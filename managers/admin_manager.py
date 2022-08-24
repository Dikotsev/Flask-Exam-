from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from managers.auth import AuthManager
from models.admin import AdminModel
from models.purchase import PurchaseModel


class AdminManager:
    @staticmethod
    def login(data):
        # Todo refector as sub-func and reuse in complainer as well, later in admin
        admin = AdminModel.query.filter_by(email=data["email"]).first()
        if not admin:
            raise BadRequest("You are not admin")

        if check_password_hash(admin.password, data["password"]):
            return AuthManager.encode_token(admin)
        raise BadRequest("Invalid credentials")


    @staticmethod
    def approve_purchase(purchase_id):
        if purchase_id:
            purchase = PurchaseModel.query.filter_by(purchase_id=purchase_id).first()
            pass




