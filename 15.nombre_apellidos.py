def nombre_apellidos():
    nombre= raw_input("Dime tu nombre:")
    apellido1= raw_input("Dime tu primer apellido:")
    apellido2= raw_input("Dime tu segundo apellido:")
    print "Tu nombre completo es;",nombre,apellido1,apellido2
nombre_apellidos()
                      
    
#otra forma de hacerlo es;#
def nombre_apellidos():
    nombre= raw_input("Dime tu nombre:")
    apellido1= raw_input("Dime tu primer apellido:")
    apellido2= raw_input("Dime tu segundo apellido:")
    nombre_total=nombre+" "+apellido1+ " "+apellido2
    print"Te llamas "+nombre_total
nombre_apellidos()
                    
