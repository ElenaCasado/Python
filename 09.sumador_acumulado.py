def sumador_acumulado():
    n=input("dime hasta que numero quiere sumar")
    suma=0
    for cont in range(1,n+1,1):
        suma=suma+cont
        #print "suma pacial=",suma
    print "suma=",suma
sumador_acumulado()
