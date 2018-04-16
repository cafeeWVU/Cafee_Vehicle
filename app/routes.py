from flask import url_for, redirect,render_template,flash,request
from werkzeug.urls import url_parse

from app import app

from app.forms import VehicleForm,SearchForm,LoginForm,EngineForm,TransmissionForm,OwnerForm
from app import db
from app.models import Vehicle,User,Engine,Transmission,Owner
from flask_login import current_user, login_user,logout_user,login_required

from tables import VehicleResults,EngineResults,TransmissionResults, OwnerResults

@app.route('/')
@app.route('/index')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:

        return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
     if current_user.is_authenticated:
        return home()
     form = LoginForm(request.form)
     if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print user
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return render_template('index.html')

     return render_template('login.html',title = 'Sign In',form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

#####Vehicle##########

@app.route("/vehicle",methods=['GET','POST'])
@login_required
def vehicle():
    #print(request.form['VEHICLE_ID'])
    #if not db.session['logged_in']:
    #    return home()
    form = VehicleForm(request.form)

    if form.validate_on_submit():

        vehicle = Vehicle()
        save_changes_vehicle(vehicle,form,True)
        flash('Vehicle Added')
        return home()

    return render_template('vehicle.html',title='Vehicle',form=form)

def save_changes_vehicle(vehicle,form,new=False):

    vehicle.VEHICLE_ID = form.VEHICLE_ID.data
    vehicle.VEHICLE_TYPE = form.VEHICLE_TYPE.data or ''
    vehicle.CABIN_TYPE = form.CABIN_TYPE.data or ''
    vehicle.MANUFACTURER = form.MANUFACTURER.data or ''
    vehicle.MODEL = form.MODEL.data or ''
    vehicle.MODEL_YEAR = form.MODEL_YEAR.data or ''
    vehicle.VIN = form.VIN.data
    vehicle.GVWR = form.GVWR.data
    vehicle.TOTAL_MILES = form.TOTAL_MILES.data
    vehicle.AGENCY_VEHICLE_NUMBER = form.AGENCY_VEHICLE_NUMBER.data or ''
    vehicle.LICENSE_PLATE = form.LICENSE_PLATE.data
    vehicle.OEM_COMMENTS = form.OEM_COMMENTS.data or ''
    vehicle.AQMD_CATEGORY = form.AQMD_CATEGORY.data or ''
    vehicle.EMA_CATEGORY = form.EMA_CATEGORY.data or ''

    if new:
        db.session.add(vehicle)

    db.session.commit()

@app.route('/editVehicle/<int:id>', methods=['GET', 'POST'])
@login_required
def editVehicle(id):
    qry = db.session.query(Vehicle).filter(
                Vehicle.VEHICLE_ID==id)
    vehicle = qry.first()

    if vehicle:
        form = VehicleForm(formdata=request.form, obj=vehicle)
        if request.method == 'POST' and form.validate():
            # save edits

            #db.session.add(vehicle)
            save_changes_vehicle(vehicle,form)
            #return 'Added'
            flash('Updated successfully!')
            return redirect('vehicle')
        return render_template('editVehicle.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/delete_vehicle/<int:id>', methods=['GET', 'POST'])
def delete_vehicle(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db.session.query(Vehicle).filter(
        Vehicle.VEHICLE_ID==id)
    vehicle = qry.first()
    if vehicle:
        form = VehicleForm(formdata=request.form, obj=vehicle)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db.session.delete(vehicle)
            db.session.commit()
            flash('Deleted successfully!')
            return redirect('vehiclesearch')
        return render_template('delete_vehicle.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)

##########engine###############

@app.route("/engine",methods=['GET','POST'])
@login_required
def engine():
    #print(request.form['VEHICLE_ID'])
    #if not db.session['logged_in']:
    #    return home()
    form = EngineForm(request.form)

    if request.method== 'POST' and form.validate_on_submit():
        engine= Engine()
        save_changes(engine,form,True)


        flash('engine Added')
        return 'Engine Added'
    #return home()

    return render_template('engine.html',title='Engine',form=form)
def save_changes( engine,form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    engine.VEHICLE_ID = form.VEHICLE_ID.data
    engine.MANUFACTURER = form.MANUFACTURER.data or ''
    engine.ENGINE_MODEL = form.ENGINE_MODEL.data or ''
    engine.ENGINE_YEAR = form.ENGINE_YEAR.data or ''
    engine.SERIAL = form.SERIAL.data
    engine.EPA_FAMILY_CERT = form.EPA_FAMILY_CERT.data or ''
    engine.DISPLACEMENT = form.DISPLACEMENT.data or ''
    engine.NUMBER_OF_CYLINDERS = form.NUMBER_OF_CYLINDERS.data or ''
    engine.CONFIGURATION = form.CONFIGURATION.data or ''
    engine.IDLE_SPEED = form.IDLE_SPEED.data or ''
    engine.GOVERNED_SPEED = form.GOVERNED_SPEED.data or ''
    engine.HIGH_IDLE = form.HIGH_IDLE.data or ''
    engine.REFERENCE_TORQUE = form.REFERENCE_TORQUE.data or ''
    engine.ENGINE_REBUILT = form.ENGINE_REBUILT.data or ''
    engine.YEAR_OF_REBUILT = form.YEAR_OF_REBUILT.data or ''
    engine.ECU_PROTOCOL = form.ECU_PROTOCOL.data or ''
    engine.STOIC_LEAN_BURN = form.STOIC_LEAN_BURN.data or ''
    engine.PRIMARY_FUEL_TYPE = form.PRIMARY_FUEL_TYPE.data or ''

    #engine = Engine(VEHICLE_ID,MANUFACTURER,ENGINE_MODEL,ENGINE_YEAR,SERIAL,EPA_FAMILY_CERT,DISPLACEMENT,NUMBER_OF_CYLINDERS,CONFIGURATION,
    #                IDLE_SPEED,GOVERNED_SPEED,HIGH_IDLE,REFERENCE_TORQUE,ENGINE_REBUILT,YEAR_OF_REBUILT,ECU_PROTOCOL,STOIC_LEAN_BURN,PRIMARY_FUEL_TYPE)

    if new:
        # Add the new album to the database
        #db.session.delete(engine)
        db.session.add(engine)

    # commit the data to the database
    db.session.commit()

@app.route('/edit_engine/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_engine(id):
    qry = db.session.query(Engine).filter(
                Engine.VEHICLE_ID==id)
    engine = qry.first()

    if engine:
        form = EngineForm(formdata=request.form, obj=engine)
        if request.method == 'POST' and form.validate():

            # save edits

            save_changes(engine,form)
            flash('updated successfully!')
            return 'Added'

        return render_template('edit_engine.html',id = engine.VEHICLE_ID,form = form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/delete_engine/<int:id>', methods=['GET', 'POST'])
def delete_engine(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db.session.query(Engine).filter(
        Engine.VEHICLE_ID==id)
    engine = qry.first()
    if engine:
        form = EngineForm(formdata=request.form, obj=engine)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db.session.delete(engine)
            db.session.commit()
            flash('Album deleted successfully!')
            return redirect('/')
        return render_template('delete_engine.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)
###########end Engien####################

##############transmission###################

@app.route("/transmission",methods=['GET','POST'])
@login_required
def transmission():
    #print(request.form['VEHICLE_ID'])
    #if not db.session['logged_in']:
    #    return home()
    form = TransmissionForm(request.form)

    if request.method== 'POST' and form.validate_on_submit():
        transmission= Transmission()
        save_changes_transmission(transmission,form,True)


        flash('Transmission Added')
        return 'Transmission Added'
    #return home()

    return render_template('transmission.html',title='Transmission',form=form)
def save_changes_transmission( transmission,form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    print(transmission.HYBRID_TECH)
    transmission.VEHICLE_ID = form.VEHICLE_ID.data
    transmission.TOTAL_NO_OF_AXELS = form.TOTAL_NO_OF_AXELS.data or ''
    transmission.NO_OF_DRIVE_AXELS = form.NO_OF_DRIVE_AXELS.data or ''
    transmission.TRANSMISSION_TYPE = form.TRANSMISSION_TYPE.data or ''
    transmission.SPEEDS = form.SPEEDS.data or ''
    transmission.HYBRID_TECH = True if form.HYBRID_TECH else False
    transmission.HYBRID_TECH_COMMENTS = form.HYBRID_TECH_COMMENTS.data or ''


    if new:
        db.session.add(transmission)

    # commit the data to the database
    db.session.commit()

@app.route('/edit_transmission/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_transmission(id):
    qry = db.session.query(Transmission).filter(
                Transmission.VEHICLE_ID==id)
    transmission = qry.first()

    if transmission:
        form = TransmissionForm(formdata=request.form, obj=transmission)
        if request.method == 'POST' and form.validate():

            # save edits

            save_changes_transmission(transmission,form)
            flash('updated successfully!')
            return 'Added'

        return render_template('edit_transmission.html',id = transmission.VEHICLE_ID,form = form)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route('/delete_transmission/<int:id>', methods=['GET', 'POST'])
def delete_transmission(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db.session.query(Transmission).filter(
        Transmission.VEHICLE_ID==id)
    transmission = qry.first()
    if transmission:
        form = TransmissionForm(formdata=request.form, obj=transmission)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db.session.delete(transmission)
            db.session.commit()
            flash('Album deleted successfully!')
            return redirect('/')
        return render_template('delete_transmission.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)
###########end#########################

############owner ####################
@app.route("/owner",methods=['GET','POST'])
@login_required
def owner():
    #print(request.form['VEHICLE_ID'])
    #if not db.session['logged_in']:
    #    return home()
    form = OwnerForm(request.form)

    if request.method== 'POST' and form.validate_on_submit():
        owner= Owner()
        save_changes_owner(owner,form,True)


        flash('Owner Added')
        return home()
    #return home()

    return render_template('owner.html',title='Owner',form=form)
def save_changes_owner( owner,form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object

    owner.VEHICLE_ID = form.VEHICLE_ID.data
    owner.FLEET_OWNER = form.FLEET_OWNER.data or ''
    owner.CONTACT_PERSON = form.CONTACT_PERSON.data or ''
    owner.ADDRESS = form.ADDRESS.data or ''
    owner.PHONE_NUMBER = form.PHONE_NUMBER.data or ''
    owner.EMAIL =form.EMAIL.data or ''


    if new:
        db.session.add(owner)

    # commit the data to the database
    db.session.commit()

@app.route('/edit_owner/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_owner(id):
    qry = db.session.query(Owner).filter(
                Owner.VEHICLE_ID==id)
    owner = qry.first()

    if owner:
        form = OwnerForm(formdata=request.form, obj=owner)
        if request.method == 'POST' and form.validate():

            # save edits

            save_changes_owner(owner,form)
            flash('updated successfully!')
            return home()

        return render_template('edit_owner.html',id = owner.VEHICLE_ID,form = form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/delete_owner/<int:id>', methods=['GET', 'POST'])
def delete_owner(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db.session.query(Owner).filter(
            Owner.VEHICLE_ID==id)
    owner= qry.first()
    if owner:
        form = OwnerForm(formdata=request.form, obj=owner)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db.session.delete(owner)
            db.session.commit()
            flash('Album deleted successfully!')
            return redirect('/')
        return render_template('delete_owner.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)


#############end##########################

###########Searching the Database##################
@app.route("/vehiclesearch",methods=['GET','POST'])
@login_required
def vehiclesearch():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('vehiclesearch.html', form=search)

@app.route('/results')
@login_required
def search_results(search):
    results = []
    search_string = search.data['search']
    print search.data
    if search.data['search'] == '' and search.data['select'] == 'Vehicle':
        qry = Vehicle.query
        results = qry.all()
        table = VehicleResults(results)


    if search.data['search'] == '' and search.data['select'] == 'Engine':
        qry = Engine.query
        results = qry.all()
        table = EngineResults(results)

    if search.data['search'] == '' and search.data['select'] == 'Transmission':
        qry = Transmission.query
        results = qry.all()
        table = TransmissionResults(results)



    if not results:
        flash('No results found!')
        return redirect('vehiclesearch')
    else:
        # display results
        return render_template('results.html', table = table)


###################end##################################




if __name__ == "__main__":
    app.secret_key = 'os.urandom(12)'
    app.run(debug=True)
