import os

from flask import Flask
from flask import render_template, url_for
from flask import request
from tables import AllSamples

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databasesetup import Base, samples

app = Flask(__name__)
engine = create_engine('sqlite:///totalsamples.db',
connect_args = {'check_same_thread': False})

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()



@app.route('/')
def home():
    return render_template('base.html')

@app.route('/view')
def viewall():
    all = session.query(samples).all()
    return render_template('view.html', all = all)

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