#Escriure un programa que demani dues paraules i ens digui si rimen o no. Rimen quan coincideixen 
#les 3 darreres lletres i rimen un poc quan coincideixen les 2 darreres, si no ens ha de dir que no rimen.

#Feim dues variables
paraula1 = input("Introdueix una paraula per rimar: ")
paraula2 = input("Introdueix la segona paraula per rimar: ")

#li deim que si les 3 derreres lletres de la primera paraula son iguals a les de la segona escrigui que rimen
if paraula1[-3:]==paraula2[-3:]:
    print("La paraula {} i {} rimen".format(paraula1,paraula2))

#li deim que si les 2 derreres lletres de la primera paraula son iguals a les de la segona escrigui que rimen un poc
elif paraula1[-2:]==paraula2[-2:]:
    print("La paraula {} i {} rimen un poc".format(paraula1,paraula2))

#li deim que si la derrera lletra de la primera paraula es igual a la de la segona escrigui que nomes rima la darrera
elif paraula1[-1:]==paraula2[-1:]:
    print("La paraula {} i {} només rimen la derrera lletra".format(paraula1,paraula2))

