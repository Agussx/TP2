# Definición de la clase NodoAVL
class NodoAVL:
    def __init__(self, clave, valor, padre=None):
        """
        Constructor de la clase NodoAVL.

        :param clave: La clave que identifica al nodo.
        :param valor: El valor asociado al nodo.
        :param padre: El nodo padre (opcional) del nodo actual.
        """
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.padre = padre
        self.altura = 1
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        """
        Comprueba si el nodo tiene un hijo izquierdo.

        :return: True si tiene un hijo izquierdo, False en caso contrario.
        """
        return self.izquierdo is not None

    def tieneHijoDerecho(self):
        """
        Comprueba si el nodo tiene un hijo derecho.

        :return: True si tiene un hijo derecho, False en caso contrario.
        """
        return self.derecho is not None

    def esHijoIzquierdo(self):
        """
        Comprueba si el nodo es el hijo izquierdo de su padre.

        :return: True si es hijo izquierdo, False en caso contrario.
        """
        return self.padre and self.padre.izquierdo == self

    def esHijoDerecho(self):
        """
        Comprueba si el nodo es el hijo derecho de su padre.

        :return: True si es hijo derecho, False en caso contrario.
        """
        return self.padre and self.padre.derecho == self

    def esRaiz(self):
        """
        Comprueba si el nodo es la raíz del árbol.

        :return: True si es la raíz, False en caso contrario.
        """
        return not self.padre


