numero = int(input("Dígame cuántas palabras tiene la primera lista: "))

if numero < 1:
    print("Incorrecto")
else:
    primera = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        primera += [palabra]
    print("La primera lista es:", primera)

    for i in range(len(primera)-1, -1, -1):
        if primera[i] in primera[:i]:
            del(primera[i])
    # print("La primera lista sin repeticiones es:", primera)

    numero2 = int(input("Dígame cuántas palabras tiene la segunda lista: "))

    if numero2 < 1:
        print("Incorrecto")
    else:
        segunda = []
        for i in range(numero2):
            print("Dígame la palabra", str(i + 1) + ": ", end="")
            palabra = input()
            segunda += [palabra]
        print("La segunda lista es:", segunda)

        for i in range(len(segunda)-1, -1, -1):
            if segunda[i] in segunda[:i]:
                del(segunda[i])
        # print("La segunda lista sin repeticiones es:", segunda)

        comunes = []
        for i in primera:
            if i in segunda:
                comunes += [i]
        print("Palabras que aparecen en ambas listas:", comunes)

