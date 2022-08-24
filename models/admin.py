from db import db


from models.baseUser import BaseUserModel
from models.enums import userRole


class AdminModel(BaseUserModel):
  __tablename__ = "admin"

  role = db.role(db.Enum(userRole), default=userRole.admin, nullable=False)