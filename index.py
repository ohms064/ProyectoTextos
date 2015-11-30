"""
Se encarga indexar los tokens de un archivo y convertir los tokens a enteros
"""

from os import walk
import json

for root, subdir, files in walk("raw.es\\Parseados"):
	for nombre in files:
		print("Creando indices de: " + nombre)
		vocabs = set()
		direccion = root + "\\" + nombre
		salida = "raw.es\\Indexados\\" + nombre
		with open(direccion, errors="ignore", encoding="utf8") as archivo:
			for line in archivo:
				for word in line.strip().split():
					vocabs.add(word)
		decoding = dict(list(enumerate(vocabs)))
		coding = dict([(y,x) for x,y in enumerate(vocabs)])
		with open(salida +"_INDEXMAP", "w") as index:
			json.dump(decoding, index)
		with open(direccion, errors="ignore", encoding="utf8") as archivo:
			with open(salida + "_INDEXED", "w") as indexed:
				for line in archivo:
					lineIndexed = ""
					for word in line.split():
						lineIndexed += str(coding[word]) + " "
					indexed.write(lineIndexed + "\n")