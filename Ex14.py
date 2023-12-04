def gran_de_tres(x,y,z):
        if x<y<z:
            return z
        elif y<x<z:
            return z
        elif x==y<z:
            return z
        elif x<z<y:
            return y
        elif z<x<y:
            return y
        elif x==z<y:
            return y
        elif x<z==y:
            return y
        elif z<x==y:
            return y
        elif z<y<x:
            return x
        elif y<z<x:
            return x
        elif y<z==x:
            return x
        elif y==z<x:
            return x
        elif y==z==x:
            print("Tots són iguals")
       
            

x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))
z = int(input("Introdueix el tercer nombre: "))
ñ = gran_de_tres(x,y,z)
if not y==z==x:
    print("El major de {}, {} i {} és {}".format(x,y,z,ñ))
        

