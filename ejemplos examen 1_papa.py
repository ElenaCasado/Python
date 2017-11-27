#programa cadena de numeros y me enseñe las pares; cocodrilo;      o o r l
def numero(n1):
    resultado=n1*10
    return resultado
    
def multiplicar(n2,n3):
    cadena=""
    resultado=n2*n3
    if(resultado%2==0):
        cadena="es par"
    else:
        cadena="es impar"
    return cadena
    


def cadena():
    a=0
    o=0
    suma=0
    resultado=""
    palabra=raw_input("Dime una palabra; ")
    for cont in range(0,len(palabra),1):
        if (cont%2>0):
            print palabra[cont],
        if(palabra[cont]=="a"):
            a=a+1
            suma=suma+1
        if(palabra[cont]=="o"):
            o=o+1
            suma=suma+1
    print
    print "en la palabra",palabra,"hay",a,"a ",o,"o "
    print "en la palabra hay; ",suma,"vocales"
    while (suma>0):
        suma=suma-1
        resultado=resultado+"x"
    print resultado
    print numero(a)
    print multiplicar(a,o)
    
            
        
cadena()

