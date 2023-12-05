def llegir_llista():
    a = 0
    l = []
    while a!= '.':
        a = input("Introdueix un element: ")
        if a != '.':
            l.append(a)
        else:
            return l  

def paraula_mes_llarga(r):
    max = r[0]
    for e in r:
        if len(e)>len(max):
            max=e
    return max


llista_paraules = llegir_llista()
print("La paraula més gran de la llista {} és {}".format(llista_paraules,paraula_mes_llarga(llista_paraules)))
