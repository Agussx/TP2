class Monticulo_Max:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanioActual = 0

    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanioActual += 1
        self.subir(self.tamanioActual)

    def buscarMax(self):
        if self.tamanioActual > 0:
            return self.listaMonticulo[1]
        else:
            return None

    def eliminarMax(self):
        if self.estaVacio():
            return None
        else:
         maximo = self.listaMonticulo[1]
         self.listaMonticulo[1] = self.listaMonticulo[self.tamanioActual]
         self.tamanioActual -= 1
         self.listaMonticulo.pop()
         self.bajar(1)
         return maximo

    def estaVacio(self):
        if self.tamanioActual==0:
         return True 
        else:
         return False

    def tamanio(self):
        return self.tamanioActual

    def construirMonticulo(self, lista):
        self.tamanioActual = len(lista)
        self.listaMonticulo = [0] + lista[:]
        i = self.tamanioActual // 2
        while (i > 0):
            self.bajar(i)
            i = i - 1

    def subir(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i] > self.listaMonticulo[i // 2]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2

    def bajar(self, i):
        while (i * 2) <= self.tamanioActual:
            hijoMaximo = self.encontrarHijoMaximo(i)
            if self.listaMonticulo[i] < self.listaMonticulo[hijoMaximo]:
                self.listaMonticulo[i], self.listaMonticulo[hijoMaximo] = self.listaMonticulo[hijoMaximo], self.listaMonticulo[i]
            i = hijoMaximo

    def encontrarHijoMaximo(self, i):
        if (i * 2 + 1) > self.tamanioActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] > self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
