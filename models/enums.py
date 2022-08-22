from enum import Enum



class userRole(Enum):
    seller = "seller"
    buyer = "buyer"
    admin = "admin"


class sellState(Enum):
    complate = "complate"
    reject = "reject"
    in_progress = "in progress"
    approved = "approved"