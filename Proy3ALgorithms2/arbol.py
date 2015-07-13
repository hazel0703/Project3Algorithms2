#!/usr/bin/python3
#**************************************************************************#
# Autoras: Adriana Devera 09-11286
#          Natascha Gamboa 12-11250
#
# Descripción: Maneja al arbol binario
# archivo: arbol.py
#**************************************************************************#
class arbol():
	def __init__(self,info=None,hijoIzq=None,hijoDer=None):
	# contiene la informacion del nodo
		self.nodo = info
	# hijo izquierdo
		self.izq = hijoIzq
	# hijo derecho
		self.der = hijoDer
	# posicion que ocupa inicialmente cada nodo en el arbol al leerse el archivo de entrada1
		self.n = 0

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion insertar: Dada una determinada relacion padre-hijo si el arbol
# actual es el padre entonces inserta al hijo, de lo contrario continua
# buscando por los desendientes del padre. Coloca las posiciones del padre
# (posPadre) y del hijo1(posHijo1).
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	def insertar(self,padre, hijo1,posHijo1, posPadre):
		if self.nodo == None:
			self.nodo = padre
			self.izq = arbol(hijo1)
			self.n = posPadre
			self.izq.n = posHijo1
		elif self.nodo == padre:
			if self.izq == None:
				self.izq = arbol(hijo1)
				self.izq.n = posHijo1
			else:
				self.der = arbol(hijo1)
				self.der.n = posHijo1
		else:
			if self.izq != None:
				self.izq.insertar(padre,hijo1,posHijo1,posPadre)
			elif self.der != None:
				self.der.insertar(padre,hijo1,posHijo1,posPadre)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion insertar2: similar a insertar pero con dos argumentos hijos
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	def insertar2(self, padre, hijo1, hijo2, posHijo1, posHijo2, posPadre):
		if (self.nodo == None)  or (self.nodo == padre):
			self.nodo = padre
			self.izq = arbol(hijo1)
			self.der = arbol(hijo2)
			self.n = posPadre
			self.izq.n = posHijo1
			self.der.n = posHijo2
		else:
			if self.izq != None:
				self.izq.insertar2(padre,hijo1,hijo2,posHijo1,posHijo2,posPadre)
			if self.der != None:
				self.der.insertar2(padre,hijo1,hijo2,posHijo1,posHijo2,posPadre)
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion que va a insertar la raiz y luego los hijos de sus hijos
# recursivamente, la nueva raiz en cada iteracion sera un hijo de la anterior.
# Inserta tambien las posiciones del padre(posPadre) y de sus hijos
# (posHijo1,posHijo2), dependiendo se tiene uno o dos hijos. Estas dependen de 
# cuando se introdujieron en el diccionario.
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	def insertarRaiz(self,diccionario):
		listaPadres = list(diccionario.keys())
		listaHijos = list(diccionario.values())	
			
		# Busca cual es la raiz del arbol (el que no es hijo de nadie)
		raiz = determinarRaiz(diccionario)
		
		# Inserto la raiz del arbol con sus hijos
		for x in range(len(diccionario)):
			if listaPadres[x] == raiz and len(listaHijos[x]) == 3:
				padre = listaPadres[x]
				posPadre = listaHijos[x][0]
				hijo1 = listaHijos[x][1]
				posHijo1 = listaHijos[x][2]
				self.insertar(padre,hijo1,posHijo1,posPadre)
			elif listaPadres[x] == raiz and len(listaHijos[x]) == 5:
				padre = listaPadres[x]
				posPadre = listaHijos[x][0]
				hijo1 = listaHijos[x][1]
				posHijo1 = listaHijos[x][2]
				hijo2 = listaHijos[x][3]
				posHijo2 = listaHijos[x][4]
				self.insertar2(padre,hijo1,hijo2,posHijo1,posHijo2,posPadre)
		
		# Elimino la raiz del diccionario porque ya la agregue
		del diccionario[raiz]
		
		# Lamo recursivamente para seguir agregando las siguientes raices(hijos)
		# hasta que el diccionario este vacio
		if len(diccionario) != 0:
			self.insertarRaiz(diccionario)
		
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion corregirHijo: Dado un hijo si el arbol actual(padre) posee al hijo,
# lo elimino del arbol de lo contrario continuo buscando al hijo
# recursivamente por los nodos descendientes
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	def corregirHijo(self, hijo):
		if self.izq != None:
			if self.izq.nodo == hijo:
				newTree = self.izq
				self.izq = None
				return newTree
			else:
				newTree = self.izq.corregirHijo(hijo)
				if newTree != None:
					return newTree
		if self.der != None:
			if self.der.nodo == hijo:
				newTree = self.der
				self.der = None
				return newTree
			else:
				newTree = self.der.corregirHijo(hijo)
				if newTree != None:
					return newTree
		return None

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion corregirPadre: Dada una correcion padre-hijo si el arbol actual 
# es el padre, le agrego al hijo de lo contrario continuo buscando al padre
# de manera recursiva por los hijos descendientes.
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	def corregirPadre(self, padre, hijo):
		if self.nodo == padre:
			if self.izq == None:
				self.izq = hijo
			else:
				self.der = hijo
		else:
			if self.izq != None:
				self.izq.corregirPadre(padre,hijo)
			if self.der != None:
				self.der.corregirPadre(padre,hijo)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion que busca el primer hijo(valor) de un padre(clave) y sus posiciones
# corresposientes dentro del diccionario que contiene la relacion padre-hijos, 
# para poder agregar el nuevo hijo manteniendo los valores anteriores del padre
# (clave); posicion del padre(posPadre), primer hijo(primerHijo)
# y posicion primer hijo(posPrimerHijo)
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
def buscarPrimerHijo(diccionario,clavePadre):
	listaPadres = list(diccionario.keys())
	listaHijos = list(diccionario.values())
	for pos,padre in enumerate(listaPadres):
		if padre == clavePadre:
			posPadre = listaHijos[pos][0]
			primerHijo = listaHijos[pos][1]
			posPrimerHijo = listaHijos[pos][2]
			return [posPadre, primerHijo, posPrimerHijo]

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#Funcion que busca la posicion como padre(clave) de un hijo(valor) en el
# diccionario dado .
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
def buscarPosComoPadre(diccionario,hijo):
	listaPadres = list(diccionario.keys())
	listaHijos = list(diccionario.values())
	for pos,padre in enumerate(listaPadres):
		if padre == hijo:
			posComoPadre = listaHijos[pos][0]
			return posComoPadre
	
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion que determina cual es la raiz del arbol (el padre de todos)
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
def determinarRaiz(diccionario):
	listaPadres = list(diccionario.keys())
	listaHijos = list(diccionario.values())
	izq , der = [] , []
	for i in range(len(listaHijos)):
		if len(listaHijos[i]) == 5:
			izq += [] + [listaHijos[i][1]] + []
			der += [] + [listaHijos[i][3]] + []
		else:
			izq += [] + [listaHijos[i][1]] + []
		
	hijosIzq , hijosDer = set(izq) , set(der)
	padres = set(listaPadres)
	hijos = hijosIzq | hijosDer
	raiz = list(padres - hijos)[0]
	
	return raiz