from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField,BooleanField, SubmitField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired

class VehicleForm(FlaskForm):
    VEHICLE_ID =  StringField('Vehicle ID',validators=[DataRequired()])
    VEHICLE_TYPE = StringField('Vehicle TYPE')
    CABIN_TYPE =  StringField('Cabin Type')
    MANUFACTURER =  StringField('Manufacturer')
    MODEL=  StringField('Model')
    MODEL_YEAR =  StringField('Model Year')
    VIN =  StringField('Vin ',validators=[DataRequired()])
    GVWR =  StringField('GVWR(lbs)')
    TOTAL_MILES =  StringField('Total Miles',validators=[DataRequired()])
    AGENCY_VEHICLE_NUMBER =  StringField('Agency Vehicle Number')
    LICENSE_PLATE =  StringField('License Plate',validators=[DataRequired()])
    OEM_COMMENTS =  StringField('OEM Comments')
    AQMD_CATEGORY =  StringField('AQMD Category')
    EMA_CATEGORY =  StringField('EMA Category')

    submit = SubmitField('Save')

class SearchForm(FlaskForm):
    choices = [('Vehicle', 'Vehicle'),('Engine','Engine'),('Transmission','Transmission')]
    select = SelectField('Search for Vehicle Information:', choices=choices)
    search = StringField('')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class EngineForm(FlaskForm):
    VEHICLE_ID =  StringField('Vehicle ID',validators=[DataRequired()])
    MANUFACTURER = StringField('Manufacturer')
    ENGINE_MODEL =  StringField('Engine Model')
    ENGINE_YEAR =  StringField('Engine Year')
    SERIAL=  StringField('Serial',validators=[DataRequired()])
    EPA_FAMILY_CERT =  StringField('EPA Family Cert')
    DISPLACEMENT =  StringField('Displacement ')
    NUMBER_OF_CYLINDERS =  StringField('No of Cylinders')
    CONFIGURATION =  StringField('Configuration')
    IDLE_SPEED =  StringField('Idle Speed')
    GOVERNED_SPEED =  StringField('Governed Speed')
    HIGH_IDLE =  StringField('High Idle')
    REFERENCE_TORQUE =  StringField('Reference Torque')
    ENGINE_REBUILT =  StringField('Engine Rebuilt')
    YEAR_OF_REBUILT =  StringField('Year of Rebuilt')
    ECU_PROTOCOL =  StringField('ECU Protocol')
    STOIC_LEAN_BURN =  StringField('Stoic/Lean Burn')
    PRIMARY_FUEL_TYPE =  StringField('Primary Fuel Type')


    submit = SubmitField('Save')

class TransmissionForm(FlaskForm):
    VEHICLE_ID =  StringField('Vehicle ID',validators=[DataRequired()])
    TOTAL_NO_OF_AXELS = StringField('Total No Of Axels')
    NO_OF_DRIVE_AXELS =  StringField('No Of Drive Axels')
    TRANSMISSION_TYPE = StringField('Transmission Type')
    SPEEDS =  StringField('Speeds')
    MANUFACTURER=  StringField('Manufacturer')
    HYBRID_TECH =  BooleanField('Hybrid Tech')
    HYBRID_TECH_COMMENTS=  StringField('Hybrid Tech Comments ')



    submit = SubmitField('Save')

class OwnerForm(FlaskForm):
    VEHICLE_ID =  StringField('Vehicle ID',validators=[DataRequired()])
    FLEET_OWNER = StringField('Fleet Owner')
    CONTACT_PERSON =  StringField('Contact Person')
    ADDRESS = StringField('Address')
    PHONE_NUMBER =  StringField('Phone Number')
    EMAIL=  StringField('Email')
    

    submit = SubmitField('Save')
