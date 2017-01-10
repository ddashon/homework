import random

def noun ():
    file=open('Mnoun.txt', 'r', encoding='utf-8')
    f=readlines()
    nouns=[]
    for line in f:
        nouns.append(line.split(" "))
        return random.choise(nouns)
def verb ():
    file=open ('verb1.txt', 'r', encoding='utf-8')
    f=readlines()
    verbs=[]
    for line in f:
        verbs.append(line.split(" "))
        return random.choise(verbs)
def adj ():
    file=open ('adj.txt', 'r', encoding='utf-8')
    f=readlines()
    adjectives=[]
    for line in f:
        adjectives.append(line.split(" "))
        return random.choise(adjectives)

def noun2 ():
    file=open ('noun2.txt','r', encoding='utf-8')
    f=readlines()
    plnouns=[]
    for line in f:
        plnouns.append(line.split(" "))
        return random.choise(plnouns)
def conj():
    conjs=["и", "или", "но", "да", "однако", "зато", "когда", "пока", "потому что", "чтобы", "то есть"]
    return "," + random.choise(conjs)
def noun3 ():
    file=open ('noun3.txt', 'r', encoding='utf-8')
    f=readlines ()
    fnouns=[]
    for line in f:
        fnouns.append (line.split(" "))
        return random.choise(fnouns)
def 2verb ():
    file=open ('2verb.txt', 'r', encoding ='utf-8')
    f=readlines ()
    2verbs=[]
    for line in f:
        2verbs.append (line.split(" "))
        return random.choise (2verbs)
def sen ():
    return (noun+" "+verb+" "+adj+" "+noun2+" "+conj+" "+noun3+" "+2verb+"."

for i in range(5):
            print (sen())

        
