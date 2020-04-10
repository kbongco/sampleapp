from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databasesetup import Base, samples

engine = create_engine('sqlite:///totalsamples.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Dummy Sample Data

samples1 = samples(lotnumber ='123456789',
samplename = 'some candy', devname ='Sky',
samplesubmitdate = '04/10/2020', testsreq ='hardness, micro',
other ="do visual tests")

session.add(samples1)
session.commit()

print('Dummy data entered!')