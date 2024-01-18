"""
EJERCICIO 2 
ORDENAR LISTAS
"""

class ListaOrdenada:
    def __init__(self):
        self.lista = []

    def lista_length(self, cantidad):
        for i in range(cantidad):
            n = int(input(f"Ingrese el numero {i + 1}: "))
            self.lista.append(n)

    def ordenar_lista(self):
        self.lista.sort()        

    def obtener_lista(self):
        return self.lista
    
    def contar_repetidos(self):
        ocurrencias = {}
        for elemento in self.lista:
            if elemento in ocurrencias:
                ocurrencias[elemento] += 1
            else:
                ocurrencias[elemento] = 1

        repetidos = {elemento: cantidad for elemento, cantidad in ocurrencias.items() if cantidad > 1}
        return repetidos

    
class ListaOrdenadaPares:
    def __init__(self):
        self.listaPares = []

    def lista_length(self, cantidad):
        for i in range(cantidad):
            n = int(input(f"Ingrese el numero {i + 1}: "))
            self.listaPares.append(n)

    def ordenar_lista(self):
        # Filtrar los números pares de la lista original
        listaP = []
        for n in self.listaPares:
            if n % 2 == 0:
                listaP.append(n)
        self.listaPares.clear()
        self.listaPares.extend(listaP) 
        self.listaPares.sort()

    def obtener_lista(self):
        return self.listaPares
    
class ListaOrdenadaImpares:
    def __init__(self):
        self.listaImpares = []

    def lista_length(self, cantidad):
        for i in range(cantidad):
            n = int(input(f"Ingrese el numero {i + 1}: "))
            self.listaImpares.append(n)

    def ordenar_lista(self):
        # Filtrar los números pares de la lista original
        listaIm = []
        for n in self.listaImpares:
            if n % 2 != 0:
                listaIm.append(n)
        self.listaImpares.clear()
        self.listaImpares.extend(listaIm) 
        self.listaImpares.sort()


    def obtener_lista(self):
        return self.listaImpares
    

def main():
    cantidadNumLista = int(input("De cuántos números quieres la lista: "))
    lista_ordenada = ListaOrdenada()
    lista_ordenada.lista_length(cantidadNumLista)
    lista_ordenada.ordenar_lista()
    print("LISTA ORDENADA:", lista_ordenada.obtener_lista())
    #print("NUMEROS REPETIDOS DE LA LISTA: ")
    #print(lista_ordenada.contar_repetidos())

    # LISTA PARES
    lista_ordenada_pares = ListaOrdenadaPares()
    lista_ordenada_pares.lista_length(cantidadNumLista)
    lista_ordenada_pares.ordenar_lista()
    print("LISTA ORDENADA POR PARES:", lista_ordenada_pares.obtener_lista())
    
    # LISTA IMPARES
    lista_ordenada_impares = ListaOrdenadaImpares()
    lista_ordenada_impares.lista_length(cantidadNumLista)
    lista_ordenada_impares.ordenar_lista()
    print("LISTA ORDENADA POR POR IMPARES:", lista_ordenada_impares.obtener_lista())

if __name__ == "__main__":
    main()
