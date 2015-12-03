import os
import json


def clean(texto):
        output = ''
        for i in texto:
                if i.isalpha() or i.isspace():
                        output += i.lower()
        return output


def indexing(texto):
        index = {}
        numword = {}
        i = 1
        for word in texto.split():
                if len(word) > 4:
                        if word[:5] not in index:
                                index[word[:5]] = i
                                numword[i] = word[:5]
                                i += 1
        return index, numword


def indizar(texto, diccPal={}, diccNum={}):
        if not diccNum:
                i = 1
        else:
                i = max(diccNum)
        for word in texto.split():
                if len(word) > 4:
                        if word[:5] not in diccPal:
                                diccPal[word[:5]] = i
                                diccNum[i] = word[:5]
                                i += 1
        return diccPal, diccNum


def indexFile(data_path, filename, diccPal={}, diccNum={}):
        f = open(data_path+filename, 'r')
        j = 0
        for line in f:
                j += 1
                diccPal, diccNum = indizar(clean(line), diccPal, diccNum)
                # print(j)
        return (diccPal, diccNum)


def indexFolder(data_path, diccPal={}, diccNum={}):
        for filename in os.listdir(data_path):
                print(filename)
                diccPal, diccNum = indexFile(data_path, filename)
        return (diccPal, diccNum)


parent_folder = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
data_path = parent_folder + "\\parsed_files\\"
diccPal, diccNum = indexFolder(data_path)
with open('data.json', 'w') as outfile:
        json.dump(diccPal, outfile)
        outfile.write('\n')
        json.dump(diccNum, outfile)


