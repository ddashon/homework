import xml.etree.ElementTree as a
from os import walk

def sent(filename):
    tree = a.parse('./news/'+file)
    root = tree.getroot()
    tmp = root.findall('.//se')
    return(len(tmp))

def move(res,filename):
    res_file = open(filename, 'w')
    for item in res:
        res_file.write(item+'\n')

f = []
words = []
p = './news';
for (dirpath, dirnames, filenames) in walk(p):
    f.extend(filenames)
    break
for file in f:
    words.append(file+'\t'+str(sent(file)))
move(words,'counted.txt')
