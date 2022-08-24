from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums import sellState
from schemas.base import PurchaseBase


class PurchaseSchemaResponse(ComplaintBase):
    id = fields.Int(required=True)
    created_on = fields.DateTime(required=True)
    status = EnumField(sellState, by_value=True)
    photo_url = fields.String(required=True)

