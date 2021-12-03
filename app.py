from flask import Flask, render_template, request,session, url_for, flash, send_from_directory, request,json, jsonify
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from car import CarController, Car, carData

import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__) # Create the flask object
app.secret_key = 'ict2x01' #secretkey need to set for session
app.config['UPLOAD_FOLDER'] = 'Data'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carData.sqlite3'

db = SQLAlchemy(app)


db.create_all()

#page that car retrieve command
@app.route('/car') 
def carCommand():
    return render_template('car.html', carData = carData.query.all())

#page that displays car data
@app.route('/carData')
def show_data():
   return render_template('carData.html', carData = carData.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def instruction():
    if request.method == 'POST':
        postData = request.form
        command = str(postData['command'])
        car = carData(command=command, speed="0",distance="0",status="executing")
        db.session.query(carData).delete()
        db.session.commit()
        db.session.add(car)
        db.session.commit()
        CarController.executeInstruction(car)
        return render_template('dashboard.html')

    elif request.method == 'GET':
        command = request.args.get('command')
        speed = request.args.get('speed')
        distance = request.args.get('distance')
        status = request.args.get('status')
        car = carData(command=command,speed=speed,distance=distance,status=status)
        db.session.query(carData).delete()
        db.session.commit()
        db.session.add(car)
        db.session.commit()

        CarController.sendData(car)
        return render_template('dashboard.html')

         
    

@app.route('/')
def default():
    return render_template('index.html', session=0)

@app.route('/index.html', methods=['GET', 'POST'])
def connect():
    session.pop('ip', None)
    return render_template('index.html', session=0)

@app.route('/dashboard.html', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        ip = request.form['ip']
        if ip == "192.168.1.1":
            #store ip address in session if correct ip
            session['ip'] = ip
            car = carData(command="", speed="0",distance="0",status="connected") 
            db.session.query(carData).delete()
            db.session.commit()
            db.session.add(car)
            db.session.commit()
            return render_template('dashboard.html', session=1, carData = carData.query.all())
        else:
            flash('Invalid IP!')
            return redirect(url_for('connect'))

    if session.get("ip") is None:
        flash('Not authenticated!')
        return redirect(url_for('connect'))
    elif session['ip'] == "192.168.1.1":
        return render_template('dashboard.html', session=1, carData = carData.query.all())

@app.route('/challenge1.html')
def challenge1():
    #to check for session id for everypage
    if session.get("ip") is None:
        flash('Not authenticated!')
        return redirect(url_for('connect'))
    elif session['ip'] == "192.168.1.1":
        return render_template('challenge1.html', session=1)
        

@app.route('/challenge2.html')
def challenge2():
    #to check for session id for everypage
    if session.get("ip") is None:
        flash('Not authenticated!')
        return redirect(url_for('connect'))
    elif session['ip'] == "192.168.1.1":
        return render_template('challenge2.html', session=1)
    # return render_template('challenge2.html', session=1)

@app.route('/challenge3.html')
def challenge3():
    #to check for session id for everypage
    if session.get("ip") is None:
        flash('Not authenticated!')
        return redirect(url_for('connect'))
    elif session['ip'] == "192.168.1.1":
        return render_template('challenge3.html', session=1)
    # return render_template('challenge3.html', session=1)

@app.route('/viewchallenges.html')
def viewchallenges():
     #to check for session id for everypage
    if session.get("ip") is None:
        flash('Not authenticated!')
        return redirect(url_for('connect'))
    elif session['ip'] == "192.168.1.1":
        return render_template('viewchallenges.html', session=1)
        
    # return render_template('viewchallenges.html', session=1)





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")