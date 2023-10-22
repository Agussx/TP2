# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:04:59 2023

@author: Candelaria
"""
import time
import datetime
from paciente import Paciente
import random

# Importamos la implementación de Montículo Mínimo que proporcioné anteriormente
from monticulomin import Monticulo_Min
n = 20  # cantidad de ciclos de simulación

cola_de_espera = Monticulo_Min()  # Usamos una cola de prioridad

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    paciente = Paciente()
    cola_de_espera.insertar((paciente.get_riesgo(), paciente))

    if random.random() < 0.5:
        if not cola_de_espera.estaVacio():
            criticidad, paciente_atendido = cola_de_espera.eliminarMin()
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
    
    print()

    print('Pacientes que faltan atenderse:', cola_de_espera.tamanio())
    
    for _, paciente in cola_de_espera.listaMonticulo[1:]:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)














