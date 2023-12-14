#Indica que vol col·locar la informació en forma de taula
from datetime import date
from datetime import datetime

def GetNames(aactual):
	a=[]
	
	print("Introdueixi els nom i la data de naixament de una persona:")
	for i in range(0,4):
            v=[0,0,0]
			#Demanem que introdueixi el nom de la persona
            v[0]=input("Escriu el nom de la {}a persona: ".format(i+1))
			#Demanem que introdueixi l'any en el que va nèixer la persona
            v[1]=input("Escriu l'any de naixament de {}: ".format(v[0]))
            v[2]=int(aactual) - int(v[1])
			#Li deim que ho afegeixi a la llista v
            a.append(v)
            return a

#Programa Principal
#Indica la data actual
avui	= date.today()
aactual = avui.year
x = GetNames(aactual)
print("L'any actual és: ", aactual)
#Substitueix les tres posicions(títols) per els enunciats corresponents
print ("{:<20} {:<20} {:<20}".format('Nom','Data naixament','Anys que farà aquest any'))
for e in x:
	#Indica que l'element de la llista v de la posició 0 s'ha de col·locar davall Nom, i així posant els altres al seu lloc
	print("{:<20} {:<20} {:<20}".format(e[0], e[1], e[2]))
