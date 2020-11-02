#conversion de colon salvadorenio a dolar

salir = False

   print("1. Convertir de dolar a colon")
   print("2. Cnvertir de colon a dolar")
   print("3. Salir del convertidor")
   print("**Elige una opcion**")

   opcion= input()

while not salir:
if opcion== 1:
    print("Inroduzca la cantidad de dolares")
    dolares = float(input("$ "))

    colon = (dolares * 8.75)
    print("La cantidad de dolares $", dolares, "en colones es ", colon)

elif opcion ==2:
    print("Inroduzca la cantidad de colones")
    colones = float(input("C "))
    dolar = (colones * 0.0017)
    print("La cantidad de colones ", colones , "En dolares es $ ",dolar)
elif opcion == 3:
   salir = True

else:
   print("Introduce un numero entre 1 y 3")
