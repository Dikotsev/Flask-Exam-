import uuid

from constants.common import TEMP_DIR
from db import db

#from services.s3 import S3Service
#from services.wise import WiseService
from utils.common import decode_file



from models.purchase import PurchaseModel,TransactionModel
from models.enums import sellState









class PurchaseManager:
    @staticmethod
    def get_purchase(data):
        pass


    @staticmethod
    def create_purchase(data, buyer, seller):
        purchase = PurchaseModel(**data)
        data["photo_url"] = photo_url
        extension = data.pop( "extension" )
        photo = data.pop( "photo" )
        file_name = f"{str( uuid.uuid4() )}.{extension}"
        path = os.path.join( TEMP_DIR, file_name )
        decode_file( path, photo )
     #seller["seller_id"] = seller_id
        buyer["buyer_id"] = buyer_id
        seller["seller_id"] = seller_id
        db.session.add(purchase)
        db.session.flush()
        transaction_data = PurchaseManager.issue_transaction(data["amount"], f"{user.first_name} {user.last_name}", user.iban, complaint.id)
        transaction = TransactionModel(**transaction_data)
        db.session.add(transaction)
        db.session.flush()
        return purchase






    @staticmethod
    def reject(purchase_id):
        #transaction = TransactionModel.query.filter_by( purchase_id=purchase_id ).first()
        # Here cancel the transfer
        # wise.fund_transfer(transaction.transfer_id)
        PurchaseModel.query.filter_by( id=purchase_id ).update( {"status": sellState.rejected} )


    @staticmethod
    def approve(purchase_id):
    # transaction = TransactionModel.query.filter_by(complaint_id=complaint_id).first()
    #wise.fund_transfer(transaction.transfer_id)
        PurchaseModel.query.filter_by(id=purchase_id).update({"status": sellState.in_progress})\



    @staticmethod
    def issue_transaction(amount, full_name, iban, complaint_id):
        quote_id = wise.create_quote( "EUR", "EUR", amount )
        recipient_id = wise.create_recipient( full_name, iban )
        customer_transaction_id = str( uuid.uuid4() )
        transfer_id = wise.create_transfer( recipient_id, quote_id, customer_transaction_id )["id"]
        data = {
            "quote_id": quote_id,
            "recipient_id": recipient_id,
            "transfer_id": transfer_id,
            "target_account_id": customer_transaction_id,
            "amount": amount,
            "complaint_id": complaint_id,
        }
        return data
