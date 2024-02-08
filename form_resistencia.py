from wtforms import Form
from wtforms import EmailField
from wtforms import StringField, TelField, IntegerField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email


class ResistenciaForm(Form):
    color1 = IntegerField("c1")
    color2 = IntegerField("c2")
    color3 = IntegerField("c3")
