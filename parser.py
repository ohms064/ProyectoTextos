import os


def parse(filename, data_path, parsed_path):
    f = open(data_path+filename, 'r')
    g = open(parsed_path+'parsed_'+filename, 'w')
    inDoc = False
    for line in f:
        line2 = line.replace("\n", " ")
        l = line.split()
        if (not l or l[0] == '</doc>'):
            # linea ne blanco o de fin de documenteo
            continue
        if((not inDoc) and (l[0] == '<doc')):
            # inicio de documento
            inDoc = True
            title = l[2][7:-1]+' '  # titulo:2nd word 7th chr
            # print('title: '+title)
            g.write(title)
        elif(inDoc and l[0] == 'ENDOFARTICLE.'):
            # fin del documento
            inDoc = False
            g.write("\n")

        else:
            # texto del documetno
            # print(line2, end=' ')
            g.write(line2)

    g.close()

parent_folder = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
data_path = parent_folder + "\\raw.es\\"
parsed_path = parent_folder + "\\parsed_files\\"
#filename = 'spanishText_10000_15000'
for filename in os.listdir(data_path):
    parse(filename, data_path, parsed_path)
print('enda')
