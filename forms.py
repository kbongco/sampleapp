from wtforms import Form, StringField, SelectField

class SampleSearchForm(Form):
    choices = [('lotnumber', 'lotnumber'),
    ('samplename', 'samplename'),
    ('devname', 'devname')]

    select = SelectField('Enter your information in:', choices = choices)

    search = StringField('')

    