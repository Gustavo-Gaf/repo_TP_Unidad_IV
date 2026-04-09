#6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
#kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
#• Menor que 150 kWh: “Consumo bajo”.
#• Entre 150 y 300 kWh (inclusive): “Consumo medio”.
#• Mayor que 300 kWh: “Consumo alto”

kwh = int(input("Ingrese el consumo mensual de energía electrica en kilovatios (kWh): "))

if kwh < 150:
    print("Consumo bajo") 
elif kwh <= 300:
    print("Consumo medio")
else :
    print("Consumo alto")
    

if kwh > 500:
    print("Considere medidas de ahorro energético")