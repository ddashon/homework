import os
os.listdir('.')
file_tree=os.walk('.')
names = {}
for root, dirs, files in os.walk('.'):
    for f in files:
       name = f.split('.')[0]
       if name not in names:
           names[name]=1
           print(len(names))
