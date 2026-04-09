"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro"""

import math
radio = int(input("Ingrese el valor del radio: "))
area = (math.pi) * radio **2
perimetro = 2 * (math.pi) * radio

print (f"El area del circulo es {area} y su perimetro es {perimetro}")