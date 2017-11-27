def contador_u():
    palabra=raw_input("Dime cualquier cosa;")
    resultado=""
    for cont in range(0,len(palabra),1):
        if palabra[cont]=='a' or palabra[cont]=='e' or palabra[cont]=='i' or palabra[cont]=='o' or palabra[cont]=='A' or palabra[cont]=='E' or palabra[cont]=='I' or palabra[cont]=='O':
            print'u',
            resultado=resultado+"u"
        else:
            print palabra[cont],
            resultado=resultado+palabra[cont]
    print resultado
contador_u()

