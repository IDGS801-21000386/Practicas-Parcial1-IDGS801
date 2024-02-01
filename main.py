from flask import Flask, render_template, request
import forms_distancia
from math import *

# Crear una instancia de la clase Flask
app = Flask(__name__)

@app.route("/distancia", methods={"GET", "POST"})
def distancia():
    distancia = forms_distancia.DistanciaForm(request.form)
    x1=""
    x2=""
    y1=""
    y2=""
    resultado=""

    if request.method == "POST":
        x1 = distancia.x1.data
        x2 = distancia.x2.data
        y1 = distancia.y1.data
        y2 = distancia.y2.data
        resultado = sqrt((x2-x1)**2 + (y2-y1)**2)
        
    return render_template("distancia.html", form = distancia, x1=x1, x2=x2, y1=y1, y2=y2, resultado=resultado)

# Definir una ruta y la función asociada a esa ruta
@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        operador = request.form.get("operador")
        if operador == "+":
            return f"La suma de {n1} + {n2} = {str(int(n1) + int(n2))}"
        elif operador == "-":
            return f"La resta de {n1} - {n2} = {str(int(n1) - int(n2))}"
        elif operador == "*":
            return f"La multiplicacion de {n1} * {n2} = {str(int(n1) * int(n2))}"
        else:
            return f"La division de {n1} / {n2} = {str(int(n1) / int(n2))}"


@app.route("/operacionBasica")
def operacionBasica():
    return render_template("OperacionBasica.html")

    
# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Iniciar el servidor web incorporado de Flask en el puerto por defecto (5000)
    # Habilitar el modo de depuración para facilitar la identificación y solución de errores
    app.run(debug=True)
