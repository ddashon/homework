a=open (input(), 'r', encoding='utf-8')
b=0
c=0
for line in a:
    arr=line.split()
    b=b+len(arr)
    for d in arr:
        if len(d)>10:
            c=c+1
            a.close()
            e=c/b*100
            print (e, '%')
        
