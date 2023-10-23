# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:00:03 2023
@author: Candelaria
"""

class Monticulo_Min:
    def __init__(self):
        """
        Inicializa un montículo mínimo vacío.

        Un montículo mínimo (o min-heap) es una estructura de datos en la que el elemento en la cima
        del montículo es el elemento más pequeño en el conjunto. Se utiliza un montículo mínimo para
        mantener un conjunto de elementos con eficiencia en las operaciones de inserción y eliminación
        del elemento mínimo.
        """
        self.listaMonticulo = [0]  # La listaMonticulo se inicializa con un valor ficticio en la posición 0

    def insertar(self, k):
        """
        Inserta un elemento en el montículo mínimo.

        :param k: El elemento que se va a insertar en el montículo.
        """
        self.listaMonticulo.append(k)  # Agrega el elemento al final de la listaMonticulo
        self.subir(len(self.listaMonticulo) - 1)  # Llama a la función subir para restaurar la propiedad del montículo

    def eliminarMin(self):
        """
        Elimina y devuelve el elemento mínimo del montículo mínimo.

        :return: El elemento mínimo del montículo, o None si el montículo está vacío.
        """
        if len(self.listaMonticulo) > 1:
            minimo = self.listaMonticulo[1]  # El mínimo está en la posición 1
            ultimo = self.listaMonticulo.pop()  # Elimina el último elemento de la lista
            if len(self.listaMonticulo) > 1:
                self.listaMonticulo[1] = ultimo  # Mueve el último elemento a la cima del montículo
                self.bajar(1)  # Llama a la función bajar para restaurar la propiedad del montículo
            return minimo
        return None

    def estaVacio(self):
        """
        Comprueba si el montículo mínimo está vacío.

        :return: True si el montículo está vacío, False en caso contrario.
        """
        return len(self.listaMonticulo) == 1  # El montículo está vacío si tiene un solo elemento ficticio.

    def tamanio(self):
        """
        Devuelve el número de elementos en el montículo mínimo.

        :return: El número de elementos en el montículo.
        """
        return len(self.listaMonticulo) - 1  # Resta uno para excluir el elemento ficticio.

    def subir(self, i):
        """
        Restaura la propiedad del montículo al mover un elemento hacia arriba si es necesario.

        :param i: La posición del elemento que se desea subir en el montículo.
        """
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2

    def bajar(self, i):
        """
        Restaura la propiedad del montículo al mover un elemento hacia abajo si es necesario.

        :param i: La posición del elemento que se desea bajar en el montículo.
        """
        while (i * 2) <= self.tamanio():
            hijoMinimo = self.encontrarHijoMinimo(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hijoMinimo]:
                self.listaMonticulo[i], self.listaMonticulo[hijoMinimo] = self.listaMonticulo[hijoMinimo], self.listaMonticulo[i]
            i = hijoMinimo

    def encontrarHijoMinimo(self, i):
        """
        Encuentra la posición del hijo más pequeño de un elemento en el montículo mínimo.

        :param i: La posición del elemento del cual se busca el hijo más pequeño.
        :return: La posición del hijo más pequeño.
        """
        if (i * 2 + 1) > self.tamanio():
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

if __name__ == "__main__":
    monticulo = Monticulo_Min()  # Crea un objeto de la clase Monticulo_Min

    # Inserta elementos en el montículo mínimo
    monticulo.insertar(8)
    monticulo.insertar(5)
    monticulo.insertar(20)
    monticulo.insertar(7)

    print("Eliminando elementos en orden ascendente:")
    while not monticulo.estaVacio():
        minimo = monticulo.eliminarMin()  # Elimina y muestra los elementos en orden ascendente
        print(minimo)

