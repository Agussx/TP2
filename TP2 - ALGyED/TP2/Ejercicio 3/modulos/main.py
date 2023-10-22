# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:41:58 2023

@author: Candelaria
"""
class TransporteCasaBella:
    def __init__(self, archivo_rutas):
        self.grafo = self._cargar_rutas(archivo_rutas)

    def _cargar_rutas(self, archivo_rutas):
        grafo = {}
        with open(archivo_rutas, "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                origen = partes[0]
                destino = partes[1]
                capacidad = int(partes[2])
                costo = int(partes[3])
                if origen not in grafo:
                    grafo[origen] = []
                grafo[origen].append((destino, capacidad, costo))
        return grafo

    def maximo_cuello_de_botella(self, inicio, fin):
        cuello_de_botella = {vertice: float('inf') for vertice in self.grafo}
        cuello_de_botella[inicio] = 0
        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            cuello_actual, vertice_actual = min(cola_prioridad, key=lambda x: x[0])
            cola_prioridad.remove((cuello_actual, vertice_actual))

            if vertice_actual == fin:
                return cuello_de_botella[fin]

            for vecino, capacidad, costo in self.grafo[vertice_actual]:
                cuello_actualizado = min(cuello_actual, capacidad)
                if cuello_actualizado < cuello_de_botella[vecino]:
                    cuello_de_botella[vecino] = cuello_actualizado
                    cola_prioridad.append((cuello_actualizado, vecino))

        return None

    def obtener_maximos_cuellos_de_botella(self, inicio="CiudadBs.As."):
        maximos_cuellos_de_botella = {}
        for ciudad in self.grafo.keys():
            if ciudad != inicio:
                maximos_cuellos_de_botella[ciudad] = self.maximo_cuello_de_botella(inicio, ciudad)
        return maximos_cuellos_de_botella

    def obtener_costos_minimos_para_transportar(self, peso, inicio="CiudadBs.As."):
        maximos_cuellos_de_botella = self.obtener_maximos_cuellos_de_botella(inicio)
        costos_minimos = {}
        for ciudad in self.grafo.keys():
            if ciudad != inicio:
                cuello_maximo = maximos_cuellos_de_botella[ciudad]
                costo = None
                if cuello_maximo >= peso:
                    for _, capacidad, costo_de_ruta in self.grafo[inicio]:
                        if capacidad >= peso:
                            if costo is None or costo > costo_de_ruta:
                                costo = costo_de_ruta
                costos_minimos[ciudad] = costo
        return costos_minimos

if __name__ == "__main__":
    transporte = TransporteCasaBella("rutas.txt")
    print("Contenido del diccionario self.graph:")
    for origen, destinos in transporte.grafo.items():
        print(f"Origen: {origen}")
        for destino, capacidad, costo in destinos:
            print(f"  -> Destino: {destino}, Capacidad: {capacidad}, Costo: {costo}")
    
    # Obtener el máximo cuello de botella entre Ciudad de Buenos Aires y otras ciudades
    maximos_cuellos = transporte.obtener_maximos_cuellos_de_botella()
    print("Máximo cuello de botella entre Ciudad de Buenos Aires y otras ciudades:")
    for ciudad, cuello in maximos_cuellos.items():
        print(f"{ciudad}: {cuello} kg")

    # Obtener los costos mínimos para transportar un mobiliario de 100 kg desde Buenos Aires a otras ciudades
    costos_minimos_100kg = transporte.obtener_costos_minimos_para_transportar(100)
    print("\nPrecio mínimo para transportar un mobiliario de 100 kg desde Ciudad de Buenos Aires a otras ciudades:")
    for ciudad, costo in costos_minimos_100kg.items():
        print(f"{ciudad}: {costo} unidades de 1000")