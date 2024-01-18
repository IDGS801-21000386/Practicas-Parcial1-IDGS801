"""
EJERCICIO 1
IMPRIMIR ESCALERA CON *
"""

class escalera:
    # Declaracion de propiedades
    n_escaleras = 0

    # Declaracion de constructor
    def __init__(self, a):
        self.n_escaleras = a

    # Metodos de prueba
    def imprimir(self):
        for i in range(self.n_escaleras + 1):
            print('*' * i)

def main():
    n_escalera = int(input("Ingresa un numero: "))
    obj = escalera(n_escalera)
    obj.imprimir()

if __name__ == "__main__":
    main()
