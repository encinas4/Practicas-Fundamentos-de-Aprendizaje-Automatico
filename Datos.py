import numpy as np

class Datos(object):
  
  TiposDeAtributos=('Continuo','Nominal')
 
  # TODO: procesar el fichero para asignar correctamente las variables tipoAtributos, nombreAtributos, nominalAtributos, datos y diccionarios
  def __init__(self, nombreFichero):
  	with open(nombreFichero, "r") as f:
			f.replace("/n","");
			numFilas=atoi(f.readline());
			atributos=f.readline();
			tipos=f.readline().split(",");
			posiciones=[];
			diccionario=[];

		i=0;
		for x in tipos:
			ele = [];
			diccionario.append(ele);

			if x == "Nominal":
				posiciones.append(i);
				i++;

		for x in f:
			fila = x.split(",");
			i=0;
			for y in fila:
				if i in posiciones and y not in diccionario[i]:
					diccionario[i].append(y);
				i++;

		for element in diccionario:
			element.tolist();
			element.sort();
			elemant.toarray();
		

    		
  # TODO: implementar en la práctica 1
  def extraeDatos(idx):
    pass


  