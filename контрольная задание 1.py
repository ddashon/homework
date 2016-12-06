with open ('fr.txt', 'r', encoding = 'utf-8') as a:
    text=a.readlines()
    for line in text:
        if 'союз' in line:
            print (line)
        
