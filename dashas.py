# os.walk('.')
# for root, dirs, files in os.walk ('.'): print root
# for root, dirs, files in os.walk('.'): print (root, len(files))
# for root, dirs, files in os.walk(os.path.join('adres papki'):
# for f in files: with open(os.path.join(root, f)) as text:
# whole_corpus += text.read()
# for root, dirs, files os.walk ('.'): for d in dirs:
# if d.startswith('.'): dirs.remove (d):

# zadanie 1
#def delete_folder(path):
#    for root, dirs, files in os.walk(path, topdown=False):
#        for f in files:
#            os.remove(f)
#        for d in dirs:
#            os.rmdir(os.path.join(root,d))
#    os.rmdir(path)
#    print ('yep')

# zadanie 2
import os
def sup():
    for root,dirs,files in os.walk('.'):
        num=root.count('\\')
        root+ root.split('\\')[-1]
        print ('\t'*(num), root, sep='--')
        for f in files:
            print ('\t'*(num+1), f)
sup()
