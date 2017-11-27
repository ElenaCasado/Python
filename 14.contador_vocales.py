def contador_vocales():
    palabra= raw_input("Dime algo:")
    suma=0
    A=0
    E=0
    I=0
    O=0
    U=0
    for cont in range(0,len(palabra),1):
        if palabra[cont]=='A' or palabra[cont]=='a':
            suma=suma+1
            A=A+1
        if palabra[cont]=='E' or palabra[cont]=='e':
            suma=suma+1
            E=E+1
        if palabra[cont]=='I' or palabra[cont]=='i':
            suma=suma+1
            I=I+1
        if palabra[cont]=='O' or palabra[cont]=='o':
            suma=suma+1
            O=O+1
        if palabra[cont]=='U' or palabra[cont]=='u':
            suma=suma+1
            U=U+1
    print"En la palabra",palabra,"hay",suma,"vocales","A:",A,"E:",E,"I:",I,"O:",O,"U:",U

contador_vocales()



