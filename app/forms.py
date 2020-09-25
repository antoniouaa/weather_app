from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    location = StringField("Location", validators=[DataRequired()])
