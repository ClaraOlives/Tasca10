#Definir una funció llista_20_elements() que retorni una llista de 
#20 elements creats aleatòriament entre 1 i 100. Provar amb la funció anterior si s’han generat elements duplicats o no.


from random import random
import random

#funcio que conte una llista buida
def llista_20_elements():
    l = []
    for i in range(20):
        l.append(random.randint(1,100))
    return l



def hi_ha_duplicats(a):
    seen = set()    
    dupes = [x for x in a if x in seen or seen.add(x)]  	 
    if len(dupes)>0:
        print("La llista {} té elements duplicats {}".format(a,dupes))
    else:
        print("La llista {} no té elements duplicats {}".format(a,dupes))
                
#Pprincipal
x = llista_20_elements()
hi_ha_duplicats(x)
