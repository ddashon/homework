import re
dic = {}
with open('f.xml') as f:
    for row in f:
        if(re.match(r'<w lemma=".*" type=".*">.*</w>',row)):
        	arr = row.split("\"")
        	key = arr[3]
        	if key in dic:
        		dic[key]=dic[key]+1
        	else:
        		dic[key] = 1;
    for key in dic.items():
        print(key+" "+"\r\n")
 
