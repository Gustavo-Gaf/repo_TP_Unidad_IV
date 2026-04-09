"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal."""

altura = float(input("Ingrese su altura en metros : "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / (altura**2)

print(f"Su Imc es: {imc}")