"""
Se encarga indexar los tokens de un archivo y convertir los tokens a enteros
"""

from os import walk
import json
def createIndexMap(subdir="raw.es\\Parseados", encode="utf8"):
	vocabs = set()
	for root, dirs, files in walk(subdir):
		numFiles = len(files)
		for num, nombre in enumerate(files):
			print("Obteniendo indices de: " + nombre)
			print("\t {} de {}".format(num+1, numFiles))
			direccion = root + "\\" + nombre
			salida = root.split("\\")[0] +  "\\Indexados\\" + nombre
			with open(direccion, errors="ignore", encoding=encode) as archivo:
				for line in archivo:
					for word in line.strip().split():
						vocabs.add(word)
	decoding = dict(list(enumerate(vocabs)))
	coding = dict([(y,x) for x,y in enumerate(vocabs)])
	with open(salida + "\\Indexados\\indexmap.json", "w", encoding=encode) as index:
		json.dump(decoding, index, indent=1)
	print("¡Se terminó de crear el mapa de índices!")
	return decoding, coding

def createIndexFiles(subdir="raw.es\\Parseados", encode="utf8", coding=None):
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

if __name__ == "__main__":
	decoding, code = createIndexMap(encode="cp1252")
	createIndexFiles(encode="cp1252", coding=code)