#un numero te multiple el primero por el segundo, 56=5*6   564=5*6*4
def longitud(a):
    respuesta=0
    while(a>0):
        a=a/10
        respuesta=respuesta+1
    return respuesta
def multiplicador():
    n=1
    a=input("Dime un numero; ")
    for cont in range(0,longitud(a),1):
        resto=a%10
        n=n*resto
        print n
        a=a/10
    print "El resultado es; ",n
    
multiplicador()
    
def multiplicador2():
    n=1
    a=input("Dime un numero; ")
    while (a>0):
        resto=a%10
        n=n*resto
        print n
        a=a/10
    print "El resultado es; ",n
multiplicador2()
