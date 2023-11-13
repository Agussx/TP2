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
        Elimina y devuelve la distancia mínima y el vértice asociado del montículo mínimo.

        :return: Una tupla con la distancia mínima y el vértice asociado,
                 o None si el montículo está vacío.
        """
        if len(self.listaMonticulo) > 1:
            minimo = self.listaMonticulo[1]  # El mínimo está en la posición 1
            ultimo = self.listaMonticulo.pop()  # Elimina el último elemento de la lista
            if len(self.listaMonticulo) > 1:
                self.listaMonticulo[1] = ultimo  # Mueve el último elemento a la cima del montículo
                self.bajar(1)  # Llama a la función bajar para restaurar la propiedad del montículo
            return minimo[0], minimo[1]  # Ahora devuelve la distancia y el vértice asociado
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
     while i // 2 > 0:
        if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
            self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
        i = i // 2

    def bajar(self, i):
     while (i * 2) <= self.tamanio():
        hijoMinimo = self.encontrarHijoMinimo(i)
        if self.listaMonticulo[i][0] > self.listaMonticulo[hijoMinimo][0]:
            self.listaMonticulo[i], self.listaMonticulo[hijoMinimo] = self.listaMonticulo[hijoMinimo], self.listaMonticulo[i]
        i = hijoMinimo

    def encontrarHijoMinimo(self, i):
     if (i * 2 + 1) > self.tamanio():
        return i * 2
     else:
        hijo_izquierdo = i * 2
        hijo_derecho = i * 2 + 1

        # Comparar las distancias en lugar de los vértices directamente
        if self.listaMonticulo[hijo_izquierdo][0] < self.listaMonticulo[hijo_derecho][0]:
            return hijo_izquierdo
        else:
            return hijo_derecho
            
    def decrementarClave(self, vertice, nueva_distancia):
        for i in range(1, len(self.listaMonticulo)):
            if self.listaMonticulo[i][1] == vertice:
                if nueva_distancia < self.listaMonticulo[i][0]:
                    self.listaMonticulo[i] = (nueva_distancia, vertice)
                    self.subir(i)
                break