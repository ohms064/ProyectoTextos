"""
Se encarga indexar los tokens de un archivo y convertir los tokens a enteros
"""

from os import walk
import json
def createIndexMap(subdir="raw.es\\Parseados", encode="utf8"):
	"""
		Crea el indexmap que describe como fue codificado el archivo para poder decodificarlo.
		-La condificación se crea para todos los archivos de la carpeta subdir.
		Entradas:
			subdir: La carpeta donde se encuentran los archivos a codificar.
			encode: La condificación que tiene los archivos de dicha carpeta.
		Salidas:
			decoding: Diccionario que indica como decodificar los archivos.
			coding: Diccionario que indica como codificar los archivos.
	"""
	vocabs = set() #El vocabulario es un conjunto para evitar palabras repetidas
	for root, dirs, files in walk(subdir):
		numFiles = len(files)
		for num, nombre in enumerate(files):
			print("Obteniendo indices de: " + nombre)
			print("\t {} de {}".format(num+1, numFiles))
			direccion = root + "\\" + nombre
			with open(direccion, errors="ignore", encoding=encode) as archivo:
				for line in archivo:
					for word in line.strip().split():
						vocabs.add(word)
		break #Por si existieran más subcarpetas
	decoding = dict(list(enumerate(vocabs))) #Creamos el diccionario para la decodificación
	coding = dict([(y,x) for x,y in enumerate(vocabs)]) #Creamos la codifiación
	print("Creando indexmap")
	with open(root.split("\\")[0] + "\\Indexados\\indexmap.json", "w", encoding=encode) as index:
		json.dump(decoding, index, indent=1)
	print("¡Se terminó de crear el mapa de índices!")
	return decoding, coding

def createIndexFiles(coding, subdir="raw.es\\Parseados", encode="utf8"):
	"""
		A partir de un diccionario se codifican los archivos dentro de la carpeta subdir.
		Entradas:
			subdir: La carpeta donde se encuentran los archivos.
			encode: La condifiación de todos los archivos de dicha carpeta.
			coding: Obligatorio. El diccionario que indica la codificación. (dict[palabra] = codigo)
	"""
	for root, dirs, files in walk(subdir):
		numFiles = len(files)
		for num, nombre in enumerate(files):
			print("Codificando: " + nombre)
			print("\t {} de {}".format(num+1, numFiles))
			direccion = root + "\\" + nombre
			salida = root.split("\\")[0] +  "\\Indexados\\" + nombre
			with open(direccion, errors="ignore", encoding=encode) as archivo:
				with open(salida + "_INDEXED", "w") as indexed:
					for line in archivo:
						lineIndexed = ""
						for word in line.split():
							lineIndexed += str(coding[word]) + " "
						indexed.write(lineIndexed + "\n")
		break #Por si existieran más subcarpetas

if __name__ == "__main__":
	decoding, code = createIndexMap(encode="cp1252")
	createIndexFiles(encode="cp1252", coding=code)