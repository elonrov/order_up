from flask_wtf import FlaskForm
from wtforms.fields import (
  PasswordField, SelectField, SelectMultipleField, StringField, SubmitField
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  employee_number = StringField("Employee Number", [DataRequired()])
  password = PasswordField("Password", [DataRequired()])
  submit = SubmitField("Login")