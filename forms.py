from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class SignupForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
