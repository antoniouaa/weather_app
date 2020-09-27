from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import BooleanField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    location = StringField("Location", validators=[DataRequired()])
    pressure = BooleanField("Pressure")
    humidity = BooleanField("Humidity")

