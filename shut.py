#import os
#import shutil
#with open (f)
# windows C:\\Users\\student\\downloads
# linux, mac: /home/student/downloads
# текущая папка обозначается .
#os.path.abspath('.')
#os.getcwd()
# os.getrekt()
#os.path.join ('texts', '1.txt')
# ' '.join(['hello', 'world'])
#os.path.exists ('texts')
#os.listdir('.')
#os.listdir ('texts')
#for f in os.listdir('.'):
#    if f.endswith('.txt')

#os.mkdir ('corpus')
#os.makedirs ('')
#os.rename ('corpus', 'newc')
#os.path.isfile(r'texts')
#shutil.copy(r'texts\corpus1.txt', r'newc\corpus1.txt')
#shutil.copytree('texts', 'corpus')
# DANGER ZONE BISH
#os.remove(r'corpus\corpus2.txt')
#shutil.rmtree('corpus')
# 

import os
import shutil
name=input ('напишите што-нибудь')
f_name=name.replace(' ', '\\')
os.makedirs(f_name)

#n=int(input ('номерок не дадите?'))
#for i in range (1, n+1):
#    os.mkdir(str(i))
#    for m in range (1, i):
#       open(str(m), 'w')
    
    
