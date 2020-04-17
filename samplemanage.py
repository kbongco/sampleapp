import os

from flask import Flask
from flask import render_template, url_for,redirect, flash
from flask import request
from tables import AllSamples

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databasesetup import Base, samples

app = Flask(__name__)
app.secret_key = 'super_secret_key'
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
    Samples = session.query(samples).all()
    return render_template('view.html', Samples = Samples)

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
    
    edits = session.query(samples).filter_by(id = sample_id).one()
    
    if request.method == 'POST':
        if request.form['lotnumber']:
            edits.lotnumber = request.form['lotnumber']
        if request.form['samplename']:
            edits.samplename = request.form['samplename']
        if request.form['devname']:
            edits.devname = request.form['devname']
        if request.form['submitdate']:
            edits = request.form['submitdate']
        if request.form['tests']:
            edits == request.form['tests']
        if request.form['otherhere']:
            edits == request.form['otherhere']

        session.add(edits)
        session.commit()
        flash('You have edited your sample')
        return redirect(url_for('viewall', sample_id = sample_id))
    else:
        return render_template('edit.html', sample_id = sample_id, s = editsample)

@app.route('/view/<int:sample_id>/delete', methods = ['GET', 'POST'])
def deletesample(sample_id):
    deletesamples = session.query(samples).filter_by(id = sample_id).one()
    if request.method == 'POST':
        session.delete(deletesamples)
        session.commit()
        return redirect(url_for('viewall'))






if __name__ == '__main__':
    app.run(debug = True)