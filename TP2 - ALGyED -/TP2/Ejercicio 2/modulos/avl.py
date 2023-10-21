from nodo import NodoAVL

class AVL:
    
 def __init__(self):
         self.raiz = None
         self.tamanio = 0

 def longitud(self):
        return self.tamanio

 def _len_(self):
        return self.tamanio

 def _iter_(self):
        return self.inorder()

 def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.izquierdo)
                self.tamanio += 1
            else:
                nodoNuevo = NodoAVL(clave, valor, padre=nodoActual)
                nodoActual.izquierdo = nodoNuevo
                self.actualizarEquilibrio(nodoNuevo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.derecho)
                self.tamanio += 1
            else:
                nodoNuevo = NodoAVL(clave, valor, padre=nodoActual)
                nodoActual.derecho = nodoNuevo
                self.actualizarEquilibrio(nodoNuevo)

        

 def eliminar(self, clave):
    if self.raiz is not None:
        self.raiz = self._eliminar(clave, self.raiz)
        self.tamanio = self.tamanio-1

 def _eliminar(self, clave, nodo):
    if nodo is None:
        return nodo

    if clave < nodo.clave:
        nodo.izquierdo = self._eliminar(clave, nodo.izquierdo)
    elif clave > nodo.clave:
        nodo.derecho = self._eliminar(clave, nodo.derecho)
    else:
        if nodo.izquierdo is None:
            temp = nodo.derecho
            nodo = None
            return temp
        elif nodo.derecho is None:
            temp = nodo.izquierdo
            nodo = None
            return temp
        temp = self._min_nodo(nodo.derecho)
        nodo.clave = temp.clave
        nodo.valor = temp.valor
        nodo.derecho = self._eliminar(temp.clave, nodo.derecho)

    if nodo is None:
        return nodo

    nodo.altura = 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))
    factor_equilibrio = self.factorEquilibrio(nodo)

    # Caso de desequilibrio hacia la izquierda
    if factor_equilibrio > 1:
        if self.factorEquilibrio(nodo.izquierdo) >= 0:
            return self.rotarDerecha(nodo)
        else:
            nodo.izquierdo = self.rotarIzquierda(nodo.izquierdo)
            return self.rotarDerecha(nodo)

    # Caso de desequilibrio hacia la derecha
    if factor_equilibrio < -1:
        if self.factorEquilibrio(nodo.derecho) <= 0:
            return self.rotarIzquierda(nodo)
        else:
            nodo.derecho = self.rotarDerecha(nodo.derecho)
            return self.rotarIzquierda(nodo)

    return nodo

 def _min_nodo(self, nodo):
    actual = nodo
    while actual.izquierdo is not None:
        actual = actual.izquierdo
    return actual

 def actualizarEquilibrio(self, nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)

 def rotarIzquierda(self, nodo):
    nueva_raiz = nodo.derecho
    nodo.derecho = nueva_raiz.izquierdo

    if nueva_raiz.izquierdo:
        nueva_raiz.izquierdo.padre = nodo

    nueva_raiz.padre = nodo.padre

    if not nodo.padre:
        self.raiz = nueva_raiz
    elif nodo.esHijoIzquierdo():
        nodo.padre.izquierdo = nueva_raiz
    else:
        nodo.padre.derecho = nueva_raiz

    nueva_raiz.izquierdo = nodo
    nodo.padre = nueva_raiz

    # Actualizar alturas y factores de equilibrio
    self.actualizarAltura(nodo)
    self.actualizarAltura(nueva_raiz)

    if nodo.factorEquilibrio < -1 or nodo.factorEquilibrio > 1:
        self.reequilibrar(nodo)

 def rotarDerecha(self, nodo):
    nueva_raiz = nodo.izquierdo
    nodo.izquierdo = nueva_raiz.derecho

    if nueva_raiz.derecho:
        nueva_raiz.derecho.padre = nodo

    nueva_raiz.padre = nodo.padre

    if not nodo.padre:
        self.raiz = nueva_raiz
    elif nodo.esHijoIzquierdo():
        nodo.padre.izquierdo = nueva_raiz
    else:
        nodo.padre.derecho = nueva_raiz

    nueva_raiz.derecho = nodo
    nodo.padre = nueva_raiz

    # Actualizar alturas y factores de equilibrio
    self.actualizarAltura(nodo)
    self.actualizarAltura(nueva_raiz)

    if nodo.factorEquilibrio < -1 or nodo.factorEquilibrio > 1:
        self.reequilibrar(nodo)

 def reequilibrar(self, nodo):
        while nodo is not None:
            self.actualizarAltura(nodo)
            factor_equilibrio = self.factorEquilibrio(nodo)

            # Caso de desequilibrio hacia la izquierda
            if factor_equilibrio > 1:
                if self.factorEquilibrio(nodo.izquierdo) < 0:
                    self.rotarIzquierda(nodo.izquierdo)
                self.rotarDerecha(nodo)

            # Caso de desequilibrio hacia la derecha
            if factor_equilibrio < -1:
                if self.factorEquilibrio(nodo.derecho) > 0:
                    self.rotarDerecha(nodo.derecho)
                self.rotarIzquierda(nodo)

            nodo = nodo.padre

 def factorEquilibrio(self, nodo):
        if nodo is None:
            return 0
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)
    
 def insertar(self, clave, valor):
        if not self.raiz:
            self.raiz = NodoAVL(clave, valor)
        else:
            self._agregar(clave, valor, self.raiz)

 def actualizarAltura(self, nodo):
        if nodo is not None:
            nodo.altura = 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))

 def altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

 def buscar(self, clave):
        return self._buscar(clave, self.raiz)

 def _buscar(self, clave, nodo):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo
        if clave < nodo.clave:
            return self._buscar(clave, nodo.izquierdo)
        else:
            return self._buscar(clave, nodo.derecho)
    
 def inorder(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo:
            yield from self.inorder(nodo.izquierdo)
            yield nodo
            yield from self.inorder(nodo.derecho)

'''
avl = AVL()

# Insertar valores en el árbol
avl.insertar(10, "A")
avl.insertar(20, "B")
avl.insertar(5, "C")
avl.insertar(15, "D")
avl.insertar(25, "E")

# Realizar un recorrido in-order (en orden) del árbol
def inorden(nodo):
    if nodo:
        inorden(nodo.izquierdo)
        print(f'Clave: {nodo.clave}, Valor: {nodo.valor}')
        inorden(nodo.derecho)

print("Recorrido In-order del árbol:")
inorden(avl.raiz)
'''


