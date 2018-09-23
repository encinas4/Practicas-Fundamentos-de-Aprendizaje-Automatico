import numpy as np

class Datos(object):
  
	TiposDeAtributos=('Continuo','Nominal')
 
  # TODO: procesar el fichero para asignar correctamente las variables tipoAtributos, nombreAtributos, nominalAtributos, datos y diccionarios
	def __init__(self, nombreFichero):
		with open(nombreFichero, "r") as f:
			numFilas=f.readline().rstrip();
			print(numFilas);
			atributos=f.readline().rstrip().split(",");
			print(atributos);
			tipos=f.readline().rstrip().split(",");
			print(tipos);
			posiciones=[];

			#Creacion del diccionario
			diccionario=[]*len(atributos);
			print(diccionario);

			i=0;
			for x in tipos:
				ele = {};
				diccionario.append(ele);

				if x == "Nominal":
					posiciones.append(i);
					i=i+1;

			for x in f:
				fila = x.rstrip().split(",");
				i=0;
				for y in fila:
					if i in posiciones:
						diccionario[i].update({y:len(diccionario[i])});
						 
					i=i+1;

			print(posiciones);
			print(diccionario);

			#Ordenamos los elementos del diccionario
			#for x in posiciones:
			#	diccionario[x] = sorted(diccionario[x]);

			#print(diccionario);

			#Rellenamos la polla de pelofeo que cabe en la matriz

    		
	#TODO: implementar en la práctica 1
	def extraeDatos(idx):
		pass


  