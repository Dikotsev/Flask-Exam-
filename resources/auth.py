from flask import request
from flask_api import status
from flask_restful import Resource

from managers.admin_manager import AdminManager
from managers.buyer_manager import BuyerManager
from managers.seller_manager import SellerManager
from schemas.requests.auth import RegisterSchemaRequest, LoginSchemaRequest
from utils.decorators import validate_schema


class RegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = SellerManager.register(data)
        return {"token": token},  status.HTTP_201_CREATED


class LoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = SellerManager.login(data)
        return {"token": token}, status.HTTP_200_OK

class RegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = BuyerManager.register(data)
        return {"token": token},  status.HTTP_201_CREATED


class LoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = BuyerManager.login(data)
        return {"token": token}, status.HTTP_200_OK

class AdminLoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = AdminManager.login(data)
        return {"token": token},  status.HTTP_200_OK
