import math


def ecuacion_2grado():
    a=input("Dame un numero que sea x**2; ")
    b=input("Dame otro numero que sea y; ")
    c=input("Dame otro numero; ")
    contenido_raiz =b**2 - 4*a*c
    if (contenido_raiz<0):
        print "Es de tipo c. NO CORTA CON EL EJE"
    else:
        if(contenido_raiz==0)
            print "Es de tipo b. Corta en el punto ",-b/2*a
        else:
            print "Es de tipo a. Corta en los puntos ",-b+math.sqrt(contenido_raiz)/2*a,", ",-b-math.sqrt(contenido_raiz)/2*a


ecuacion_2grado()
