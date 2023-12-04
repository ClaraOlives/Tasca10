def llegir_llista():
    a = 0
    l = []
    while a!= '.':
        a = input("Introdueix un element: ")
        if a != '.':
            l.append(int(a))
        else:
            return l
       



def sumar_llista(l):
    s=0
    for e in l:
        s+=e
    print("La suma de tots els elements de la llista {}, és {}".format(l,s))

def multiplicar_llista(l):
    m=1
    for e in l:
        m*=e
    print("La multiplicació de tots els elements de la llista {}, és {}".format(l,m))

l = llegir_llista()
sumar_llista(l)
multiplicar_llista(l)




