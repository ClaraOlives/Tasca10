#Li donam una llista buida a la funcio
def llegir_llista():
	a=[]
	c="a"
	#mentres la variable c sigui diferent a '.' segueixi demanant i els afegeixi a la llista
	while c!=".":
		c=input("Introdueixi un element de la llista i punt (.) per acabar: ")
		if c!=".":
			a.append(c)
	return a

#li pasem una llista buida, i li deim que si la longuitud de la llista a es major a 2 li 
# #pasi a b el valor de a sense l'element de la posicio 0 i -1
def eliminar_capicua(a):
	b=[]
	if len(a)>2:
		b=a[1:-1]
	return b
#Pprincipal
#li pasem les variables
x = llegir_llista()
y = eliminar_capicua(x)
print("La llista original {} s'ha transformat en la llista {}".format(x,y))