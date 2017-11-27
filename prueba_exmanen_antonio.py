# 1. diferencia entre variable contadora y acumuladora.
La diferencia entre un contador y un acumulador es que mientras
el primero va aumentando de uno en uno, el acumulador va aumentando
en una cantidad variable.
# 2.
    #a.
def hago_algo():
    x=input("Dime un numero ")
    y=0
    for cont in range(0,10,1):
        y=y+cont
    print y



def hago_algo():
    x=input("Dime un numero; ")
    y=0
    for cont in range(0,10,1):
        y=y+cont
        print(y)
hago_algo()


    #b. Añade lo necesario para repetir o salir.

def hago_algo():
    x=input("Dime un numero; ")
    var="si"
    y=0
    while (var="si"):#repetir hasta que var sea distinto de "si"
        for cont in range(0,10,1):
            y=y+cont
            print(y)
        var=raw_input("desea continuar: ")     
hago_algo() 

# 3.Descomposición en productos de factores.
# 4.Lee 3 lados y te dice si forman un triangulo rectangulo.
def triangulo_rectangulo():
    a=input("Dime la hipotenusa; ")
    b=input("Dime otro lado; ")
    c=input("Dime otro lado; ")
    if a**2==b**2+c**2
        print("Es un triangulo rectangulo")
    else:
        print("No es un triangulo rectangulo")
triangulo_rectangulo()

    

