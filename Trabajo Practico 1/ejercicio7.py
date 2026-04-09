"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""

numero1 = int(input("Ingrese un numero entero distinto de 0: "))
numero2 = int(input("Ingrese un numero entero distinto de 0: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"La suma de los numeros es {suma}")
print(f"La resta de los numeros es {resta}")
print (f"La multiplicacion de los numeros es {multiplicacion}")
print (f"La division de los numeros es {division}")