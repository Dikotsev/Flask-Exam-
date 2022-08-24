from config import create_app
from decouple import config
from db import db





app = create_app()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.after_request
def return_resp(resp):
    db.session.commit()
    return resp


if __name__ == "__main__":
    app.run()
