def clasificador_numeros():
    x=input("Dime un numero:")
    y=input("Dime otro numero:")
    if (x%2 >0 and y%2 >0):
        print "Los dos numeros son impares"
    if (x%2==0 and y%2==0):
        print "Los dos numeros son pares"
    if (x%2 >0 and y%2==0):
        print "El primer numero es impar, el segundo es par"
    if (x%2==0 and y%2 >0):
        print "El primero es numero par, el segundo es impar"
        
clasificador_numeros()

    
    
    
