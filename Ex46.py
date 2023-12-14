#Definir una funció esta_ordenada() que donada una llista de números, 
#ens indiqui si està ordenada en ordre ascendent, descendent o no està ordenada. 
#Prova-la. Ex. esta_ordenada([3,2,1]) retorni està ordenada de forma descendent. 
#esta_ordenada([4,5,6]) retorni està ordenada de forma ascendent i qualsevol altres cas retorni no està ordenada.


def  esta_ordenada(a):
	b = a.copy()
	c = a.copy()
	b.sort()
	c.sort(reverse=True)
	if a == b:
		print("La llista {} està ordenada ascendentment {}".format(a, b))
	elif a==c:
		print("La llista {} està ordenada descendentment {}".format(a, c))
	else:
    		print("La llista {} no està ordenada {}".format(a, b))
			
def llegir_llista():
#Prec: Llegeix una llista de números
#Post: Retorna la llista llegida.
	b = []
	a = "a"
	while a != ".":
		a = input("Introdueixi el següent número: ")
		if a != ".":
			b.append(int(a))
		else:
			return b
#Pprincipal
a = llegir_llista()
esta_ordenada(a)
