#Escriure un programa que sumi tots els números entre dos números donats, ambdós inclosos.


def sumar(a,b):
    suma=0
    if a>b:
        for i in range(b,a+1,1):
            suma+=i
    elif b>a:
        for i in range(a,b+1,1):
            suma+=i
    else:
        suma = 0
    return suma

#PPrincipal
a = int (input("Introdueixi el primer número: "))
b = int (input("Introdueixi el segon número: "))
c = sumar(a,b)
print("La suma dels números entre {} i {} és {}".format(a, b, c))
