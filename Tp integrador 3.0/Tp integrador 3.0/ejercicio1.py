"""
Ejercicio 1— “Caja del Kiosco”
Objetivo: Simular una compra con validaciones y cálculo de total.
Requisitos
1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
2. Pedir cantidad de productos a comprar (número entero positivo, validar con
.isdigit() en while).
3. Por cada producto (usar for):
o Pedir precio (entero, validar .isdigit()).
o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
cualquier mayuscula/minuscula).
o Si tiene descuento: aplicar 10% al precio de ese producto.
4. Al final mostrar:
o Total sin descuentos
o Total con descuentos
o Ahorro total
o Promedio por producto (usar float y formatear con :.2f, ejem:
"""

totalcondescuento = 0
totalsindescuento = 0
descuentosinaplicar = 0
ahorro = 0
promedio = 0

nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    print("Por favor, el nombre solo puede contener letras(sin espacios, ni numeros)")
    nombre = input("Por favor, ingrese el nombre nuevamente: ")
    
cantidadproductos = input("Por favor, ingrese la cantidad de productos que desea comprar: ")

while ((not cantidadproductos.isdigit()) or int(cantidadproductos) <= 0):
    print("Por favor, ingrese un numero entero positivo")

    cantidadproductos = (input("Por favor, ingrese una cantidad valida: "))
cantidadproductos = int(cantidadproductos)

for producto in range (1,cantidadproductos + 1):
    precio = input(f"Ingrese el precio del producto {producto}: ")
    while not precio.isdigit() or precio == "0":
        print("Ingrese un numero entero positivo")
        precio = (input("Por favor, ingrese una cantidad valida: "))
    precio = int(precio)

    descuento = input("Si el producto tiene descuento, presione 'S' Sino presione 'N' :")
    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Ingrese un descuento valido")
        descuento = input("Si el producto tiene descuento, presione 'S' Sino presione 'N' :")

    if descuento.lower() == "s":
        preciocondescuento = precio * .90
        descuentosinaplicar += precio
        totalcondescuento += preciocondescuento
        print("El producto tiene descuento")
    else:
        totalsindescuento += precio
        print("El producto no tiene descuento")
       
    promedio = totalcondescuento / cantidadproductos
    ahorro = descuentosinaplicar - totalcondescuento
    total = totalcondescuento + totalsindescuento

print(f"El total de los productos sin descuento es de {totalsindescuento:.2f}")
print(f"El total de los productos con descuento es de {totalcondescuento:.2f}")
print(f"El ahorro total en los productos es de {ahorro:.2f}")
print(f"El promedio por producto es {promedio:.2f}")
print(f"El total de la compra es de {total:.2f}")