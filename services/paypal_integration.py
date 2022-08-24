'''
import braintree
from constants.common import currencies
from models.buyer import BuyerModel

gateway = braintree.BraintreeGateway(access_token=use_your_access_token)
'''
'''
#@app.route("/client_token", methods=["GET"])
def client_token():
  return client_token == gateway.client_token.generate()

@app.route("/checkout", methods=["POST"])
def create_purchase():
  nonce = request.form["payment_method_nonce"]
  # Use payment method nonce here...

import braintree

gateway = braintree.BraintreeGateway( access_token=use_your_access_token )

result = gateway.transaction.sale( {
      "amount": request.form["amount"],
      "merchant_account_id": currencies[transaction_currencies],
      "payment_method_nonce": request.form["payment_method_nonce"],
      "device_data": request.form["device_data"],
      "order_id": "Mapped to PayPal Invoice Number",
      "descriptor": {
          "name": "Descriptor displayed in customer CC statements. 22 char max"
      },
      "shipping": {
          "first_name": BuyerModel.first_name,
          "last_name":  BuyerModel.last_name,
          "street_address": BuyerModel.address,
          "extended_address": BuyerModel.post_code,
          "region": "IL",
          "country_code_alpha2": "US"
      },
      "options": {
          "paypal": {
              "custom_field": "PayPal custom field",
              "description": "Description for PayPal email receipt"
          },
      }
  } )
if result.is_success:
    "Success ID: ".format( result.transaction.id )
else:
 #   format( result.message )
'''