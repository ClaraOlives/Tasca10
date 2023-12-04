
def gran(x,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        print("Són iguals")

        

x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))
z = gran(x,y)
if not y==x:
    print("El major de {} i {} és {}".format(x,y,z))


