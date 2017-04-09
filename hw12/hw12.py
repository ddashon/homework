def open_format(crab):
    a = []
    with open (crab.txt, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = re.sub('\.\.\.|[\.\?]', '!', text)
    a = text.split('!')[:-1]
    for i in range(len(a)):
         a[i] = re.sub('[<>\*\.«»,\'\"]','', a[i])
         a[i] = a[i].strip()
    return a
def repeat():
    work=open_format (crab.txt)
    words=re.findall(r'([a-zA-Z]+(?:[?:[\'-][a-zA-Z]+)*)',s)
    res=[]
    for x in range (a,z):
        res.append (x)
    print (res)
