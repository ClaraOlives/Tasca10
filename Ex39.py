#Escriure un programa que si li introduïm un número menor de 100, 
#mostri la suma dels quadrats dels números que estan separats entre sí per a quatres posicions.
#Ex: 80 --> 76**2 + 72**2 + 68**2 + ... 

numero = int(input("Introdueix un nombre menor a 100: "))

suma = 0
for i in range(numero):
    suma = suma + (i**2)
print("La suma dels quadrats de 4 posicions menys de {} és {} ".format(numero,suma))











