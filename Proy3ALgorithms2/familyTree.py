#**************************************************************************#
# Autoras: Adriana Devera 09-11286
#          Natascha Gamboa 12-11250
#
# Descripción: TAD que contiene el arbol genealógico, manejo de los archivos de
# entrada(1 y 2) y el archivo de salida
# archivo: familyTree.py
#**************************************************************************#
import sys
from arbol import *
from imprimirArbol import *

class ArbolGenealogico():
	def __init__(self):
		#Arbol genealogico
		self.raiz = arbol()

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion crearArbol: Carga la informacion del archivo de entrada1 (archivoE1)
# para construir el arbol genealogico incial. Guarda los padres con sus hijos
# en un diccionario(DiccPadresHijos) de la siguiente manera:
# {padre: (posicion padre, hijo1, posicion hijo1, hijo2, posicion hijo2)}
#
# Las posiciones dependen de en que momento se lee en el archivo y esa sera
# su posicion en el arbol simepre, incluso luego de modificar el arbol con el 
# archivo de entrada2.
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	def crearArbol(self,archivoE1):
		archivo = open(archivoE1,"r")
		# Posicion que ocupara inicialmente cada hijo y padre al leerse el archivo
		n = 0
		
		DiccPadresHijos = {}
		for line in archivo:
			if len(line.split()) == 2:
				padre , hijo1 = line.split()[0] , line.split()[1]
				
				# Si le voy a agrgar otro hijo(valor) a un padre(clave) que ya tiene uno
				if padre in list(DiccPadresHijos.keys()):
					# Si hijo no es padre le coloco su posicion al leerlo
					if hijo1 not in list(DiccPadresHijos.keys()):
						# Busco lo que ya tenia el padre(clave) como hijo(valor) y las posiciones de c/u
						primerHijo = buscarPrimerHijo(DiccPadresHijos,padre)
						posPadre = primerHijo[0]
						nombrePrimerHijo = primerHijo[1]
						posPrimerHijo = primerHijo[2]
						DiccPadresHijos[padre] = posPadre, nombrePrimerHijo, posPrimerHijo, hijo1, n+1
					# Sino le coloco su posicion como padre para no sobreescribir la verdadera
					else:
						primerHijo = buscarPrimerHijo(DiccPadresHijos,padre)
						posComoPadre = buscarPosComoPadre(DiccPadresHijos,hijo1)
						posPadre = primerHijo[0]
						nombrePrimerHijo = primerHijo[1]
						posPrimerHijo = primerHijo[2]
						DiccPadresHijos[padre] = posPadre, nombrePrimerHijo, posPrimerHijo, hijo1, posComoPadre
				# Sino le agrego su primer hijo
				else:
					if hijo1 not in list(DiccPadresHijos.keys()):
						DiccPadresHijos[padre] = n, hijo1, n+1
					else:
						posComoPadre = buscarPosComoPadre(DiccPadresHijos,hijo1)
						DiccPadresHijos[padre] = n+1, hijo1, posComoPadre
				n += 1
			else:
				padre = line.split()[0]
				hijo1 , hijo2 = line.split()[1] , line.split()[2]
				# Si ninguno de los hijos es padre(clave) les agrego la posicion al leerlo
				if hijo1 not in list(DiccPadresHijos.keys()) and hijo2 not in list(DiccPadresHijos.keys()):
					DiccPadresHijos[padre] = n, hijo1, n+1, hijo2, n+2
				# Si uno de los hijos es padre(clave) busco su posicion como padre para no sobreescribir la verdadera
				elif hijo1 not in list(DiccPadresHijos.keys()) and hijo2 in list(DiccPadresHijos.keys()):
					posComoPadre = buscarPosComoPadre(DiccPadresHijos,hijo2)
					DiccPadresHijos[padre] = n+1, hijo1, n+2, hijo2, posComoPadre
				elif hijo1 in list(DiccPadresHijos.keys()) and hijo2 not in list(DiccPadresHijos.keys()):
					posComoPadre = buscarPosComoPadre(DiccPadresHijos,hijo1)
					DiccPadresHijos[padre] = n+1, hijo1, posComoPadre, hijo2, n+2
				# Si los dos hijos son padre(clave) busco sus posiciones como padres para no sobreescribir la verdadera
				else:
					posComoPadreHjo1 = buscarPosComoPadre(DiccPadresHijos,hijo1)
					posComoPadreHijo2 = buscarPosComoPadre(DiccPadresHijos,hijo2)
					DiccPadresHijos[padre] = n+2, hijo1, posComoPadreHijo1, hijo2, posComoPadreHijo2
				n += 2
		archivo.close()
		
		# Inserta la raiz y luego los demas hijos. Se toman los padres y los hijos del
		# diccionario DiccPadresHijos
		print(DiccPadresHijos)
		self.raiz.insertarRaiz(DiccPadresHijos)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion modificarArchivo
# Realiza las modificaciones proporcionadas por el segundo archivo de 
# entrada (archivoE2) en el arbol inicial. Devuelve el arbol modificado.
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	def modificarArbol(self,archivoE2):
		archivo = open( archivoE2,"r")
		for line in archivo:
			padre = line.split()[0]
			hijo = line.split()[1]
			newChild = self.raiz.corregirHijo(hijo)
			self.raiz.corregirPadre(padre, newChild)
		archivo.close()

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion imprimir junto con Funcion imprimirRecursivo(R): Imprime el Arbol
# Genealogico en el archivo de salida(archivoS) mediante la siguiente sintaxis:
# padre (n): hijo1 (n) hijo2 (n)
# hijo1 (n): hijo1 (n) hijo2 (n)
# hijo2 (n): hijo1 (n) hijo2 (n)
# 
# Asi sucesivamente para cada hijo. Se imprime desde hijo izquierdo al derecho
# Donde n es la posicion que ocupa en el arbol inicialmente(al leerse el archivo
# de entrada1). Luego se imprime el arbol en Pre, Post e In - Orden
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	def imprimirR(self,archivo,padre):
		arbol = ''
		arbol += '\n' + padre.nodo + ' (' + str(padre.n) + '): '
		if padre.izq != None and padre.izq.nodo != None:
			hijoIzq = padre.izq.nodo
			arbol += hijoIzq + ' (' + str(padre.izq.n) + ') '
		if padre.der != None and padre.der.nodo != None:
			hijoDer = padre.der.nodo
			arbol += hijoDer + ' (' + str(padre.der.n) + ')'
		
		archivo.write(arbol)
		
		if padre.izq != None:
			if padre.izq.izq != None or padre.izq.der != None:
				self.imprimirR(archivo,padre.izq)
		if padre.der != None:
			if padre.der.izq != None or padre.der.der != None:
				self.imprimirR(archivo,padre.der)
	
	def imprimir(self,archivoS):
		archivo = open(archivoS,'w')
		
		## Se imprime el arbol completo
		arbol = self.raiz
		self.imprimirR(archivo,arbol)
		
		## se imprime en pre,pos e in orden el arbol
		archivo.write('\n\nPre-Orden: ')
		archivo.write(imprimirPreOrden(self.raiz))
		archivo.write('\nPost-Orden: ')
		archivo.write(imprimirPostOrden(self.raiz))
		archivo.write('\nIn-Orden: ')
		archivo.write(imprimirInOrden(self.raiz))

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Funcion que imprime un error si no se pasan los argumentos correctos
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
def printError(argumentos):
	ERROR = "Error en los argumentos, USO: python3 familyTree.py <entrada1> <entrada2> <salida>"
	if len(argumentos) != 4:
		print(ERROR)
		sys.exit(1)
	return str(argumentos[1]), str(argumentos[2]) , str(argumentos[3])

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#			Programa Principal
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
if __name__=="__main__":
	entrada1, entrada2, salida = printError(sys.argv)
	arbol = ArbolGenealogico()
	arbol.crearArbol(entrada1)
	arbol.modificarArbol(entrada2)
	arbol.imprimir(salida)