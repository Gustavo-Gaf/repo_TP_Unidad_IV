#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año :


hemisferio = input("Indique en que hermisferio se encuentra: (N/S): ").upper()

while hemisferio not in  ("N" ,"S"):
    print("El ingreso no es válido")
    hemisferio = input("Indique en que hermisferio se encuentra: (N/S): ").upper()
if hemisferio == "N" :
    print("Usted esta en el hemisferio norte")
elif hemisferio == "S" :
    print("Usted esta en el hermisferio sur")
    
mes = int(input("Ingrese el mes en que se encuentra: "))

while mes <1 or mes >12:
   print("Ingrese un mes válido") 
   mes = int(input("Ingrese el mes en que se encuentra: "))


dia = int(input("Ingrese el dia en que se encuentra: "))

while dia <1 or dia >31:
    print("Ingrese un día valido")
    dia = int(input("Ingrese el dia en que se encuentra: "))
    
def fecha(m, d):
    return m * 100 + d
f = fecha(mes, dia)

if hemisferio == "N":
    if 1221<= f or f <= 320:
        estacion = "Invierno"
    elif 321 <= f <= 620:
        estacion = "Primavera"
    elif 621 <= f <= 920:
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:
    if 1221<= f or f <= 320:
        estacion = "Verano"
    elif 321 <= f <= 620:
        estacion = "Otoño"
    elif 621 <= f <= 920:
        estacion = "Invierno"
    else:
        estacion = "Primavera"
        
print(f"La estacion correspondiente es {estacion}")  