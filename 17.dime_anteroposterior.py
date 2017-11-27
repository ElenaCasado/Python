def dime_ant_post():
    numero= input("Dime un numero:")
    print "numeros anteriores ",
    for cont in range(numero-3,numero,1):
        print cont,
    print
    print "numeros posteriores ",
    for cont in range(numero+1,numero+4,1):
        print cont,
dime_ant_post()
