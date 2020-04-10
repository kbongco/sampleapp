import os

from flask import Flask
from flask import render_template, url_for
from flask import request
from tables import AllSamples

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sql:///{}".format(os.path.join(project_dir, "sample.db"))
SQLALCHEMY_TRACK_MODIFICATIONS = False 


app = Flask(__name__, template_folder = 'templates')
app.config["SQLALCHEMY_DATBASE_URI"] = database_file
db = SQLAlchemy(app)

class samples(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lotnumber = db.Column(db.String(100), unique = True, nullable = False)
    samplename = db.Column(db.String(100), unique = False, nullable = False)
    name = db.Column(String(100), unique = False, nullable = False)
    submissiondate = db.Column(db.String(100), nullable = False)
    tests = db.Column(db.String(150), nullable = False)




@app.route('/')
def home():
    return render_template('base.html')

@app.route('/view')
def samples():
    if request.form:
        viewsamples = session.query(samples).all()
        return render_template('view.html', viewsamples = viewsamples)

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        newsample = samples(lotnumber = request.form['lotnumber'],
        samplename = request.form['samplename'],
        name = request.form['name'],
        submissiondate = request.form['submission'],
        testrequired = request.form['tests'])

        session.add(newsample)
        session.commit()
        return redirect(url_for('samples', newsample = newsample))
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug = True)