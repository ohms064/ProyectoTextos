"""
Script que hace un parse del archivo para que cada documento definido entre etiquetas <doc></doc> se escriba
en una sóla linea.
"""

from os import walk
import re
def parser(subdir="raw.es", encode="utf8"):
	"""
		Función que convierte un archivo del corpus de wikicorpus a un archivo donde cada linea 
		es un documento en lugar de separarlo en etiquetas. Se hace un filtrado para evitar
		palabras individuales, palabras pequeñas y símbolos.
		Entradas:
			subdir: La carpeta donde se encuentran los archivos a parsear.
			encode: La codificación que tienen los archivos que se quieren parsear. Se asume que todos
			los archivos de la carpeta tienen la misma codificación.
	"""
	pattern = "\s*ENDOFARTICLE.\s*|\W" #Limpia el archivo
	lil_words = r"\W*\b\w{1,3}\b" #Este patrón también elimina palabras pequeñas
	init = ".*<doc.*>.*"
	fin = ".*</doc>.*"
	espacios = "\s+"
	lineWrite = ""
	for root, dirs, files in walk(subdir): #Obtiene la lista de los archivos
		numFiles = len(files)
		for num, archivo in enumerate(files): #Itera sobre la lista de los archivos
			direccion = str(root) + "\\" + str(archivo)
			direccionParsed = str(root) + "\\Parseados\\" + str(archivo) #Obtenemos la dirección, se asume que existe la carpeta Parseados dentro de raw.es
			if "_PARSED" not in direccion:
				print("Parsing: " + direccion)
				print("\t {} de {}".format(num+1, numFiles))
				with open(direccion, errors='ignore', encoding=encode) as archivo:
					with open(direccionParsed + "_PARSED", "w", encoding=encode) as salida:
						for line in archivo:
							if re.match(init, line):
								lineWrite = ""
							elif re.match(fin, line) and len(lineWrite.split()) > 30:
								salida.write(lineWrite.lstrip() + "\n")
							else:
								line = re.sub(pattern, " ", line)
								line = re.sub(lil_words, "", line)
								line = re.sub(espacios, " ", line)
								if len(line.strip().split()) > 1:
									lineWrite += " " + line.strip().lower()
	print("Se terminó de hacer el parser")


if __name__ == "__main__":
	parser(encode="cp1252")