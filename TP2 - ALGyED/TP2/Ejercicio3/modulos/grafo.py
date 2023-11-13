from TP2.Ejercicio3.modulos.vertice import Vertice

class Grafo:
    """
    Clase que representa un grafo.

    """
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        """
        Agrega un vértice al grafo.

        Parámetros:
        - vertice: Objeto Vertice a agregar al grafo.
        """
        self.vertices[vertice.obtener_id()] = vertice

    def obtener_vertice(self, clave):
        """
        Obtiene un vértice del grafo por su clave (ID).

        Parámetros:
        - clave: Clave (ID) del vértice a obtener.

        Retorna:
        - Vértice correspondiente o None si no se encuentra.
        """
        return self.vertices[clave] if clave in self.vertices else None

    def agregar_arista(self, desde, hacia, peso, atributo_extra=0):
        """
        Agrega una arista al grafo entre dos vértices con un peso y un atributo extra opcional(precio).

        Parámetros:
        - desde: Clave (ID) del vértice de origen.
        - hacia: Clave (ID) del vértice de destino.
        - peso: Peso de la arista.
        - atributo_extra: Atributo extra de la arista (precio).
        """
        if desde not in self.vertices:
            self.agregar_vertice(Vertice(desde))
        if hacia not in self.vertices:
            self.agregar_vertice(Vertice(hacia))

        self.vertices[desde].agregar_vecino(self.vertices[hacia], peso, atributo_extra)



