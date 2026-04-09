"""Hay 2 días de atención: Lunes y Martes. 
Cada día tiene cupos fijos: 
• Lunes: 4 turnos 
• Martes: 3 turnos 
Reglas 
1. Pedir nombre del operador (solo letras). 
2. Menú repetitivo hasta salir: 
1. Reservar turno 
2. Cancelar turno (por nombre) 
3. Ver agenda del día 
4. Ver resumen general 
5. Cerrar sistema  """

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
contadorLunes = 0
contadorMartes = 0
cancelacionLunes = 0
cancelacionMartes = 0

operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    print("Por favor, ingrese un nombre valido, solo letras")
    operador = input("Vuelva a ingresar el nombre del operador: ")

menu = ("\n1. Reservar turno \n" "2. Cancelar turno (por nombre) \n" "3. Ver agenda del día \n" "4. Ver resumen general\n" "5. Cerrar sistema\n")
#print(menu)\
while True:
    print(menu)
    seleccion = input("Ingrese la opcion deseada del menu: ")
    while not seleccion.isdigit() or "1" > seleccion or "5"< seleccion :
        print ("La seleccion ingresada no corresponde a una opcion")
        seleccion = input("Por favor, ingrese una opcion valida: ")
    if seleccion == "1":
        print("Reserve su turno")
        menureserva = ("1 = Lunes\n" "2 = Martes")
        print(menureserva)
        seleccionreserva = input("Por favor, elija el dia que desee reservar: ") 
        while True:
            while not seleccionreserva.isdigit() or "1" > seleccionreserva or  "2" < seleccionreserva :
                print("Ingrese una opcion valida")
                seleccionreserva = input("Por favor, ingrese una opcion: ")
            if seleccionreserva == "1":
                print("Usted ha seleccionado el dia lunes")
                nombrepaciente= input("Ingrese su nombre: ")
                while not nombrepaciente.isalpha():
                    print("Solo use letras")
                    nombrepaciente = input("Vuelva a ingresar su nombre: ")
                if nombrepaciente == lunes1  or nombrepaciente == lunes2 or nombrepaciente ==  lunes3 or nombrepaciente == lunes4:
                    print("Usted ya se encuentra registrado")
                    break  
                elif lunes1 == "": 
                    lunes1 = nombrepaciente
                    print(f"Señor/a {nombrepaciente} usted ha reservado el turno 1 del dia Lunes")
                    contadorLunes = contadorLunes + 1
                    break
                elif lunes2 == "":
                    lunes2 = nombrepaciente
                    print(f"Señor/a {nombrepaciente} usted ha reservado el turno 2 del dia Lunes")
                    contadorLunes = contadorLunes + 1
                    break
                elif lunes3 == "":
                    lunes3 = nombrepaciente
                    print(f"Señor/a {nombrepaciente} usted ha reservado el turno 3 del dia Lunes")
                    contadorLunes = contadorLunes + 1
                    break
                elif lunes4 == "":
                    lunes4 = nombrepaciente
                    print(f"Señor/a {nombrepaciente} usted ha reservado el turno 4 del dia Lunes")
                    contadorLunes = contadorLunes + 1
                    break
                else:
                    print("Todos los turnos se encuentran ocupados")
                    break
            elif seleccionreserva == "2":
                print("Usted ha seleccionado el dia martes")
                nombrepaciente = input("Ingrese su nombre: ")
                while not nombrepaciente.isalpha():
                    print("Solo use letras")
                    nombrepaciente = input("Vuelva a ingresar su nombre: ")
                if nombrepaciente == martes1  or nombrepaciente == martes2 or nombrepaciente ==  martes3:
                    print("Usted ya se encuentra registrado")
                    break  
                if martes1 == "": 
                    martes1 = nombrepaciente
                    print(f"Señor/a {nombrepaciente} usted ha reservado el turno 1 del dia Martes")
                    contadorMartes = contadorMartes + 1
                    break
                elif martes2 == "":
                    martes2 = nombrepaciente
                    print(f"Señor/a {nombrepaciente} usted ha reservado el turno 2 del dia Martes")
                    contadorMartes = contadorMartes + 1
                    break
                elif martes3 =="":
                    martes3 = nombrepaciente
                    print(f"Señor/a {nombrepaciente} usted ha reservado el turno 3 del dia Martes")
                    contadorMartes = contadorMartes + 1
                    break
                else:
                    print("Todos los turnos se encuentran ocupados")
                    break      
    elif seleccion == "2":
        print("Cancele su turno")
        menureserva = ("1 = Lunes\n" "2 = Martes")
        print(menureserva)
        seleccionreserva = input("Por favor, elija el dia que desee cancelar: ")
        while True:
            while not seleccionreserva.isdigit() or "1" > seleccionreserva or  "2" < seleccionreserva :
                print("Ingrese una opcion valida")
                seleccionreserva = input("Por favor, ingrese una opcion: ")
            if seleccionreserva == "1":
                print("Usted ha seleccionado el dia lunes")
                nombrepaciente= input("Ingrese su nombre: ")
                while not nombrepaciente.isalpha():
                    print("Solo use letras")
                    nombrepaciente = input("Vuelva a ingresar su nombre: ")
                if nombrepaciente != lunes1  and nombrepaciente != lunes2 and nombrepaciente !=  lunes3 and nombrepaciente != lunes4:
                    print("Usted no se encuentra registrado")
                    break  
                elif lunes1 == nombrepaciente: 
                    lunes1 = ""
                    print(f"Señor/a {nombrepaciente} usted ha cancelado el turno 1 del dia Lunes")
                    cancelacionLunes = cancelacionLunes + 1
                    break
                elif lunes2 == nombrepaciente:
                    lunes2 = ""
                    print(f"Señor/a {nombrepaciente} usted ha cancelado el turno 2 del dia Lunes")
                    cancelacionLunes = cancelacionLunes + 1
                    break
                elif lunes3 == nombrepaciente:
                    lunes3 = ""
                    print(f"Señor/a {nombrepaciente} usted ha cancelado el turno 3 del dia Lunes")
                    cancelacionLunes = cancelacionLunes + 1
                    break
                elif lunes4 == nombrepaciente:
                    lunes4 = ""
                    print(f"Señor/a {nombrepaciente} usted ha cancelado el turno 4 del dia Lunes")
                    cancelacionLunes = cancelacionLunes + 1
                    break
            if seleccionreserva == "2":
                print("Usted ha seleccionado el dia martes")
                nombrepaciente= input("Ingrese su nombre: ")
                while not nombrepaciente.isalpha():
                    print("Solo use letras")
                    nombrepaciente = input("Vuelva a ingresar su nombre: ")
                if nombrepaciente != martes1  and nombrepaciente != martes2 and nombrepaciente !=  martes3:
                    print("Usted no se encuentra registrado")
                    break  
                elif martes1 == nombrepaciente: 
                    martes1 = ""
                    print(f"Señor/a {nombrepaciente} usted ha cancelado el turno 1 del dia Martes")
                    cancelacionMartes = cancelacionMartes + 1
                    break
                elif martes2 == nombrepaciente:
                    martes2 = ""
                    print(f"Señor/a {nombrepaciente} usted ha cancelado el turno 2 del dia Martes")
                    cancelacionMartes = cancelacionMartes + 1
                    break
                elif martes3 == nombrepaciente:
                    martes3 = ""
                    print(f"Señor/a {nombrepaciente} usted ha cancelado el turno 3 del dia Martes")
                    cancelacionMartes = cancelacionMartes + 1
                    break

    elif seleccion == "3":
        print("Ver agenda del día")
        menureserva = ("1 = Lunes\n" "2 = Martes")
        print(menureserva)
        seleccionreserva = input("Por favor, elija el dia que desee ver: ")
        if seleccionreserva == "1":
            print(f"Primer turno {lunes1}")
            print(f"Segundo turno {lunes2}")
            print(f"Tercer turno {lunes3}")
            print(f"Cuarto turno {lunes4}")
        else:
            print(f"Primer turno {martes1}")
            print(f"Segundo turno {martes2}")
            print(f"Tercer turno {martes3}")
    elif seleccion == "4":
        print("Resumen general ")
        print(f"Para el dia Lunes se han realizado {contadorLunes} altas de turnos y {cancelacionLunes} bajas ")
        print(f"Para el dia Martes se han realizado {contadorMartes} altas de turnos y {cancelacionMartes} bajas ")
    elif seleccion == "5":
        print("Cerrar sistema")
        exit()
                
        