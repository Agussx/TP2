import heapq  # Importa el módulo heapq para implementar la cola de prioridad.

# Clase Grafo para representar un grafo ponderado de ciudades y rutas.
class Grafo:
    def __init__(self):
        # Inicializa un diccionario de vértices.
        self.vertices = {}

    def agregar_vertice(self, ciudad):
        """
        Agrega un vértice (ciudad) al grafo.

        :param ciudad: Nombre de la ciudad a agregar como vértice.
        """
        if ciudad not in self.vertices:
            self.vertices[ciudad] = {}

    def agregar_arista(self, ciudad_origen, ciudad_destino, peso, precio):
        """
        Agrega una arista entre dos ciudades con peso y precio.

        :param ciudad_origen: Nombre de la ciudad de origen.
        :param ciudad_destino: Nombre de la ciudad de destino.
        :param peso: Peso de la arista (cuello de botella).
        :param precio: Precio de la arista (costo, tarifa, etc.).
        """
        if ciudad_origen in self.vertices and ciudad_destino in self.vertices:
            self.vertices[ciudad_origen][ciudad_destino] = (peso, precio)
            self.vertices[ciudad_destino][ciudad_origen] = (peso, precio)

def dijkstra(grafo, inicio):
    """
    Realiza el algoritmo de Dijkstra para encontrar las distancias más cortas desde un vértice de inicio.

    :param grafo: Objeto de la clase Grafo que representa el grafo ponderado.
    :param inicio: Nombre de la ciudad de inicio.
    :return: Un diccionario con las distancias más cortas desde la ciudad de inicio a todas las demás ciudades.
    """
    distancia = {vertice: float('inf') for vertice in grafo.vertices}
    distancia[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        (dist, vertice_actual) = heapq.heappop(cola_prioridad)

        if dist > distancia[vertice_actual]:
            continue

        for vecino, peso in grafo.vertices[vertice_actual].items():
            nueva_distancia = distancia[vertice_actual] + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancia

if __name__ == "__main__":
    # Crear un objeto de grafo
    grafo = Grafo()

    # Leer el archivo de texto y agregar los vértices y aristas al grafo
    with open('C:/Users/agust/OneDrive/Escritorio/Ejercicio3/.spyproject/modulos/rutas.txt', 'r') as file:
        for linea in file:
            datos = linea.strip().split(',')
            ciudad_inicio, ciudad_destino, peso, precio = datos
            peso = int(peso)
            precio = int(precio)

            grafo.agregar_vertice(ciudad_inicio)
            grafo.agregar_vertice(ciudad_destino)
            grafo.agregar_arista(ciudad_inicio, ciudad_destino, peso, precio)

    #  imprimir el grafo
    for ciudad, conexiones in grafo.vertices.items():
        print(f"Ciudad: {ciudad}")
        for conexion, (peso, precio) in conexiones.items():
            print(f"  -> Conexión a {conexion}: Peso = {peso}, Precio = {precio}")