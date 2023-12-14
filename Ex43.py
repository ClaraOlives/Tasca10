#Escriure un programa que sumi els dígits d’un número donat i ens digui si la seva suma és parell o senar.

suma=0
x = input("Introdueix un número: ")
print("{} té {} dígits".format(x,len(x)))
for i in x:
	suma = suma + int(i)
print("La suma dels dígits del número {} és {}".format(x,suma))
if suma%2==0:
	print("És parell".format(x))
else:
	print("És senar".format(x))




