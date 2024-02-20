from flask import Flask, render_template, request
import forms_distancia
import forms_traductor
# import forms_resistencia
from math import *

# Crear una instancia de la clase Flask
app = Flask(__name__)

@app.route("/traductor", methods=["GET", "POST"])
def traductor():
    ingles = ""
    espaniol = ""
    traducir = ""
    texto = ""
    resultado = ""
    traductor_clase = forms_traductor.TraductorForms(request.form)
    traductor_clase2 = forms_traductor.TraductorForms2(request.form)
    
    if request.method == "POST" and traductor_clase.validate():
        ingles = traductor_clase.ingles.data
        espaniol = traductor_clase.espaniol.data
        print(f'Ingles: {ingles}')
        print(f'Español: {espaniol}')
        forms_traductor.insertar(ingles, espaniol)

    if request.method == "POST" and traductor_clase2.validate():
        traducir = traductor_clase2.traducir.data
        texto = traductor_clase2.texto.data
    
        print(traducir)
        print(texto)
        resultado = forms_traductor.buscar(texto, traducir)
        print("Resultado" + resultado)
        
    return render_template("traductor.html", form1=traductor_clase, form2=traductor_clase2, ingles=ingles, espaniol=espaniol, traducir=traducir, texto=texto, resultado=resultado)


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


@app.route("/resistencia", methods={"GET", "POST"})
def resistencia():
    resistencia = forms_distancia.ResistenciaForm(request.form)
    c1=""
    c2=""
    c3=""
    color_c1=""
    color_c2=""
    color_c3=""
    tolerancia=0
    valorMax=0
    valorMin=0
    valor=""

    resistencia_colores = {
    0: "Negro",
    1: "Marrón",
    2: "Rojo",
    3: "Naranja",
    4: "Amarillo",
    5: "Verde",
    6: "Azul",
    7: "Violeta",
    8: "Gris",
    9: "Blanco"
    }

    resistencia_multiplicador = {
    0: 1,
    1: 10,
    2: 100,
    3: 1000,
    4: 10000,
    5: 100000,
    6: 1000000,
    7: 10000000,
    8: 100000000,
    9: 1000000000,
    }

    if request.method == "POST":
        c1 = resistencia.c1.data
        c2 = resistencia.c2.data
        c3 = resistencia.c3.data
        color_c1 = resistencia_colores[int(c1)]
        color_c2 = resistencia_colores[int(c2)]
        color_c3 = resistencia_colores[int(c3)]
        tolerancia = resistencia.tolerancia.data

        valorMax = str(c1 + c2)
        valorMax = int(valorMax)
        valorMax = valorMax * (resistencia_multiplicador[int(c3)])
        valor = valorMax

        valorTolerancia = float(tolerancia)
        tolerancia = valorTolerancia
        valorMax = valorMax + valorMax * tolerancia
        valorMin = valor - valor * tolerancia

        #valorMax = float((valor * pow(10, c3)) * (1 + tolerancia))
        #valorMin = float((valor * pow(10, c3)) * (1 - tolerancia))
        
    return render_template("resistencias.html", form = resistencia, c1=c1, c2=c2, c3=c3, tolerancia=tolerancia, valor=valor, valorMax=valorMax, valorMin=valorMin, color_c1=color_c1, color_c2=color_c2, color_c3=color_c3)

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
