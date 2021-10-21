from flask import Flask, render_template, request, url_for, flash, send_from_directory
from werkzeug.utils import redirect
import sort
import os
import PlotChart

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__) # Create the flask object
app.config['UPLOAD_FOLDER'] = 'Data'

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/upload.html', methods=['GET', 'POST'])
def upload():
    url ='/upload.html'
    if request.method == 'POST':
        uploaded_file = request.files['dataupload']
        full_path = os.path.join(basedir, app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        if uploaded_file.filename != '':
            uploaded_file.save(full_path)
            sort.main(full_path)
        #return redirect(url_for('select'))
    return render_template('upload.html', url=url)

@app.route('/uploaded.html' , methods=['GET', 'POST'])
def select():
    return render_template('uploaded.html')

@app.route('/TestData.html')
def viewData():
    return render_template('TestData.html')
@app.route('/Ram.html')
def ram():
    ramtable = PlotChart.plotRamTable()
    return render_template("Ram.html", ramtable=ramtable)
@app.route('/Network.html')
def network():
    routingtable = PlotChart.plotRoutingTable()
    # kernelinterfacetable = PlotChart.plotKernelInterfaceTable()
    return render_template("Network.html", routingtable=routingtable)
@app.route('/Processes.html')
def processes():
    services = PlotChart.printServices()
    # ramtable = PlotChart.plotRamTable()
    return render_template("Processes.html", services=services)

@app.route('/Dashboard.html')
def Dashboard():
    # services = PlotChart.printServices()
    # ramtable = PlotChart.plotRamTable()
    ramtable = PlotChart.plotRamTable()
    return render_template("Dashboard.html", ramtable=ramtable)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")