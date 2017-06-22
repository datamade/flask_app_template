from template.database import db
from template import models
from template import create_app

if __name__ == "__main__":
    fake_app = create_app()

    with fake_app.test_request_context():

        db.create_all()
