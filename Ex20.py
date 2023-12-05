def superposició(l1,l2):
    
    

    for e in l1:
        if e in l2:
            print("Vertader")
        else:
            print("Fals")


l1=["hola", "poma", "pera"]
l2=["macarrons", "poma", "lleó"]

print("Primera llista: {}".format(l1))
print("Segona llista: {}".format(l2))
superposició(l1,l2)