def sumador_digitos():
    numero=input("Dime un numero de dos digitos:")
    decenas=numero/10
    unidades=numero - 10*decenas #n%10#
    print "La suma de",numero,"vale",decenas+unidades
sumador_digitos()



def sumador_cifras():
    suma=0
    numero=input("Dime un numero: ")
    while numero>10:
        suma=suma+numero%10
        numero=numero/10
    print "La suma de los digitos es ",suma+numero
sumador_cifras()



#programa numero de x cifras, que cuente cuales de esas cifras son pares

def cuales_cifraspares():
    suma=0
    numero= input("Dime un numero: ")
    while numero>1:
        aux=numero%10
        if aux%2==0:
            suma=suma+1
        numero=numero/10
    print "Hay",suma,"numeros pares"
cuales_cifraspares()



    
