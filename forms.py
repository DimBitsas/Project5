from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, StringField, DateField
from wtforms.validators import DataRequired, ValidationError

import datetime


class EntryForm(FlaskForm):
    title = StringField(
        'Title', 
        validators=[DataRequired()]
    )
    date = DateField(
        'Date', 
        validators=[DataRequired()
    ])
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