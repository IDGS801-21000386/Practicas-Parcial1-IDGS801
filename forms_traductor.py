from io import open
from wtforms import Form, EmailField, validators
from wtforms import StringField, TelField, IntegerField, RadioField
from flask_wtf import FlaskForm

"""
archivo1 = open("archivo.txt", "a") # Para poder escribir sobre el archivo
archivo1.write("HOLAAAAAAAAAAAAAAAAAAAA SALUDOS DE ERICK")
archivo1.close()
"""


"""
archivo1 = open("archivo.txt", "r") # Para solo lectura
print(archivo1.read())
archivo1.seek(0) # Para que vuelva desde la posicion 0 del archivo
print(archivo1.read())
"""

"""
# print(archivo1.readlines()) #Lo lee todo dentro de una sola linea mediante []
for datos in archivo1: # Imprime linea por linea los datos que se encuentren en el archivo
    #print(datos)
    print(datos.rstrip())
archivo1.close()
"""

class TraductorForms(Form):
    ingles = StringField("ingles", [
        validators.DataRequired(message="El campo es requerido")
    ])
    espaniol = StringField("espaniol", [
        validators.DataRequired(message="El campo es requerido")
    ])

class TraductorForms2(Form):
    traducir = RadioField("traducir", choices=[(0, "espaniol"), (1, "ingles")])
    texto = StringField("texto", [
        validators.DataRequired(message="El campo es requerido")
    ])        

def insertar(ingles, espaniol):
    archivo1 = open("archivoInglesEspaniol.txt", "a") # Para poder escribir sobre el archivo
    archivo1.write(f"{ingles}")
    archivo1.write(f",{espaniol}\n")
    archivo1.close()

def buscar(buscar, opcion):
    archivo1 = open("archivoInglesEspaniol.txt", "r") # Para solo lectura
    resultado = ""
    
    buscar = buscar.strip().lower()
    print(buscar)

    if (opcion == "0"):
        print("ESPAÑOOOOOL")
        for linea in archivo1:
            palabras = linea.strip().split(",")  
            print(palabras)
            if buscar == palabras[0].strip().lower(): 
                resultado = palabras[1].strip() 
                break
            elif buscar == palabras[1].strip().lower(): 
                resultado = palabras[1].strip()  
                break
    elif (opcion == "1"):        
        print("INGLEEEEES")
        for linea in archivo1:
            palabras = linea.strip().split(",")  
            print(palabras)
            if buscar == palabras[1].strip().lower(): 
                resultado = palabras[0].strip() 
                break
            elif buscar == palabras[0].strip().lower(): 
                resultado = palabras[0].strip()  
                break
    

    archivo1.close() 
    return resultado