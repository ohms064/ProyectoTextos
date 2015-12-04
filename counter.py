import json
from os import walk

def countDocsWords(fileName, encode="utf8"):
	"""
		Cuenta cuantas palabras y lineas(documentos) hay en un archivo.
	"""
	with open(fileName, encoding=encode, errors="ignore") as f:
		count = 0
		for numLine, line in enumerate(f):
			count += len(line.split())
	return count, numLine

def countDocs(subdir="raw.es\\Parseados", limit=0, encode="utf8"):
	"""
		Cuenta cuantas lineas(documentos) hay en varios textos de una carpeta
		Entradas:
			subdir: La carpeta que se buscarán los archivos
			limit: El límite de archivos que se quieren ver, si es menor o igual 
			a cero se tomarán todos los archivos de la carpeta..
			encode: La codificación de los archivos.
	"""
	print("Obteniendo número de documentos")
	countWord = 0
	numLine = 0
	
	for root, dirs, files in walk(subdir):
		if limit <= 0:
			limit = len(files)
		for num, nombre in enumerate(files):
			x, y = countDocsWords(root + "\\" + nombre, encode)
			countWord += x
			numLine += y
			if num == limit:
				break
	return countWord, numLine