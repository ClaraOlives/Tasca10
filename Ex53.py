#Escriure un programa que ens mostri tots els números 
#parells fins arribar a 100. Ex: 2, 4, 6 ...., 98, 100. Prova-la. Fer el mateix amb els números senars.

def parells():
    a=[]
    for i in range(2,101,2):
        a.append(i)
        print("Els parells d'1 a 100 són {}".format(a))


def senars():
    a=[]
    for i in range(1,100,2):
        a.append(i)
        print("Els senars d'1 a 100 són {}".format(a))    
#PPrincipal
parells()
senars()
