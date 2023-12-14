#Cream una variable que ens demana que introdueixis un nombre
numero = input("Introdueix un nombre entre 1 i 900000: ")
#li pasam a la variable que contengui el nombre de xifres del nombre introduit
lon = len(numero)
print("El nombre {} té {} dígits".format(numero,lon))