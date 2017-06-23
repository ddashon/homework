import xml.etree.ElementTree as a
from os import walk
import pandas as q

def second(filename):
    tree = a.parse('./news/'+file)
    root = tree.getroot()
    name = root.find(".//*[@name='author']")
    topic = root.find(".//*[@name='topic']")
    return(name.attrib['content']+":"+topic.attrib['content'])

f = []
d = []
p = './news';
for (dirpath, dirnames, filenames) in walk(p):
    f.extend(filenames)
for file in f:
    tmp = second(file).split(':')
    tmp_arr = [file,tmp[0],tmp[1]]
    d.append(tmp_arr)
df = q.DataFrame(d,columns=["название","автор","тема"])
df.to_csv("2.csv", sep=';', encoding='windows-1251')
