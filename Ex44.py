#Escriure un programa que mostri els dígits parells d’un número donat.
suma = 0
numero = input("Introdueix un número: ")
print("El número {} té {} dígits".format(numero, len(numero)))
for i,e in enumerate(numero):
	if i%2==0:
		print("El numero parell de {} és {} ".format(numero,e))



