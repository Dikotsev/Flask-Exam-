from enum import Enum



class userRole(Enum):
    seller = "seller"
    buyer = "buyer"
    admin = "admin"


class sellState(Enum):
    complate = "complate"
    rejected = "rejected"
    listed = "listed"
    in_progress = "in progress"
