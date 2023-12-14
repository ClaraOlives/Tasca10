#Definir una funció crear_llista_fitxer() 
#on llegeixi un fitxer i transformi cada paraula llegida en un element de la llista. Prova-la.

def crear_llista_fitxer(fitxer):
	with open(fitxer, 'r') as f:
		llista = f.readlines()
	lparaules = [linea.rstrip('\n')for linea in llista] 
	print(lparaules)
	f.close()
		

#Pprincipal
crear_llista_fitxer('/home/cicles/AO/Tasca10/prova')# Ruta absoluta