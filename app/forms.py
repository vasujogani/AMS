from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    nincidents = StringField('Incidents', validators=[DataRequired()])
    nrfc = StringField('RFC', validators=[DataRequired()])
    nalerts = StringField('Alerts', validators=[DataRequired()])
    people = StringField('Who is in the office? (comma separated number)', validators=[DataRequired()])
    reset = BooleanField('Reset count')
    showcount= BooleanField('Show count')
    submit = SubmitField('Submit')
