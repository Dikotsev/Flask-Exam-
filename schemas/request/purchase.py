from schemas.base import PurchaseBase
from marshmallow import fields


class PurchaseSchemaRequest(ComplaintBase):
    photo = fields.String(required=True)
    extension = fields.String(required=True)
