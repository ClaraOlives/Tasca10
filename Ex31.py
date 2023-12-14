#Cream una funcio que contengui una varible amb valor 0 i una altra que contengui una llista buida
def noms_que_comencen_per(llista,lletra):
	comptador = 0
	llnom= []
	#Per cada element de la llista si l'element 0 es igual a la lletra la afeguim a la llista
	for e in llista:
		if e[0]==lletra:
			llnom.append(e)
			comptador += 1
	print("El número de noms que comencen per el caràcter {} són: {} i són: {}".format(lletra, comptador, llnom))

def llegir_llista():
	#Prec: Llegeix una llista de paraules, en el nostre cas de noms
	#Post: Retorna la llista llegida.
	b = []
	a = "a"
	while a != ".":
		a = input("Introdueixi el següent nom: ")
		if a != ".":
			b.append(a)
		else:
			return b
    
# Programa principal
noms = llegir_llista()
noms_que_comencen_per(noms,"a")

