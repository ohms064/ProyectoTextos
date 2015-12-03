"""
Script que hace un parse del archivo para que cada documento definido entre etiquetas <doc></doc> se escriba
en una sóla linea.
"""

from os import walk
import re
import time #Sólo para contar el tiempo que tarda el programa

init = ".*<doc.*>.*"
fin = ".*</doc>.*"
ignorar = "\s*ENDOFARTICLE.\s*"

START_TIME = time.time() 
lineWrite = ""

for root, dirs, files in walk("raw.es"): #Obtiene la lista de los archivos
	for num, archivo in enumerate(files): #Itera sobre la lista de los archivos
		direccion = str(root) + "\\Parseados\\" + str(archivo) #Obtenemos la dirección, se asume que existe la carpeta Parseados dentro de raw.es
		if not "_PARSED" in direccion and direccion.endswith("_LIMPIO"):
			print("Parsing: " + direccion)
			with open(direccion, errors='ignore', encoding='utf8') as archivo:
				with open(direccion + "_PARSED", "w", encoding='utf8') as salida:
					for line in archivo:
						if re.match(init, line):
							lineWrite = ""
						elif re.match(fin, line):
							salida.write(lineWrite.lstrip() + "\n")
						elif not re.match(ignorar, line):
							lineWrite += " " + line.strip()


print("--- Total: {:05.2f} seconds ---".format((time.time() - START_TIME)))