#Hacer un programa que segun la hora que sea, te diga buenos dias, buenas tardes, o buenas noches
#de 6-14, son buenos dias; de 14-20 son buenas noches y de 20-6 son buenas noches
def saludador():
    hora=input("Dime que hora es:")
    if (hora>=6 and hora<14):
        print "Buenos dias"
    if (hora>=14 and hora<20):
        print "Buenas tardes"
    if ((hora>=20 and hora<=24) or (hora>=0 and hora<6)) :
        print "Buenas noches"
saludador()
        
        
