def comptar_vocals(a):
    b = ['a', 'e', 'i', 'o', 'u', 'altres']
    vocals = [0,0,0,0,0,0]

    for i,e in enumerate(a):
        #Posibles formes de les vocals
        if e=='a' or e=='A' or e=='á' or e=='à' or e=='À' or e=='Á':
            #Indicam a la posició a la que li sumam 1
            vocals[0]+=1
        #Posibles formes de les vocals
        if e=='e' or e=='E' or e=='é' or e=='è' or e=='È' or e=='É':
            #Indicam a la posició a la que li sumam 1
            vocals[1]+=1
        #Posibles formes de les vocals
        if e=='i' or e=='I' or e=='í' or e=='ì' or e=='Ì' or e=='Í':
            #Indicam a la posició a la que li sumam 1
            vocals[2]+=1
        #Posibles formes de les vocals
        if e=='o' or e=='O' or e=='ó' or e=='ò' or e=='Ò' or e=='Ó':
            #Indicam a la posició a la que li sumam 1
            vocals[3]+=1
        #Posibles formes de les vocals
        if e=='u' or e=='U' or e=='ú' or e=='ù' or e=='Ù' or e=='Ú':
            #Indicam a la posició a la que li sumam 1
            vocals[4]+=1
        #Sinos altre
        else:
            vocals[5]+=1
        
    for i,e in enumerate(vocals):
        print("La vocal {} apareix {} vegades.".format(b[i], vocals[i]))






a = input("Introdueix una paraula o cadena de caràcters: ")
comptar_vocals(a)


