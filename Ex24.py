def gran_llista(a):
    a.sort()
    return a[::-1]




a = [3,9,3,11,20]
c = gran_llista(a)
print(a)
print("El nombre més gran d'aquesta llista és {}".format(c[0]))
    

