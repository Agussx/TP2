import time
import datetime
from modulos.paciente import Paciente
from modulos.monticulo import Monticulo_Max
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = Monticulo_Max()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = Paciente()
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5 and not cola_de_espera.estaVacio():
        # se atiende al paciente más crítico que se encuentra en la cima del montículo
        paciente_atendido = cola_de_espera.eliminarMax()
        print('*' * 40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*' * 40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass

    print()

    # Se muestran los pacientes restantes en la cola de espera (montículo)
    print('Pacientes que faltan atenderse:', cola_de_espera.tamanio())
    for paciente in cola_de_espera.listaMonticulo[1:]:
        print('\t', paciente)

    print()
    print('-*-' * 15)

    time.sleep(1)









