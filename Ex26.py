#Definir una funció filtrar_paraules() que donada una llista de paraules i un número x, 
#retorni totes les paraules que tingui més d’x-caràcters.

def llegir_llista():
	#Cream una llista buida
	b = []
	a = "a"
	#Li deim que mentres el caracter introduit sigui diferent a '.' segueixi demanant, i ho afegeixi a la llista b
	while a != ".":
		a = input("Introdueixi la següent paraula: ")
		if a != ".":
			b.append(a)
		else:
			return b
		

def filtrar_paraules(a, num):
	b = list()
	i = 0
	for e in a:
		if num < len(e):
			b.append(e)
	return b

#Cridam a les funcions
x = llegir_llista()
a = input("Indicar la longitud de les paraules que vols filtrar: ")
y = filtrar_paraules(x,int(a))
print("Les paraules de igual o més tamany de ", a, " són: ", y)
