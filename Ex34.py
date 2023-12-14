#cream una funcio que si la variable any es divideix per 4 i el residu es zero, o per 400 i el residu es 0 o per
#100 i el residu es major a 0 escrigui ue es de traspas sinos que no ho es
def es_de_traspas(any):
    if any%4==0 and any%400==0 or any%100>0:
        print("L'any {} és de traspàs".format(any))
    else:
        print("L'any {} no és de traspàs".format(any))



a = int(input("Introdueix un any (aaaa): "))   
es_de_traspas(a)