from flask_table import Table, Col, LinkCol 

class AllSamples(Table):
    id = Col('Id', show = False)
    lotnumber = Col('Lot Number')
    samplename = Col('Sample Name')
    name = Col('Chemist/Developer Name')
    submissiondate = Col('Date Submitted')
    tests = Col('Tests Required')