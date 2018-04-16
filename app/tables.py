from flask_table import Table, Col, LinkCol

class VehicleResults(Table):
    VEHICLE_ID = Col('ID')
    VEHICLE_TYPE = Col('TYPE')
    MODEL = Col('MODEL')
    MODEL_YEAR = Col('YEAR')
    VIN = Col('MODEL')
    GVWR = Col('GVWR(lbs)')
    TOTAL_MILES = Col('TOTAL MILES')
    AGENCY_VEHICLE_NUMBER = Col('Agency Vehicle Number')
    LICENSE_PLATE = Col('LICENSE PLATE')
    OEM_COMMENTS = Col('OEM COMMENTS')
    AQMD_CATEGORY = Col('AQMD CATEGORY')
    EMA_CATEGORY = Col('EMA CATEGORY')
    edit = LinkCol('Edit', 'editVehicle', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete_vehicle', url_kwargs=dict(id='id'))


class EngineResults(Table):
    VEHICLE_ID = Col('ID')
    MANUFACTURER = Col('MANUFACTURER')
    ENGINE_MODEL = Col('MODEL')
    ENGINE_YEAR = Col('YEAR')
    SERIAL = Col('SERIAL')
    EPA_FAMILY_CERT = Col('EPA FAMILY CERT')
    DISPLACEMENT = Col('DISPLACEMENT')
    NUMBER_OF_CYLINDERS = Col('NO OF CYLINDERS')
    CONFIGURATION = Col('CONFIGURATION')
    IDLE_SPEED = Col('IDLE SPEED')
    GOVERNED_SPEED = Col('GOVERNED SPEED')
    HIGH_IDLE = Col('HIGH IDLE')
    REFERENCE_TORQUE = Col('REF TORQUE')
    ENGINE_REBUILT = Col('REBUILT')
    YEAR_OF_REBUILT = Col('YEAR REBUILT')
    ECU_PROTOCOL = Col('ECU PROTOCOL')
    STOIC_LEAN_BURN = Col('STOIC/LEAN BURN')
    PRIMARY_FUEL_TYPE = Col('PRIMARY FUEL TYPE')

    edit = LinkCol('Edit', 'edit_engine', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))

class TransmissionResults(Table):
    VEHICLE_ID = Col('ID')
    TOTAL_NO_OF_AXELS = Col('TOTAL No Of AXELS')
    NO_OF_DRIVE_AXELS = Col('No Of DRIVE AXELS')
    TRANSMISSION_TYPE = Col('TRANSMISSION TYPE')
    SPEEDS = Col('SPEEDS')
    MANUFACTURER = Col('MANUFACTURER')
    HYBRID_TECH = Col('HYBRID TECH')
    HYBRID_TECH_COMMENTS = Col('HYBRID TECH COMMENTS')


    edit = LinkCol('Edit', 'edit_transmission', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))


class OwnerResults(Table):
    VEHICLE_ID = Col('ID')
    FLEET_OWNER = Col('FLEET OWNER')
    CONTACT_PERSON = Col('CONTACT_PERSON')
    ADDRESS = Col('ADDRESS')
    PHONE_NUMBER = Col('PHONE NUMBER')
    EMAIL = Col('EMAIL')


    edit = LinkCol('Edit', 'edit_owner', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))
