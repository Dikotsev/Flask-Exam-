from flask import request
from flask_api import status
from flask_restful import Resource

from managers.auth import auth
from managers.purchase_manager import PurchaseManager
from models.enums import userRole
from schemas.request.purchase import PurchaseSchemaRequest
from schemas.response.purchase import PurchaseSchemaResponse
from utils.decorators import permission_required, validate_schema


class PurchaseResource(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        purchase = PurchaseManager.get_purchase(user)
        return PurchaseSchemaResponse().dump(purchase, many=True)

    @auth.login_required
    @permission_required(userRole.seller)
    @validate_schema(PurchaseSchemaRequest)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_purchase = PurchaseManager.create_purchase(data, current_user)
        return PurchaseSchemaResponse().dump(new_purchase) , status.HTTP_201_CREATED


class ApproveComplaintResource(Resource):
    @auth.login_required
    @permission_required(UserRole.approver)
    def put(self, id):
        ComplaintManager.approve(id)
        return status.HTTP_204_NO_CONTENT


class RejectPurchaseResource(Resource):
    @auth.login_required
    @permission_required(userRole.seller)
    def put(self, id):
        PurchaseManager.reject(id)
        return status.HTTP_204_NO_CONTENT


class RejectPurchaseResource(Resource):
    @auth.login_required
    @permission_required(userRole.buyer)
    def put(self, id):
        PurchaseManager.reject(id)
        return status.HTTP_204_NO_CONTENT