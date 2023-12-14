#Escriure un programa que ens permeti jugar a una versió simplificada del joc de MasterMind, 
#el joc consisteix en crear un codi de 4 xifres i demanar a l’usuari que vagi introduint codis de 4 xifres fins que l’endevini. 
#En cada jugada, li direm quants número ha encertat (estan en la posició correcte) 
#i quants coincideixen (i són, però no estan en la posició correcte).


import random

codi_4 = "".join(list(map(lambda x: str(x), random.sample(range(0,9), 4))))
print("Mastermind \n Adivina el nombre de 4 xifres.")

codi = input("Introdueix el possible codi de 4 xifres: ")

intents = 0
while codi != codi_4:
    intents += 1 
    nombres_i_posicions_correctes = 0
    nombres_correctes = 0
    

    for i in range(4):
        if codi[i] == codi_4[i]:
            nombres_i_posicions_correctes += 1
            
        if codi[i] in codi_4:
            nombres_correctes += 1
    
    print("Nombres i posicions correctes: {}. Nombres correctes: {}".format(nombres_correctes, nombres_i_posicions_correctes))
    codi = input("Intenta a introduir un altre codi de 4 xifres: ")
if codi == codi_4:
    print("Has endevinat el codi en {} intents".format(intents))