class Monticulo_Max:
    """
    Clase que representa un montículo máximo (max heap).
    Atributos:
    - listaMonticulo: Lista que almacena los elementos del montículo.
    """
    def __init__(self):
        self.listaMonticulo = [0] #tamanio?

    def insertar(self, k):
        """
        Inserta un nuevo elemento en el montículo.

        Parámetros:
        - k: Elemento a insertar en el montículo.
        """
        self.listaMonticulo.append(k)
        self.subir(len(self.listaMonticulo) - 1)

    def eliminarMax(self):
        """
        Elimina y devuelve el elemento máximo del montículo.

        Retorna:
        - Tupla que contiene el elemento máximo y su segundo elemento (si es que existe).
        - None si el montículo está vacío.
        """
        if len(self.listaMonticulo) > 1:
            maximo = self.listaMonticulo[1]
            ultimo = self.listaMonticulo.pop()
            if len(self.listaMonticulo) > 1:
                self.listaMonticulo[1] = ultimo
                self.bajar(1)
            return maximo[0], maximo[1]
        return None

    def estaVacio(self):
        """
        Verifica si el montículo está vacío.

        Retorna:
        - True si el montículo está vacío, False en caso contrario.
        """
        return len(self.listaMonticulo) == 1

    def tamanio(self):
        """
        Retorna el tamaño del montículo.

        Retorna:
        - Tamaño del montículo.
        """
        return len(self.listaMonticulo) - 1

    def subir(self, i):
        """
        Realiza la operación "subir" para mantener la propiedad del montículo después de una inserción.

        Parámetros:
        - i: Índice del elemento que se ha insertado.
        """
        while i // 2 > 0:
            if self.listaMonticulo[i][0] > self.listaMonticulo[i // 2][0]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2

    def bajar(self, i):
        """
        Realiza la operación "bajar" para mantener la propiedad del montículo después de una eliminación.

        Parámetros:
        - i: Índice del elemento que se ha eliminado.
        """

        while (i * 2) <= self.tamanio():
            hijoMaximo = self.encontrarHijoMaximo(i)
            if self.listaMonticulo[i][0] < self.listaMonticulo[hijoMaximo][0]:
                self.listaMonticulo[i], self.listaMonticulo[hijoMaximo] = self.listaMonticulo[hijoMaximo], self.listaMonticulo[i]
            i = hijoMaximo

    def encontrarHijoMaximo(self, i):
        """
        Encuentra el índice del hijo máximo en un nodo dado.

        Parámetros:
        - i: Índice del nodo padre.

        Retorna:
        - Índice del hijo máximo.
        """
        if (i * 2 + 1) > self.tamanio():
            return i * 2
        else:
            hijo_izquierdo = i * 2
            hijo_derecho = i * 2 + 1

            if self.listaMonticulo[hijo_izquierdo][0] > self.listaMonticulo[hijo_derecho][0]:
                return hijo_izquierdo
            else:
                return hijo_derecho
