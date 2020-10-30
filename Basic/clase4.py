#clase numerp 4 entrada y salida de datos basico

nombre = input("Hola cual es tu nombres ")
edad = int(input("Que edad tienes? "))
promedio = float(input("cual es tu promedio? "))
respuesta = input("eres del grupo 2? (si/no) ") == "si"


print("Your name is ", nombre)
print("your age is ", edad)
print("Your average ", promedio)
print("You are in group 2", respuesta)