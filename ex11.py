#Funcions

def menu_principal():
    print("""
        Menú principal:
        1. Calculadora enters
        2. Calculadora reals
        3. Sortir
          """)
    a = int(input("Elegeix una opció: "))
    return a    
#enters
def suma():
    x = int(input("Introdueix el primer número a sumar: "))
    y = int(input("Introdueix el segon número a sumar: "))
    print("Resultat: {} + {} = {}".format(x, y, x+y))
def resta():
    x = int(input("Introdueix el primer número a restar: "))
    y = int(input("Introdueix el segon número a restar: "))
    print("Resultat: {} - {} = {}".format(y, x, y-x))

def multiplicacio():
    x = int(input("Introdueix el primer número a multiplicar: "))
    y = int(input("Introdueix el segon número a multiplicar: "))
    print("Resultat: {} * {} = {}".format(y, x, y*x))

def divisio():
    x = int(input("Introdueix el primer número a dividir: "))
    y = int(input("Introdueix el segon número a dividir: "))
    print("Resultat: {} / {} = {}".format(y, x, y/x))

def canvidevalors():
    x = int(input("Ingresa el primer nombre:"))
    y = int(input("Ingresa el segon nombre:"))

#reals

def sumareals():
    x = float(input("Introdueix el primer número a sumar: "))
    y = float(input("Introdueix el segon número a sumar: "))    
    print("Resultat: {} + {} = {}".format(x, y, x+y))
def restareals():
    x = float(input("Introdueix el primer número a restar: "))
    y = float(input("Introdueix el segon número a restar: "))
    print("Resultat: {} - {} = {}".format(y, x, y-x))

def multiplicacioreals():
    x = float(input("Introdueix el primer número a multiplicar: "))
    y = float(input("Introdueix el segon número a multiplicar: "))
    print("Resultat: {} * {} = {}".format(y, x, y*x))

def divisioreals():
    x = float(input("Introdueix el primer número a dividir: "))
    y = float(input("Introdueix el segon número a dividir: "))
    print("Resultat: {} / {} = {}".format(y, x, y/x))

def canvidevalorsreals():
    x = float(input("Ingresa el primer nombre:"))
    y = float(input("Ingresa el segon nombre:"))

def opreals():
    c=1
    while c>0:
        print("""
    Operacions:

        1) Suma
        2) Resta
        3) Multiplicació
        4) Divisió
        5) Canvi de valors
        6) Sortir
          """)
        c = int(input("Elegeix una opció: "))
        match c:
            case 1:
                sumareals()
            case 2:
                restareals()
            case 3:
                multiplicacioreals()
            case 4:
                divisioreals()
            case 5:
                canvidevalorsreals()
            case 6:
                c=-1 


def openters():
    b=1
    while b>0:
        print("""
    Operacions:

        1) Suma
        2) Resta
        3) Multiplicació
        4) Divisió
        5) Canvi de valors
        6) Sortir
          """)
        b = int(input("Elegeix una opció: "))
        match b:
            case 1:
                suma()
            case 2:
                resta()
            case 3:
                multiplicacio()
            case 4:
                divisio()
            case 5:
                canvidevalors()
            case 6:
                b=-1 
    


#Programa
a = 1 
while a>0:
    a = menu_principal()
    match a:
        case 1:
            openters()   
        case 2:
            opreals()
        case 3:
            a=0 
        case other:
            print("Opció no vàlida torni al menú principal: \n")