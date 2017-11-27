def ordenar_vectores():
    suma=0
    numero= input("Dime cualquier numero: ")
    L=[]
    while numero>0:
        aux=numero%10
        L.append(aux) # el append; TE METE TODO EL AUX
        numero=numero/10
 #   print L
#    L.sort(reverse=False) #de menor a mayor
#    print L
    L.sort(reverse=True) #de mayor a menor
    print L
ordenar_vectores ()

