import numpy as np
import collections as collections

class Datos(object):
  
	TiposDeAtributos=('Continuo','Nominal')
 
  # TODO: procesar el fichero para asignar correctamente las variables tipoAtributos, nombreAtributos, nominalAtributos, datos y auxDic
	def __init__(self, nombreFichero):
		with open(nombreFichero, "r") as f:
			numFilas=f.readline().rstrip();		# NUMERO DE FILAS DEL CONJUNTO DE DATOS
			nombreAtributos=f.readline().rstrip().split(",");	# LISTA CON EL NOMBRE DE LOS ATRIBUTOS
			tipoAtributos=f.readline().rstrip().split(",");		# LISTA CON LOS TIPOS DE LOS ATRIBUTOS
			posiciones=[];
			numeroAtributos = len(nombreAtributos);
			datos = np.empty([numeroAtributos,int(numFilas)], dtype=int); 

			#Creacion del diccionario
			auxDic=[set() for i in range(numeroAtributos)];
			#print(auxDic);
			diccionarios = [None for i in range(numeroAtributos)];

			i=0;
			for x in tipoAtributos:
				if x == "Nominal":
					posiciones.append(i);
					i=i+1;

			content = f.read()
			file = content.split("\n")
			#auxDic = [collections.OrderedDict()]*numeroAtributos;

			for fila in file:
				i=0
				for x in fila.rstrip().split(","):
					print(x)
					print(i);
					if i in posiciones and x not in auxDic[i]:
						l=set();
						l = auxDic[i]
						l.add(x);
						auxDic[i]= l;
					i=i+1
			i=0		
			for dic in auxDic:
				j=0
				aux ={}
				for clave in sorted(dic):
					aux.update({clave:j})
					j=j+1
				diccionarios[i]=aux
				i=i+1    		
		print(diccionarios)
	#TODO: implementar en la práctica 1
	def extraeDatos(idx):
		pass


  