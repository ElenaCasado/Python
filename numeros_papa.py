def numeros():
    cociente=0
    resto=0
    total=0
    n1=input("Dime un numero; ")
    while(n1>10):
        cociente=n1/10
        resto=n1%10
        total=total+resto
        n1=cociente
    print total+cociente
numeros()
