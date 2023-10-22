# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:00:03 2023

@author: Candelaria
"""

class Monticulo_Min:
    def __init__(self):
        self.listaMonticulo = [0]

    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.subir(len(self.listaMonticulo) - 1)

    def eliminarMin(self):
        if len(self.listaMonticulo) > 1:
            minimo = self.listaMonticulo[1]
            ultimo = self.listaMonticulo.pop()
            if len(self.listaMonticulo) > 1:
                self.listaMonticulo[1] = ultimo
                self.bajar(1)
            return minimo
        return None

    def estaVacio(self):
        return len(self.listaMonticulo) == 1

    def tamanio(self):
        return len(self.listaMonticulo) - 1

    def subir(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2

    def bajar(self, i):
        while (i * 2) <= self.tamanio():
            hijoMinimo = self.encontrarHijoMinimo(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hijoMinimo]:
                self.listaMonticulo[i], self.listaMonticulo[hijoMinimo] = self.listaMonticulo[hijoMinimo], self.listaMonticulo[i]
            i = hijoMinimo

    def encontrarHijoMinimo(self, i):
        if (i * 2 + 1) > self.tamanio():
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

if __name__ == "__main__":
    monticulo = Monticulo_Min()

    monticulo.insertar(8)
    monticulo.insertar(5)
    monticulo.insertar(20)
    monticulo.insertar(7)

    print("Eliminando elementos en orden ascendente:")
    while not monticulo.estaVacio():
        minimo = monticulo.eliminarMin()
        print(minimo)

