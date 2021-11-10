from flask import Flask, render_template, request, url_for, flash, send_from_directory
from werkzeug.utils import redirect
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__) # Create the flask object
app.config['UPLOAD_FOLDER'] = 'Data'

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/challenge1.html')
def challenge1():
    return render_template('challenge1.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
