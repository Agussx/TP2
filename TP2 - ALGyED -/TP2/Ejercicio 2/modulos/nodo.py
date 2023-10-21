class NodoAVL:
    def __init__(self, clave, valor, padre=None):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.padre = padre
        self.altura = 1
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.izquierdo is not None

    def tieneHijoDerecho(self):
        return self.derecho is not None

    def esHijoIzquierdo(self):
        return self.padre and self.padre.izquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.derecho == self

    def esRaiz(self):
        return not self.padre

