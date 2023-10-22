# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:02:46 2023

@author: Candelaria
"""

# -*- coding: utf-8 -*-

from random import randint, choices
import datetime
import time

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.hora_llegada = datetime.datetime.now()  # Hora de llegada como atributo público

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
   
    def __lt__(self, otro):
    # Comparar por nivel de riesgo como primer criterio
     if self.get_riesgo() < otro.get_riesgo():
        return True
     elif self.get_riesgo() > otro.get_riesgo():
        return False
     else:
        # Si tienen el mismo nivel de riesgo, usar la hora de llegada como segundo criterio
        return self.hora_llegada < otro.hora_llegada


if __name__=="__main__":
    # Crear pacientes de prueba
    paciente1 = Paciente() 
    paciente2 = Paciente() 
  

    # Imprimir información sobre los pacientes
    print("Información de los pacientes:")
    print(paciente1)
    print(paciente1.hora_llegada)

    print()
    print('-*-'*15)
    
    time.sleep(1)

    print(paciente2)
    print(paciente2.hora_llegada)
    
    print("!Atencion!")
    print()
    # Comparar pacientes por nivel de riesgo y hora de llegada
    if paciente1 < paciente2:
        print(f"{paciente1} tiene un nivel de riesgo mayor que {paciente2}")
    if paciente2 <  paciente1:    
        print(f"{paciente2} tiene un nivel de riesgo mayor que {paciente1}")
    if paciente2==paciente1:
        print(f"{paciente1} tiene un nivel de riesgo igual que {paciente2}")



    
    