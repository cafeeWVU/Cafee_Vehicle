from datetime import datetime
from app import db
from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey, Boolean
from sqlalchemy.sql import expression
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login




#engine = create_engine('sqlite:///vehicle.db', echo=True)
#Base = declarative_base()

########################################################################
class User(UserMixin,db.Model):
    """"""
    __tablename__ = "users"

    id = db.Column(Integer, primary_key=True)
    username = db.Column(String)
    #password = db.Column(String)
    password_hash = db.Column(db.String(128))

    #----------------------------------------------------------------------
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


########################################################################
class Vehicle(db.Model):
    """"""
    __tablename__ = "vehicle"

    id = db.Column(Integer, primary_key=True)
    VEHICLE_ID = db.Column(String)
    VEHICLE_TYPE = db.Column(String)
    CABIN_TYPE = db.Column(String)
    MANUFACTURER = db.Column(String)
    MODEL = db.Column(String)
    MODEL_YEAR = db.Column(String)
    VIN = db.Column(String)
    GVWR = db.Column(String)
    TOTAL_MILES = db.Column(String)
    AGENCY_VEHICLE_NUMBER = db.Column(String)
    LICENSE_PLATE = db.Column(String)
    OEM_COMMENTS = db.Column(String)
    AQMD_CATEGORY = db.Column(String)
    EMA_CATEGORY = db.Column(String)



class Engine(db.Model):
    """"""
    __tablename__ = "engine"

    id = db.Column(db.Integer, primary_key=True)
    VEHICLE_ID = db.Column(db.String,db.ForeignKey('vehicle.VEHICLE_ID'))
    MANUFACTURER = db.Column(String)
    ENGINE_MODEL = db.Column(String)
    ENGINE_YEAR = db.Column(String)
    SERIAL = db.Column(String)
    EPA_FAMILY_CERT = db.Column(String)
    DISPLACEMENT = db.Column(String)
    NUMBER_OF_CYLINDERS = db.Column(String)
    CONFIGURATION = db.Column(String)
    IDLE_SPEED = db.Column(String)
    GOVERNED_SPEED = db.Column(String)
    HIGH_IDLE = db.Column(String)
    REFERENCE_TORQUE = db.Column(String)
    ENGINE_REBUILT = db.Column(String)
    YEAR_OF_REBUILT = db.Column(String)
    ECU_PROTOCOL = db.Column(String)
    STOIC_LEAN_BURN = db.Column(String)
    PRIMARY_FUEL_TYPE = db.Column(String)


class Transmission(db.Model):

    __tablename__ = "transmission"

    id = db.Column(db.Integer, primary_key=True)
    VEHICLE_ID = db.Column(db.String,db.ForeignKey('vehicle.VEHICLE_ID'))
    TOTAL_NO_OF_AXELS = db.Column(String)
    NO_OF_DRIVE_AXELS = db.Column(String)
    TRANSMISSION_TYPE = db.Column(String)
    SPEEDS = db.Column(String)
    MANUFACTURER = db.Column(String)
    HYBRID_TECH = db.Column(Boolean,default=False,nullable=True)
    HYBRID_TECH_COMMENTS = db.Column(String)


class Owner(db.Model):

    __tablename__ = "owner"

    id = db.Column(db.Integer, primary_key=True)
    VEHICLE_ID = db.Column(db.String,db.ForeignKey('vehicle.VEHICLE_ID'))
    FLEET_OWNER = db.Column(String)
    CONTACT_PERSON = db.Column(String)
    ADDRESS = db.Column(String)
    PHONE_NUMBER = db.Column(String)
    EMAIL = db.Column(String)
