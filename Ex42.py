#Escriure un programa que imprimeixi la taula de multiplicar d’un número donat (mínim 1 màxim 20).

taula = int(input("Vull la taula de multiplicar del nombre: "))


for j in range(20):
    print("{} x {} = {}".format(j+1,taula,(j+1)*taula))







