"""
Script que limpia los archivos contenidos en "raw.es" que debe estar previamente descargado.
Elimina linea vacías, unas etiquetas que tiene el archivo, palabras pequeñas y algunos símbolos 
usando expresiones regulares.
"""

from os import walk
import re
import time

START_TIME = time.time()
pattern = "\s*<.*>\s*|\s*ENDOFARTICLE.\s*|[+*/=;,.:]" #Limpia el archivo

lil_words = r"\W*\b\w{1,3}\b" #Este patrón también elimina palabras pequeñas

for root, dirs, files in walk("raw.es"):
	for num, archivo in enumerate(files):

		direccion = str(root) + "\\" + str(archivo)
		if not direccion.endswith("_LIMPIO"):
			print("Limpiando: " + direccion)
			with open(direccion, errors='ignore', encoding='utf8') as archivo:
				with open(direccion + "_LIMPIO", "w", encoding='utf8') as salida:
					for line in archivo:
						line2 = re.sub(pattern, " ", line)
						line2 = re.sub(lil_words, "", line2)
						if line2.strip(): #Si la linea no está vacía
							salida.write(line2)

print("--- Total: {:05.2f} seconds ---".format((time.time() - START_TIME)))