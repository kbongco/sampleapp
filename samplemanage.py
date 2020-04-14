import os

from flask import Flask
from flask import render_template, url_for,redirect
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
def newsamples():
    if request.method == 'POST':
        newsample = samples(lotnumber = request.form['lotnumber'],
        samplename = request.form['samplename'],
        devname = request.form['devname'],
        samplesubmitdate = request.form['submitdate'],
        testsreq = request.form['tests'],
        other = request.form['otherhere'])

        session.add(newsample)
        session.commit()

        return redirect(url_for('viewall',newsample = newsample))

    else: 
        return render_template('form.html')

@app.route('/view/<int:sample_id>/edit', methods = ['GET', 'POST'])
def editsample(sample_id):
    editsamples = session.query(samples).filter_by(id = sample_id).one()

    if request.method == 'POST':
        if request.form['lotnumber']:
            editsamples.lotnumber = request.form['lotnumber']
        if request.form['samplename']:
            editsamples.samplename = request.form['samplename']
        if request.form['devname']:
            editsamples.devname = request.form['devname']
        if request.form['submitdate']:
            editsamples.samplesubmitdate = request.form['submitdate']
        if request.form['tests']:
            editsamples.testsreq = request.form['tests']
        if request.form['otherhere']:
            editsamples.other = request.form['otherhere']
        
        session.add(editsamples)
        session.commit()

        return redirect(url_for('viewall'))






if __name__ == '__main__':
    app.run(debug = True)