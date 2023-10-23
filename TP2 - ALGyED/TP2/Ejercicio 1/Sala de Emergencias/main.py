# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:04:59 2023
@author: Candelaria
"""
import time
import datetime
from modulos.paciente import Paciente  # Importa la clase Paciente desde el módulo correspondiente
import random

# Importamos la implementación de Montículo Mínimo que proporcioné anteriormente
from modulos.monticulo import Monticulo_Min
n = 20  # Cantidad de ciclos de simulación

cola_de_espera = Monticulo_Min()  # Crea una cola de prioridad utilizando el Montículo Mínimo

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    paciente = Paciente()  # Crea un objeto de la clase Paciente para simular la llegada de pacientes
    cola_de_espera.insertar((paciente.get_riesgo(), paciente))  # Inserta un paciente en la cola de espera con su riesgo como clave

    if random.random() < 0.5:  # Simula la atención de pacientes con una probabilidad del 50%
        if not cola_de_espera.estaVacio():  # Comprueba si la cola de espera no está vacía
            criticidad, paciente_atendido = cola_de_espera.eliminarMin()  # Elimina y obtiene el paciente de mayor criticidad
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
    
    print()

    print('Pacientes que faltan atenderse:', cola_de_espera.tamanio())  # Muestra la cantidad de pacientes en espera
    
    for _, paciente in cola_de_espera.listaMonticulo[1:]:
        print('\t', paciente)  # Muestra información de los pacientes en espera
    
    print()
    print('-*-'*15)
    
    time.sleep(1)  # Espera 1 segundo antes de continuar con el siguiente ciclo















