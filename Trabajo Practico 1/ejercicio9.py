"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit."""


celsius = float(input("Ingrese la temperatura en grados celcius: "))
fahrenheit = ((9/5)* celsius) + 32

print(f"La temperatura en grados fahrenheit es: {fahrenheit}")