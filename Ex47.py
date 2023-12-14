#Definir una funció hi_ha_duplicats() que ens indiqui si una llista donada té 
#qualque element duplicat o no, no s’ha de modificar la llista donada. Prova-la.

def hi_ha_duplicats(a):
	seen = set()    
	dupes = [x for x in a if x in seen or seen.add(x)]  	 
	if len(dupes)>0:
		print("La llista {} té elements duplicats {}".format(a,dupes))
	else:
    		print("La llista {} no té elements duplicats {}".format(a,dupes))
			
#li pasem una llista buida i deim q mentres c sigui diferent a '.' li segueixi demanant i ho afegeixi a la llista a
def llegir_llista():
	a=[]
	c="a"
	while c!=".":
		c=input("Introdueixi un element de la llista i punt (.) per acabar: ")
		if c!=".":
			a.append(c)
	return a
		


#Pprincipal
#li pasem a la variable a la funcio i pasem una funcio per a que l'executi
a = llegir_llista()
hi_ha_duplicats(a)
