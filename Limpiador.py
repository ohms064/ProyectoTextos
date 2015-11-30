"""
Script que limpia los archivos contenidos en "raw.es" que debe estar previamente descargado.
Elimina linea vacías, unas etiquetas que tiene el archivo, palabras pequeñas y algunos símbolos 
usando expresiones regulares.
"""

from os import walk
import re
import time

START_TIME = time.time()
pattern = "\s*ENDOFARTICLE.\s*|[+*=;,.:]" #Limpia el archivo
fin = ".*</doc>.*"
lil_words = r"\W*\b\w{1,2}\b" #Este patrón también elimina palabras pequeñas

for root, dirs, files in walk("raw.es"):
	for num, archivo in enumerate(files):

		direccion = str(root) + "\\" + str(archivo)
		if not "_LIMPIO" in direccion and not "_LIMPIO_PARSED" in direccion:
			print("Limpiando: " + direccion)
			with open(direccion, errors='ignore', encoding='utf8') as archivo:
				with open(direccion + "_LIMPIO", "w", encoding='utf8') as salida:
					for line in archivo:
						line2 = re.sub(pattern, " ", line)
						line2 = re.sub(lil_words, "", line2)
						if (line2.strip() and len(line2.split()) > 1) or re.match(fin, line): #Si la linea no está vacía y contiene más de una palabra
							salida.write(line2.lstrip())

print("--- Total: {:05.2f} seconds ---".format((time.time() - START_TIME)))