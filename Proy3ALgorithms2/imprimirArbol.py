#!/usr/bin/python3
#**************************************************************************#
# Autoras: Adriana Devera 09-11286
#          Natascha Gamboa 12-11250
#
# Descripción: Imprime el arbol en recorrido InOrden, PreOrden o PostOrden
# archivo: imprimirArbol.py
#**************************************************************************#

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion que imprime el arbol en recorrido InOrden
# primero el hijo izquierdo luego el padre y luego el hijo derecho
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
def imprimirInOrden(arbol):
	arbolPadre = ''
	arbolIzq = ''
	arbolDer = ''
	if arbol != None:
		if arbol.izq != None:
			arbolIzq = imprimirInOrden(arbol.izq)
		arbolPadre = arbol.nodo + " "
		if arbol.der != None:
			arbolDer = imprimirInOrden(arbol.der)
	
	return arbolIzq + arbolPadre + arbolDer

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion que imprime el arbol en recorrido PreOrden
# primero el padre luego el hijo izquierdo y luego el hijo derecho
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
def imprimirPreOrden(arbol):
	arbolPadre = ''
	arbolIzq = ''
	arbolDer = ''
	if arbol != None:
		arbolPadre = arbol.nodo + " "
		if arbol.izq != None:
			arbolIzq = imprimirPreOrden(arbol.izq)
		if arbol.der != None:
			arbolDer = imprimirPreOrden(arbol.der)
	
	return arbolPadre + arbolIzq + arbolDer

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion que imprime el arbol en recorrido PostOrden
# primero el hijo izquierdo luego el hijo derecho y luego el padre
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
def imprimirPostOrden(arbol):
	arbolPadre = ''
	arbolIzq = ''
	arbolDer = ''
	if arbol != None:
		if arbol.izq != None:
			arbolIzq = imprimirPostOrden(arbol.izq)
		if arbol.der != None:
			arbolDer = imprimirPostOrden(arbol.der)
		arbolPadre = arbol.nodo + " "
	
	return arbolIzq + arbolDer + arbolPadre
