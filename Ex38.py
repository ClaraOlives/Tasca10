#Escriure un programa que calculi en quan s'hauria convertit el nostre capital al final dels anys. 
#Per això li hem de demanar a l’usuari que introdueixi la quantitat a sol·licitar (mínim 50000€ màxim 800000€),
# un interès (mínim 0.5% i màxim 13%) i el número d’anys (mínim 3 anys - màxim 40 anys).  
#La fórmula per calcular-ho és: Cfinal = Cinicial * (1 + interés/100) **  anys.  
#Ex. 10000€ a 4.5% d’interés a 20 anys s’ha de convertir en 24117.14€




quantitat = float(input("Introdueix la quantitat a sol·licitar(min 50000, màx 80000): "))
interes = float(input("Introdueixi l'interés (0.5 i 13) percentatge: "))
anys = int(input("Introdueixi el número d'anys: "))
cfinal = quantitat * (1 + interes/100)**anys

print("El capital {}€ a un interés del {}% a {} anys resulta que pagarem {:.2f}€".format(quantitat, interes, anys, cfinal))
