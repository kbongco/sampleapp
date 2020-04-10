import sys 
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class samples(Base):
    __tablename__='sample'
    id = Column(Integer, primary_key = True)
    lotnumber = Column(String(80), nullable = False)
    samplename = Column(String(80), nullable = False)
    devname = Column(String(80),nullable = False)
    samplesubmitdate = Column(String(80), nullable = False)
    testsreq = Column(String(80), nullable = False)
    other = Column(String(80), nullable = True)

    @property
    def serialize(self):
        return{
            'lotnumber':self.lotnumber,
            'id': self.id,
            'samplename':self.samplename,
            'devname':self.devname,
            'samplesubmitdate':self.samplesubmitdate,
            'testsreq':self.testsreq,
            'other':self.other
        }

engine = create_engine('sqlite:///totalsamples.db')

Base.metadata.create_all(engine)
