from nodo import Nodo
#preguntar herencia ABB
class AVL:

    def __init__(self):
        self.raiz = None
        self.tamanio = 0

    def longitud(self):
        return self.tamanio

    def __len__(self):
        return self.tamanio

    def __iter__(self):
        return self.raiz.__iter__()
     
    def _agregar(self,clave,valor,nodoActual): 
     NodoArbol=Nodo()
     if clave < nodoActual.clave:
        if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,valor,nodoActual.hijoIzquierdo)
        else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
     else:
        if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
        else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)
     
     self.tamanio+=1
        
     def actualizarEquilibrio(self,nodo): 
      if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
        self.reequilibrar(nodo)
        return
      if nodo.padre != None:
        if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
        elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1

        if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)

      def rotarIzquierda(self,rotRaiz):
       nuevaRaiz = rotRaiz.hijoDerecho
       rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
       if nuevaRaiz.hijoIzquierdo != None:
          nuevaRaiz.hijoIzquierdo.padre = rotRaiz
          nuevaRaiz.padre = rotRaiz.padre
       if rotRaiz.esRaiz():
          self.raiz = nuevaRaiz
       else:
        if rotRaiz.esHijoIzquierdo():
           rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        else:
            rotRaiz.padre.hijoDerecho = nuevaRaiz
            nuevaRaiz.hijoIzquierdo = rotRaiz
            rotRaiz.padre = nuevaRaiz
            rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
            nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

        def _altura(self, nodo):
         if not nodo:
            return 0
        return nodo.altura



       #falta rotarDerecha
        def rotarDerecha(self,rotRaiz): 
            pass 

'''Para mantener el equilibrio del árbol AVL 
después de eliminar un nodo, debes implementar las rotaciones AVL adecuadas
(rotación simple y doble). Estas rotaciones se utilizan para garantizar que la diferencia 
de alturas entre los subárboles izquierdo y derecho sea como máximo 1 en cada nodo.'''

     def eliminar(self,clave):
      pass 
     def buscar(self,clave): 
      pass