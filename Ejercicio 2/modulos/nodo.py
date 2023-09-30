class Nodo:
 def __init__(self,clave,valor): 
  self.clave=clave #en el contexto, es la fecha
  self.valor=valor #en el contexto, es la temperatura 
  self.hijoIzquierdo=None 
  self.hijoDerecho=None
  self.padre=None
  self.altura=0 #preguntar
  self.fe=0 #factor de equilibrio, vale cero cuando es creado el nodo. 
  #Atributos que pensamos que van: el nivel del nodo, el factor de equilibrio
  
 def tieneHijoIzquierdo(self):
   if self.hijoIzquierdo!=None:
     return True
   else:
    return False
   
 def tieneHijoDerecho(self): 
   if self.hijoDerecho!=None: 
    return True 
   else:
    return False
  
if __name__=="__main__" :
  
  nd=Nodo("1","2")
  print (nd.tieneHijoIzquierdo)