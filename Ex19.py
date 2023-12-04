def es_palidrom(a,b):
    if a==b:
        print("És un palidrom")
    else:
        print("No és un palidrom")





a=input("Introdueix una paraula: ")
b= a[::-1]
es_palidrom(a,b)