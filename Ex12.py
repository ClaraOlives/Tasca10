#Funcions

def menu_principal():
    print("""
        Menú principal:
        1. Calculadora enters
        2. Calculadora reals
        3. Cavis de base
        4. Sortir
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
    x = float(input("Introdueix el primer número real a sumar: "))
    y = float(input("Introdueix el segon número real a sumar: "))    
    print("Resultat: {} + {} = {}".format(x, y, x+y))
def restareals():
    x = float(input("Introdueix el primer número real a restar: "))
    y = float(input("Introdueix el segon número real a restar: "))
    print("Resultat: {} - {} = {}".format(y, x, y-x))

def multiplicacioreals():
    x = float(input("Introdueix el primer número real a multiplicar: "))
    y = float(input("Introdueix el segon número real a multiplicar: "))
    print("Resultat: {} * {} = {}".format(y, x, y*x))

def divisioreals():
    x = float(input("Introdueix el primer número real a dividir: "))
    y = float(input("Introdueix el segon número real a dividir: "))
    print("Resultat: {} / {} = {}".format(y, x, y/x))

def canvidevalorsreals():
    x = float(input("Ingresa el primer nombre real:"))
    y = float(input("Ingresa el segon nombre real:"))


#funcions de canvi de base
def dectobin(numero):
    #Prec: numero sigui enter
    #Post: escriu el valor de l'enter  en binari
    return bin(numero)
def dectooct(numero):
    return oct(numero)
def dectohex(numero):
    return hex(numero)

def bintooct(numero):
    a=int(numero,2)
    return dectooct(a)
def bintodec(numero):
    a=int(numero,2)
    return (a)
def bintohex(numero):
    a=int(numero,2)
    return dectohex(a)

def octtobin(numero):
    a=int(numero,8)
    return dectobin(a)
def octtodec(numero):
    a=int(numero,8)
    return a
def octtohex(numero):
    a=int(numero,8)
    return dectohex(a)

def hextonum(hex):
    #Aquesta funcio passa qualsevol hexadecimal a un numero
    #Prec: hex és una cadena de caràcters
    #Post: retorna un enter entre o i 15
    pnum= {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
    }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)

def hextodec2(hex):
    #Prec: hex és una cadena de caràcters en codificació hexadecimal
    #Post: retorna un número decimal
    hex= hex.lower()
    hex=hex[::-1]
    decimal= 0
    posicio = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * valor
        decimal += pnum
        posicio += 1
    return decimal
def hexotobin(numero):
    #Prec: numero és una cadena de caràcters codificats en hexadecimal 
    #Post:  retorna el número binari
    a=int(numero,16)
    return dectobin(a)
def hexotooct(numero):
    #Prec: numero és una cadena de caràcters codificats en hexadecimal 
    #Post: retorna el número en octal
    a=int(numero,16)
    return dectooct(a)
def hexotodec(numero):
    #Prec: numero és una cadena de caràcters codificats en hexadecimal 
    #Post: retorna el número en decimal
    a=(hextodec2(numero))
    return a




def canvisdebase():
    d=1
    while d>0:
        print("""
    Opcions:
              
        1) Donat un binari ho passem a tota la resta
        2) Donat un octal el passem a tota la resta
        3) Donat un decimal ho passem a tota la resta
        4) Donat un hexadecimal ho passem a tota la resta
        5) Sortir 
          """)
        d = int(input("Elegeix una opció: "))
        match d:
            case 1:
                b = input("Introdueixi un número binari: ")
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El número binari {} és: \n oct -> {} \n dec -> {} \n hex -> {}" .format(b,o,d,h))
            case 2:
                o = input("Introdueixi un número octal: ")
                b = octtobin(o)
                d = octtodec(o)
                h = octtohex(o)
                print("El número octal {} és: \n bin -> {} \n dec -> {} \n hex -> {}" .format(o,b,d,h))
            case 3: 
                d = int(input("Introdueixi un número decimal: "))
                b = dectobin(d)
                o = dectooct(d)
                h = dectohex(d)
                print("El número decimal {} és: \n bin -> {} \n oct -> {} \n hex -> {}" .format(d,b,o,h))
            case 4:
                h = input("Introdueixi un número hexadecimal: ")
                o = hexotooct(h)
                d = hexotodec(h)
                b = hexotobin(h)
                print("El número hexadecimal {} és: \n oct -> {} \n dec -> {} \n bin -> {}" .format(h,o,d,b))
            case 5:  
                print("Adeu, tornaràs al menú principal \n\n")
                d=-1

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
            canvisdebase()
        case 4:
            a=-1 
        case other:
            print("Opció no vàlida torni al menú principal: \n")