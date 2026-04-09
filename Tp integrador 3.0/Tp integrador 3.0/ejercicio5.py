"""
Ejercicio 5  — “Escape Room:"La Arena del 
Gladiador"  
1. Descripción del Escenario  
Vas a desarrollar un simulador de batalla por turnos en Python.
El Ciclo de Combate  
El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 
puntos de vida.  
Turno del Jugador:  
Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 
opciones:  
1. Ataque Pesado  
2. Ráfaga Veloz (Requiere uso de for)  
3. Curar  
Turno del Enemigo:  
Justo después de tu acción, el enemigo ataca automáticamente.  
Paso 4: Fin del Juego  
Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:  
• • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."  
• • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate." 
"""

VidaGladiador = 100
VidaEnemigo = 100  
PocionesVida = 3
AtaquePesado = 15 
DañoEnemigo = 12  
TurnoGladiador = True
GolpeCritico = AtaquePesado * 1.5

print("--- BIENVENIDO A LA ARENA ---")
NombreGladiador = str(input("Nombre del Gladiador: "))
while not NombreGladiador.isalpha():
    print(f"Nombre del Gladiador: {NombreGladiador}")
    print("Error: Solo se permiten letras")
    NombreGladiador = str(input("Nombre del Gladiador: "))
print("=== INICIO DEL COMBATE ===  ")
while VidaGladiador > 0 and VidaEnemigo >0:
    if TurnoGladiador == True:
        print(f"{NombreGladiador} (HP: {VidaGladiador}) vs Enemigo (HP: {VidaEnemigo}) | Pociones: {PocionesVida}")
        menu = ("1.Ataque pesado\n2.Rafaga Veloz\n3.Curar")
        print("Elige acción: ")
        print(menu)
        seleccion = input("Ingrese una opcion del menu: ")
        while not seleccion.isdigit() or int(seleccion) <1 or int(seleccion)>3:
            print("La opcion elegida no es correcta")
            seleccion = input("Ingrese un numero valido: ")
        seleccion = int(seleccion)
        if seleccion ==1:
            print("Opcion 1")
            if VidaEnemigo < 20:
                VidaEnemigo = VidaEnemigo - GolpeCritico
                print(f"¡Atacaste al enemigo por {GolpeCritico} puntos de daño!")
            else:
                VidaEnemigo = VidaEnemigo - AtaquePesado
                print(f"¡Atacaste al enemigo por {AtaquePesado}puntos de daño!")
        elif seleccion ==2:
            for i in range(3):
                VidaEnemigo = VidaEnemigo - 5
                print("Golpe conectado por 5 de daño")
                TurnoGladiador == False
        elif seleccion ==3:
            if PocionesVida >0:
                VidaGladiador = VidaGladiador + 30
                PocionesVida = PocionesVida - 1
                print("Has recuperado 30 puntos de HP")
            elif PocionesVida <=0:
                print( "¡No quedan pociones!")
                TurnoGladiador == False
        TurnoGladiador = False
    else:
        VidaGladiador = VidaGladiador - DañoEnemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
        TurnoGladiador = True
if VidaGladiador >0:
    print(f"¡VICTORIA! {NombreGladiador} ha ganado la batalla")
else:
    print(f"DERROTA. Has caído en combate.")