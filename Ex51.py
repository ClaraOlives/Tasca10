#Definir una funció index_paraula() on donada una llista ordenada de paraules,
# ens retorni l’índex on es troba una paraula determinada o -1 en cas que no hi sigui.

def llegir_llista_paraules():
    b=[]
    a="a"
    while a!=".":
        a=input("Introdueixi la següent paraula: ")
        if a!=".":
            b.append(a) and b.sort()
    return b



def index_paraula(llista,paraula):
    return [i for i,e in enumerate(llista) if paraula == e]



#pprincipal
a = llegir_llista_paraules()
p = input("Introdueix la paraula a cercar el seu índex: ")
b = index_paraula(a,p)
if len(b)==0:
    print("Dins la llista {} no hi ha l'element {}".format(a,p))
else:
    print("Dins la llista {} la paraula {} apareix {} vegades en les següents posicions {}".format(a,p, len(b),b))
