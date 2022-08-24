from marshmallow import Schema, fields, validate


class AuthBase(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.string(min=3, max=20))


class PurchaseBase(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    amount = fields.Float(required=True)

