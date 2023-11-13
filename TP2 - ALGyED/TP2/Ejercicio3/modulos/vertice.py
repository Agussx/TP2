class Vertice:
    """
    Clase que representa un vértice en un grafo.

    Atributos:
    - id: Identificador único del vértice.
    - conectado_a: Diccionario que almacena los vértices vecinos y sus atributos.
    - predecesor: Vértice predecesor en un recorrido (inicializado como None).
    - peso
    - precio

    """
    def __init__(self, clave):
        self.id = clave
        self.conectado_a = {}
        self.precio = float('inf')  # Inicializar el precio como infinito
        self.predecesor = None
        self.peso = float('-inf')   # Inicializar el preso como menos infinito
        
    
    def agregar_vecino(self, vecino, ponderacion=0, atributo_extra=0):
        """
        Agrega un vecino al vértice con una ponderación y un atributo extra.

        Parámetros:
        - vecino: Objeto Vertice que representa el vértice vecino.
        - ponderacion: Ponderación de la arista entre el vértice y su vecino (por defecto, 0).
        - atributo_extra: Atributo extra asociado a la arista (por defecto, 0).
        """
        self.conectado_a[vecino] = {'ponderacion': ponderacion, 'atributo_extra': atributo_extra} #atributo_extra es el precio

    def __str__(self):
        """
        Retorna una representación en cadena del vértice y sus conexiones.

        """
        return str(self.id) + ' conectado a: ' + str([x.id for x in self.conectado_a])

    def obtener_conexiones(self):
        """
        Retorna los vértices vecinos del vértice.
        """
        return self.conectado_a.keys()

    def obtener_id(self):
        """
        Retorna la clave (ID) del vértice.

        """
        return self.id
    
    def __iter__(self):
        """
        Permite la iteración sobre los vértices vecinos.
        """
        return iter(self.conectado_a.keys())

    def obtener_ponderacion(self, vecino):
        """
        Retorna la ponderación de la arista hacia el vecino.

        Parámetros:
        - vecino: Vértice vecino.

        """
        return self.conectado_a[vecino]['ponderacion']
    
    def obtener_atributo_extra(self, vecino):
        """
        Retorna el atributo extra asociado a la arista hacia el vecino.

        Parámetros:
        - vecino: Vértice vecino.

        """
        return self.conectado_a[vecino]['atributo_extra']

    def obtener_precio(self):
        """
        Retorna el precio asociado al vértice.

        """
        return self.precio
   
    def obtener_peso(self):
        """
        Retorna el peso asociado al vértice.

        """
        return self.peso
    
    def asignar_precio(self, nuevo_precio):
        """
        Asigna un nuevo precio al vértice.

        Parámetros:
        - nuevo_precio: Nuevo precio a asignar.
        """
        self.precio = nuevo_precio
    
    def asignar_peso(self, nuevo_peso):
        """
        Asigna un nuevo peso al vértice.

        Parámetros:
        - nuevo_peso: Nuevo peso a asignar.
        """
        self.peso = nuevo_peso

    def asignar_predecesor(self, predecesor):
        """
        Asigna un vértice predecesor al vértice en un recorrido.

        Parámetros:
        - predecesor: Vértice predecesor.
        """
        self.predecesor = predecesor
