from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, StringField, DateField
from wtforms.validators import DataRequired, ValidationError

import datetime


def date_validation(form, field):
    """ Validation of date provided by the user"""
    try:
        field.data = datetime.datetime.strptime(field.data, '%d/%m/%Y')
        field.data = field.data.strftime('%d/%m/%Y')
    except ValueError:
        raise ValidationError('Date format error')

class EntryForm(FlaskForm):
    title = StringField(
        'Title', 
        validators=[DataRequired()]
    )
    date = StringField(
        'Date format dd/mm/yyyy', 
        validators=[DataRequired(), date_validation]
        )
    time_spent = IntegerField(
        'Time spent in minutes (integer)', 
        validators=[DataRequired()]
    )
    learned = TextAreaField('Learned', 
    validators=[DataRequired()]
    )
    resources = TextAreaField(
        'Resources', validators=[DataRequired()]
    )