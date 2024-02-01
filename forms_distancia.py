from wtforms import Form
from wtforms import EmailField
from wtforms import StringField, TelField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email


class DistanciaForm(Form):
    x1 = IntegerField("x1")
    x2 = IntegerField("x2")
    y1 = IntegerField("y1")
    y2 = IntegerField("y2")
