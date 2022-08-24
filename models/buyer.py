from db import db


from models.baseUser import BaseUserModel
from models.enums import userRole


class BuyerModel(BaseUserModel):
  __tablename__ = "buyer"

  role = db.role(db.Enum(userRole), default=userRole.buyer, nullable=False)