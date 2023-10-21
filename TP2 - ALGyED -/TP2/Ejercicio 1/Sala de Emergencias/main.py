# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
from modulos.paciente import Paciente
from modulos.monticulo import Monticulo_Max
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = Monticulo_Max()  # Crear una instancia de la clase Monticulo_Max

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = Paciente()
    # Se inserta el paciente en la cola de espera usando el montículo máximo
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende al paciente de mayor riesgo en la cola
        if not cola_de_espera.estaVacio():
            paciente_atendido = cola_de_espera.eliminarMin()
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestra el número de pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_de_espera.tamanio())
    for i in range(1, cola_de_espera.tamanio() + 1):
        print('\t', cola_de_espera.listaMonticulo[i])
    
    print()
    print('-*-'*15)
    
    time.sleep(1)











