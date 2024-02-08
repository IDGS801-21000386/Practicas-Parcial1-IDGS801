from wtforms import Form
from wtforms import EmailField
from wtforms import StringField, TelField, IntegerField, SelectField, RadioField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email


class DistanciaForm(Form):
    x1 = IntegerField("x1")
    x2 = IntegerField("x2")
    y1 = IntegerField("y1")
    y2 = IntegerField("y2")

class ResistenciaForm(Form):
    colores = [
        (0, "Negro"), 
        (1, "Café"), 
        (2, "Rojo"), 
        (3, "Naranja"), 
        (4, "Amarillo"), 
        (5, "Verde"), 
        (6, "Azul"), 
        (7, "Violeta"), 
        (8, "Gris"), 
        (9, "Blanco")
    ]

    tolerancias = {
        "dorado": 0.05,
        "plateado": 0.1
    }
    
    # Define los campos SelectField con las opciones de colores
    c1 = SelectField("c1", choices=colores)
    c2 = SelectField("c2", choices=colores)
    c3 = SelectField("c3", choices=colores)
    tolerancia = RadioField("tolerancia", choices=[(0.05, "Dorado"), (0.1, "Plateado")])

