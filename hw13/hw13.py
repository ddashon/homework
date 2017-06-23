import os
import shutil
folder='.'
print (os.listdir('.'))
for f in os.listdir('.'):
    with open (os.path.join(folder, f)) as text:
        print('file: ', f)
a=str_word_count(f, ' ')
filelist = [f for f in os.listdir('.') if os.path.isfile(f)]
if a>1:
    print(filelist)
