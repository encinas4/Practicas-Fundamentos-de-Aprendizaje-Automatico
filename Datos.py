import numpy as np
import collections as collections

class Datos(object):
  
	TiposDeAtributos=('Continuo','Nominal')
 
  # TODO: procesar el fichero para asignar correctamente las variables tipoAtributos, nombreAtributos, nominalAtributos, datos y diccionarios
	def __init__(self, nombreFichero):
		with open(nombreFichero, "r") as f:
			numFilas=f.readline().rstrip();		# NUMERO DE FILAS DEL CONJUNTO DE DATOS
			nombreAtributos=f.readline().rstrip().split(",");	# LISTA CON EL NOMBRE DE LOS ATRIBUTOS
			tipoAtributos=f.readline().rstrip().split(",");		# LISTA CON LOS TIPOS DE LOS ATRIBUTOS
			posiciones=[];
			numeroAtributos = len(nombreAtributos);
			datos = np.empty([numeroAtributos,int(numFilas)], dtype=int); 

			#Creacion del diccionario
			#diccionarios=[]*numeroAtributos;
			#print(diccionarios);

			i=0;
			for x in tipoAtributos:
				if x == "Nominal":
					posiciones.append(i);
					i=i+1;

			content = f.read()
			file = content.split("\n")
			diccionarios = [collections.OrderedDict()]*numeroAtributos;

			for fila in file:
				i=0
				for x in fila.rstrip().split(","):
					print(x)
					print(i);
					if i in posiciones:
						diccionarios[i].update({x:0})
					i=i+1

			"""for x in f:
				fila = x.rstrip().split(",");
				i=0;
				for y in fila:
					if i in posiciones:
						diccionarios[i].update({y:len(diccionarios[i])});
						 
					i=i+1;"""



			print(posiciones);
			print(diccionarios);

    		
	#TODO: implementar en la práctica 1
	def extraeDatos(idx):
		pass


  