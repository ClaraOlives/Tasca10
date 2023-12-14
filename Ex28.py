

def bintodec (bin):
    return int(bin,2)

#Cream una funcio que contengui una llista i que a cada element de llbin es canvii per enter
def llbintodec(llbin):
    lldec = []
    for e in llbin:
        lldec.append(bintodec(e))
    return lldec

#Cream una llista amb els nombres binaris que volen passar a enters
a = ["1", "11", "1010","1001"]
#Cream una variable que contengui la funcio i li passem la variable a
b = llbintodec(a)
#Deim que a cada posicio i element apliqui la variable b
for i, e in enumerate(b):
    print("El número binari : ", a[i], " es correspon amb el número decimal: ", e)

