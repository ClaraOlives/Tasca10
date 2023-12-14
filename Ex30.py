#Cream una funcio que
def mostrar_majors_que(t,numero_elegit):
	print("Tots els números majors de {} són: ".format(numero_elegit))
	for e in t:
            if e>numero_elegit:
                print("{} ".format(e))
       	 
def llegir_tupla():
     #cream una llista buida
	tupla = []
	i=0
	print("Introdueixi tots els números que vulguis. Per aturar posi -1: ")
    #Deim que mentres la variable i sigui major a -1 afegueixi els elements a la llista tupla
	while i>-1:
            tupla.append(input("Introdueixi un número: "))
            if tupla[i]=="-1":
                tupla.remove("-1")
            i=-2
            i +=1
            return tupla

#Programa principal
#Feim que ens demani que fiquem un nombre
i = input("Introdueixi el número que voleu comparar: ")
#li donam a la variable el valor de la funcio
x = llegir_tupla()
#Feim que aquesta variable converteixi la llista x en tupla
a = tuple(x)
mostrar_majors_que(a, i)