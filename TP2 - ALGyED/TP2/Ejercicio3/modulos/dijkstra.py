from grafo import Grafo
from vertice import Vertice
from monticulo_max import Monticulo_Max
from monticulo_min import Monticulo_Min

def dijkstra_max_cuello(grafo, inicio):
    monticulo = Monticulo_Max()
    inicio_vertice = grafo.obtener_vertice(inicio)
    inicio_vertice.asignar_peso(float('inf'))  # Inicializar el peso como infinito
    monticulo.insertar((float('inf'), inicio_vertice))  # Ahora insertamos la tupla (cuello de botella, vértice)

    while not monticulo.estaVacio():
        cuello_actual, actual = monticulo.eliminarMax()  # Ahora extraemos la tupla

        for vecino in actual.obtener_conexiones():
            cuello_minimo = min(cuello_actual, actual.obtener_ponderacion(vecino))
            if cuello_minimo > vecino.obtener_peso():
                vecino.asignar_peso(cuello_minimo)
                vecino.asignar_predecesor(actual)
                monticulo.insertar((cuello_minimo, vecino))  # Ahora insertamos la tupla

def dijkstra(grafo, inicio): #Dijkstra para el 2do punto
    monticulo = Monticulo_Min()
    inicio_vertice = grafo.obtener_vertice(inicio)
    inicio_vertice.asignar_precio(0)
    monticulo.insertar((0, inicio_vertice))  # Ahora insertamos la tupla (precio, vértice)

    while not monticulo.estaVacio():
        precio_actual, actual = monticulo.eliminarMin()  # Ahora extraemos la tupla

        for vecino in actual.obtener_conexiones():
            nuevo_precio = precio_actual + actual.obtener_atributo_extra(vecino)
            if nuevo_precio < vecino.obtener_precio():
                vecino.asignar_precio(nuevo_precio)
                vecino.asignar_predecesor(actual)
                monticulo.insertar((nuevo_precio, vecino))  # Ahora insertamos la tupla

def imprimir_rutas_precio(grafo, ciudad_inicial):
    for clave in grafo.vertices:
        destino = grafo.obtener_vertice(clave)

        # Imprimir resultados
        print(f"Desde {ciudad_inicial} a {destino.obtener_id()}:")
        print(f"Monto Minimo: {destino.obtener_precio()}")
        print("Camino:")
        actual = destino
        while actual:
            print(actual.obtener_id(), end=' ')
            actual = actual.predecesor
        print("\n")


def imprimir_rutas_peso(grafo, ciudad_inicial):
    for clave in grafo.vertices:
        destino = grafo.obtener_vertice(clave)

        # Imprimir resultados
        print(f"Desde {ciudad_inicial} a {destino.obtener_id()}:")
        print(f"Peso admitido: {destino.obtener_peso()}")
        print("Camino:")
        actual = destino
        while actual:
            print(actual.obtener_id(), end=' ')
            actual = actual.predecesor
        print("\n")

    
if __name__ == "__main__":
    grafo = Grafo()
    ciudad_inicial = 'CiudadBs.As.'
  
    # Lectura del archivo y construcción del grafo
    
    with open('C:/Users/agust/OneDrive/Escritorio/TP2 - ALGyED/TP2/Ejercicio3/modulos/rutas.txt', 'r') as archivo:
        for linea in archivo:
            inicio, fin, peso, precio = linea.strip().split(',')
            peso, precio = int(peso), int(precio)

            if inicio not in grafo.vertices:
                grafo.agregar_vertice(Vertice(inicio))
            if fin not in grafo.vertices:
                grafo.agregar_vertice(Vertice(fin))

            grafo.agregar_arista(inicio, fin, peso, precio)
   
    # Aplicación del algoritmo de Dijkstra modificado desde Buenos Aires
    dijkstra_max_cuello(grafo,ciudad_inicial)
    imprimir_rutas_peso(grafo,ciudad_inicial)
    dijkstra(grafo, ciudad_inicial)
    imprimir_rutas_precio(grafo,ciudad_inicial)
    
''' Codigo para mostrar el grafo
print("Grafo después de aplicar los algoritmos:")
    for vertice in grafo.vertices.values():
        print(f"Vertice {vertice.obtener_id()}:")
        for conexion in vertice.obtener_conexiones():
            ponderacion = vertice.obtener_ponderacion(conexion)
            atributo_extra = vertice.atributo_extra(conexion)
            print(f"   Conexión a {conexion.obtener_id()} con Ponderación {ponderacion} y Atributo Extra {atributo_extra}")'''


    

    


