#FUNCIONES ARRIBA Y CUERPO PRINCIPAL ABAJO

#CUERPO PRINCIPAL
def sumar(n1,n2):
    respuesta=n1+n2
    return respuesta
def restar(n1,n2):
    respuesta=n1-n2
    return respuesta
def multiplicar(n1,n2):
    respuesta=n1*n2
    return respuesta
def dividir(n1,n2):
    respuesta=n1/n2
    return respuesta
    
def menu_operacion():
    seguir="si"
    n1=input("Dime un numero: ")
    n2=input("Dime otro numero: ")
    while (seguir=="si"): #variable interruptora
        print "Que deseas hacer con los numeros: "
        print"1.Sumarlos"
        print"2.Restarlos"
        print"3.Multiplicarlos"
        print"4.Dividirlos"
        respuesta=input()
        if (respuesta==1):
            print"El resultado es; ",sumar(n1,n2)
        if (respuesta==2):
            print "El resultado es; ",restar(n1,n2)
        if (respuesta==3):
            print"El resultado es; ",multiplicar(n1,n2)
        if (respuesta==4):
            print"El resultado es; ",dividir(n1,n2)
        seguir=raw_input("quieres seguir: ")
                   
menu_operacion()
