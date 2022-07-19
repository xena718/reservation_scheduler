"""data model for reservation scheduler app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String, unique=True, nullable=False)


    def __repr__(self):
        return f"<user_id ={self.user_id} and user_name ={self.user_name}>"

class Reservation(db.Model):
    """A reservation"""

    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    reservation_start_time = db.Column(db.DateTime, unique=True, nullable=False)
    
    user = db.relationship("User", backref="reservations")
    #one user_id can have multipl reservations. one to many relationship


    def __repr__(self):
        return f"<user_id ={self.user_id} and reservation_start_time={self.reservation_start_time}"


def connect_to_db(flask_app, db_uri="postgresql:///scheduler", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)