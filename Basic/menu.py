
def menu():
    print ("Selecciona una opción")
    print ("\t1 - conversion de dolar a colon")
    print ("\t2 - Conversion de colon a dolar")
    print ("\t9 - salir \n")
while True:
    #Mostramos el menu
    menu()

    #solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu =="1":
        print("Inroduzca la cantidad de dolares")
        dolares = float(input("$ "))

        colon = (dolares * 8.75)
        print("La cantidad de dolares $", dolares, "en colones es ", colon)
        input("\npulsa una tecla para continuar")
    elif opcionMenu =="2":
        print("Inroduzca la cantidad de colones")
        colones = float(input("C "))
        dolar = (colones * 0.11)
        print("La cantidad de colones ", colones, "En dolares es $ ", dolar)
        input("\npulsa una tecla para continuar")
    elif opcionMenu =="9":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")