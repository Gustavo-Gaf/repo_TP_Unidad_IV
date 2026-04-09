"""Ejercicio 4  —“Escape Room: La Bóveda”
Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo 
limitados. 

Menú de acciones (se repite mientras el juego siga) 
1. Forzar cerradura (costo: -20 energía, -2 tiempo)
2. Hackear panel (costo: -10 energía, -3 tiempo)
3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 
energía extra)
Condiciones de fin 
• Si cerraduras_abiertas == 3 → VICTORIA 
• Si energia <= 0 o tiempo <= 0 → DERROTA 
• Si se bloquea por alarma → DERROTA (bloqueo)
"""

energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 
energia_maxima = 100
opcion_anterior = None
contador_seleccion = 0
bloqueado = False

print("Bienvenido")

print("Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados. Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.") 

nombre = input("Ingrese el nombre del agente: ")
while not nombre.isalpha():
    print("El nombre solo puede contener letras")
    nombre = input("Ingrese el nombre del agente: ")
print(f"Bienvenido {nombre}, estas por ingresar al escape room!")

while (energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueado == False):
    menu = ("1. Forzar cerradura \n2. Hackear panel \n3.Descansar")
    print(menu)
    seleccion = input("Seleccione una opcion del menu: ")
    while not seleccion.isdigit() or (not int(seleccion) < 1 and int(seleccion) > 3):
        print("La opcion ingresada no es valida")
        seleccion = input("Ingrese una opcion del menu: ")

    seleccion = int(seleccion)
    if seleccion == 1:
        contador_seleccion +=1
        if contador_seleccion >= 3:
            print("“la cerradura se trabó")
            alarma = True
            print("Alarma activada!")
        else:
            opcion_anterior = seleccion
            if alarma == False:
                if energia < 40:
                    riesgo = input("Ingrese un numero del 1 al 3: ")
                    if riesgo == 3:
                        alarma = True
                else:
                    cerraduras_abiertas = cerraduras_abiertas + 1
                    print("Has forzado la cerradura")
        energia = energia - 20
        tiempo = tiempo -2
        print(f"La cantidad de cerraduras abiertas es de {cerraduras_abiertas}")
        print(f"Su energia es {energia} y el tiempo que le queda es {tiempo}")
    elif seleccion == 2:
        opcion_anterior = seleccion
        contador_seleccion = 0
        print("Hackear panel")
        print("costo: -10 energía, -3 tiempo")
        energia = energia -10
        tiempo = tiempo - 3 
        print(f"Su energia es {energia} y el tiempo que le queda es {tiempo}")
        for i in range(4):
            letra = str(input("Ingrese una letra: "))
            while not letra.isalpha() or len(letra) !=1:
                 print("Por favor, solo ingrese una letra")
                 letra = str(input("Ingrese una letra: "))
            codigo_parcial = str(codigo_parcial)
            codigo_parcial = codigo_parcial + letra
            print(codigo_parcial)
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas = cerraduras_abiertas +1
                print("Se ha abierto otra cerradura")
    elif seleccion == 3:
        contador_seleccion = 0
        opcion_anterior = seleccion
        print("Descansar")
        print("costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra")
        energia = energia + 15
        if energia == energia_maxima:
            print("Energia maxima alcanzada")
        elif energia > energia_maxima:
            energia = energia_maxima
            print("Energia maxima alcanzada")
        tiempo = tiempo - 1
        if alarma == True:
            energia = energia - 10
        print(f"Su energia es {energia} y el tiempo que le queda es {tiempo}")
        
    if tiempo < 3 and alarma == True:
        bloqueado = True

if cerraduras_abiertas == 3:
    print("Has ganado el juego")
else:
    print("Game over")

        