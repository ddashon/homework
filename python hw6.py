def opentext (file.txt):
    forms = []
    with open (file.txt, 'r', encoding='utf-8') as a:
        text=a.read()
    forms=text.split()
    for i in range(len(forms)):
        forms[i]=forms[i].strip(.,?!:;())
    return forms

def word ():
    a=opentext(file.txt)
    b=[]
    for i in range (len(a)):
        if a[i][-1]=='s':
            if a[i][-2]=='u':
                if a[i][-3]=='o':
                    b.append(a[i])
    print (b)
    c=b.split()
    d=str.count(c)
    return d

    
    
    
