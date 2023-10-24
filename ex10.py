#Definició de la funció
def major(a):
    if a>18:
        print("És major d'edat")
    elif a<18:
        print("És menor d'edat")
    else:
        print("Té 18 anys")

#Programa principal
x = int(input("Introdueix la seva edat:"))
major(x)

   
    