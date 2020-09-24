from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Search")
