from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, Regexp
import re

phoneRegex = re.compile('^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$')


class ContactForm(Form):
    name = TextField('What is your name?', validators=[Required()])
    email = TextField('Email we can contact you at?', validators=[Email(),Required()])
    phone = TextField('Phone number we can call you at?',validators=[Required(), Regexp(phoneRegex, message = 'This is an invalid phone number.')])
    message = TextAreaField('What is on your mind?', validators=[Required()])
    submit = SubmitField('Submit')
