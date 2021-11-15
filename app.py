from flask import Flask, render_template, request,session, url_for, flash, send_from_directory
from werkzeug.utils import redirect
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__) # Create the flask object
app.secret_key = 'ict2x01' #secretkey need to set for session
app.config['UPLOAD_FOLDER'] = 'Data'

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html', methods=['GET', 'POST'])
def connect():
    session.pop('ip', None)


    return render_template('index.html')

@app.route('/dashboard.html', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        ip = request.form['ip']
        if ip == "192.168.1.1":
            #store ip address in session if correct ip
            session['ip'] = ip
            return render_template('dashboard.html')
        else:
            flash('Invalid IP!')
            return redirect(url_for('connect'))

    if session.get("ip") is None:
        flash('Not authenticated!')
        return redirect(url_for('connect'))
    elif session['ip'] == "192.168.1.1":
        return render_template('dashboard.html')            
    



@app.route('/challenge1.html')
def challenge1():
    #to check for session id for everypage
    if session.get("ip") is None:
        flash('Not authenticated!')
        return redirect(url_for('connect'))
    elif session['ip'] == "192.168.1.1":
        return render_template('challenge1.html')
        

@app.route('/challenge2.html')
def challenge2():
    return render_template('challenge2.html')

@app.route('/challenge3.html')
def challenge3():
    return render_template('challenge3.html')

@app.route('/viewchallenges.html')
def viewchallenges():
    return render_template('viewchallenges.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")