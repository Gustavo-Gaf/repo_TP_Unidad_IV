#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 

nombre = input("Ingrese un nombre")
menu = ("1. Mayusculas\n", "2. Minusculas\n", "3. Capital")
seleccion = int(input("Ingrese la seleccion deseada: "))


if seleccion == 1:
    mayuscula = nombre.upper()
    print(mayuscula)
    
elif seleccion == 2:
    minuscula = nombre.lower()
    print(minuscula)

elif seleccion == 3:
    capital = nombre.title()
    print(capital)

else:
    print("El numero ingresado no corresponde a un numero del menu")
