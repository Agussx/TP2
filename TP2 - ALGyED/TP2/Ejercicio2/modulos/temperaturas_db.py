# Importar el módulo datetime para trabajar con fechas y horas
from datetime import datetime

# Importar las clases AVL y NodoAVL del módulo avl y nodo
from avl import AVL
from nodo import NodoAVL

# Clase Temperaturas_DB para gestionar datos de temperaturas
class Temperaturas_DB:
    def __init__(self):
        # Crear una instancia de la clase AVL para gestionar las temperaturas
        self.avl = AVL()

    def guardar_temperatura(self, temperatura, fecha):
        """
        Guarda una medición de temperatura en la base de datos.

        :param temperatura: La temperatura a almacenar.
        :param fecha: La fecha de la medición en formato "dd/mm/yyyy".
        """
        fecha_datetime = datetime.strptime(fecha, "%d/%m/%Y")
        self.avl.insertar(fecha_datetime, (temperatura, fecha))

    def devolver_temperatura(self, fecha):
        """
        Devuelve la temperatura registrada en una fecha específica.

        :param fecha: La fecha de la medición en formato "dd/mm/yyyy".
        :return: La temperatura almacenada en la fecha dada o None si no se encuentra.
        """
        fecha_datetime = datetime.strptime(fecha, "%d/%m/%Y")
        nodo = self.avl.buscar(fecha_datetime)
        if nodo:
            return nodo.valor[0]  # Devuelve la temperatura almacenada
        else:
            return None

    def max_temp_rango(self, fecha1, fecha2):
        """
        Devuelve la temperatura máxima registrada en un rango de fechas.

        :param fecha1: La fecha de inicio del rango en formato "dd/mm/yyyy".
        :param fecha2: La fecha de fin del rango en formato "dd/mm/yyyy".
        :return: La temperatura máxima en el rango de fechas o None si no se encuentra.
        """
        fecha1_datetime = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_datetime = datetime.strptime(fecha2, "%d/%m/%Y")
        max_temp = self._max_temp_rango(fecha1_datetime, fecha2_datetime, self.avl.raiz)
        return max_temp if max_temp is not None else None

    def _max_temp_rango(self, fecha1, fecha2, nodo):
        """
        Método privado para encontrar la temperatura máxima en un rango de fechas.

        :param fecha1: La fecha de inicio del rango en formato "dd/mm/yyyy".
        :param fecha2: La fecha de fin del rango en formato "dd/mm/yyyy".
        :param nodo: Nodo actual en el árbol AVL.
        :return: La temperatura máxima en el rango de fechas o None si no se encuentra.
        """
        if nodo is None:
            return None

        if fecha1 <= nodo.clave <= fecha2:
            izq_max = self._max_temp_rango(fecha1, fecha2, nodo.izquierdo)
            der_max = self._max_temp_rango(fecha1, fecha2, nodo.derecho)
            max_temp = nodo.valor[0]

            if izq_max is not None:
                max_temp = max(max_temp, izq_max)
            if der_max is not None:
                max_temp = max(max_temp, der_max)

            return max_temp
        elif fecha2 < nodo.clave:
            return self._max_temp_rango(fecha1, fecha2, nodo.izquierdo)
        else:
            return self._max_temp_rango(fecha1, fecha2, nodo.derecho)

    def min_temp_rango(self, fecha1, fecha2):
        """
        Devuelve la temperatura mínima registrada en un rango de fechas.

        :param fecha1: La fecha de inicio del rango en formato "dd/mm/yyyy".
        :param fecha2: La fecha de fin del rango en formato "dd/mm/yyyy".
        :return: La temperatura mínima en el rango de fechas o None si no se encuentra.
        """
        fecha1_datetime = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_datetime = datetime.strptime(fecha2, "%d/%m/%Y")
        min_temp = self._min_temp_rango(fecha1_datetime, fecha2_datetime, self.avl.raiz)
        return min_temp if min_temp is not None else None

    def _min_temp_rango(self, fecha1, fecha2, nodo):
        """
        Método privado para encontrar la temperatura mínima en un rango de fechas.

        :param fecha1: La fecha de inicio del rango en formato "dd/mm/yyyy".
        :param fecha2: La fecha de fin del rango en formato "dd/mm/yyyy".
        :param nodo: Nodo actual en el árbol AVL.
        :return: La temperatura mínima en el rango de fechas o None si no se encuentra.
        """
        if nodo is None:
            return None

        if fecha1 <= nodo.clave <= fecha2:
            izq_min = self._min_temp_rango(fecha1, fecha2, nodo.izquierdo)
            der_min = self._min_temp_rango(fecha1, fecha2, nodo.derecho)
            min_temp = nodo.valor[0]

            if izq_min is not None:
                min_temp = min(min_temp, izq_min)
            if der_min is not None:
                min_temp = min(min_temp, der_min)

            return min_temp
        elif fecha2 < nodo.clave:
            return self._min_temp_rango(fecha1, fecha2, nodo.izquierdo)
        else:
            return self._min_temp_rango(fecha1, fecha2, nodo.derecho)

    def _temp_extremos_rango(self, fecha1, fecha2, nodo=None):
        """
        Devuelve las temperaturas mínima y máxima registradas en un rango de fechas.

        :param fecha1: La fecha de inicio del rango en formato "dd/mm/yyyy".
        :param fecha2: La fecha de fin del rango en formato "dd/mm/yyyy".
        :param nodo: Nodo actual en el árbol AVL.
        :return: Una tupla con la temperatura mínima y máxima en el rango de fechas.
        """
        return (self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1, fecha2))

    def borrar_temperatura(self, fecha):
        """
        Elimina una medición de temperatura en una fecha específica.

        :param fecha: La fecha de la medición en formato "dd/mm/yyyy".
        """
        fecha_datetime = datetime.strptime(fecha, "%d/%m/%Y")
        self.avl.eliminar(fecha_datetime)

    def devolver_temperaturas(self, fecha1, fecha2):
        """
        Devuelve todas las temperaturas registradas en un rango de fechas.

        :param fecha1: La fecha de inicio del rango en formato "dd/mm/yyyy".
        :param fecha2: La fecha de fin del rango en formato "dd/mm/yyyy".
        :return: Una lista de cadenas con las temperaturas y sus fechas en el rango de fechas.
        """
        fecha1_datetime = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_datetime = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = self._devolver_temperaturas(fecha1_datetime, fecha2_datetime, self.avl.raiz)
        return temperaturas

    def _devolver_temperaturas(self, fecha1, fecha2, nodo):
        """
        Método privado para obtener las temperaturas en un rango de fechas.

        :param fecha1: La fecha de inicio del rango en formato "dd/mm/yyyy".
        :param fecha2: La fecha de fin del rango en formato "dd/mm/yyyy".
        :param nodo: Nodo actual en el árbol AVL.
        :return: Una lista de cadenas con las temperaturas y sus fechas en el rango de fechas.
        """
        temperaturas = []
        if nodo is None:
            return temperaturas

        if fecha1 <= nodo.clave <= fecha2:
            temperaturas += self._devolver_temperaturas(fecha1, fecha2, nodo.izquierdo)
            temperaturas.append(f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.valor[0]} ºC")
            temperaturas += self._devolver_temperaturas(fecha1, fecha2, nodo.derecho)
        elif fecha2 < nodo.clave:
            return self._devolver_temperaturas(fecha1, fecha2, nodo.izquierdo)
        else:
            return self._devolver_temperaturas(fecha1, fecha2, nodo.derecho)

        return temperaturas

    def cantidad_muestras(self):
        """
        Devuelve la cantidad de muestras de temperatura almacenadas en la base de datos.

        :return: La cantidad de muestras.
        """
        return self.avl.tamanio

# Crear una instancia de Temperaturas_DB
temperaturas_db = Temperaturas_DB()

# Agregar mediciones de temperatura
temperaturas_db.guardar_temperatura(25.5, "15/01/2023")
temperaturas_db.guardar_temperatura(28.0, "16/01/2023")
temperaturas_db.guardar_temperatura(22.7, "17/01/2023")
temperaturas_db.guardar_temperatura(20.3, "18/01/2023")
temperaturas_db.guardar_temperatura(30.1, "19/01/2023")

# Consultar la temperatura en una fecha específica
temperatura_16_enero = temperaturas_db.devolver_temperatura("16/01/2023")
print(f"Temperatura el 16 de enero: {temperatura_16_enero} ºC")

# Consultar la temperatura máxima en un rango de fechas
max_temp_rango = temperaturas_db.max_temp_rango("16/01/2023", "18/01/2023")
print(f"Temperatura máxima en el rango: {max_temp_rango} ºC")

# Consultar la temperatura mínima en un rango de fechas
min_temp_rango = temperaturas_db.min_temp_rango("15/01/2023", "19/01/2023")
print(f"Temperatura mínima en el rango: {min_temp_rango} ºC")

# Consultar las temperaturas mínima y máxima en un rango de fechas
min_temp, max_temp = temperaturas_db._temp_extremos_rango("17/01/2023", "19/01/2023")
print(f"Temperatura mínima en el rango: {min_temp} ºC")
print(f"Temperatura máxima en el rango: {max_temp} ºC")

# Borrar una medición de temperatura
temperaturas_db.borrar_temperatura("18/01/2023")

# Consultar todas las temperaturas en un rango de fechas
temperaturas_rango = temperaturas_db.devolver_temperaturas("15/01/2023", "19/01/2023")
for temperatura in temperaturas_rango:
    print(temperatura)

# Consultar la cantidad de muestras en la base de datos
cantidad_muestras = temperaturas_db.cantidad_muestras()
print(f"Cantidad de muestras en la base de datos: {cantidad_muestras}")

