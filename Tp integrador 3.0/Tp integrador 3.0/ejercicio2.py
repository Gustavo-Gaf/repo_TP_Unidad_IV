""""1. Definir credenciales fijas en el código: 
o usuario correcto: "alumno" 
o clave correcta: "python123" 
2. Permitir máximo 3 intentos para ingresar usuario y clave. 
3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar. 
4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 
1. Ver estado de inscripción (mostrar “Inscripto”) 
2. Cambiar clave (pedir nueva clave y confirmación; deben 
coincidir) 
3. Mostrar mensaje motivacional (1 frase) 
4. Salir 
5. Validación del menú: 
o Debe ser número (.isdigit()) 
o Debe estar entre 1 y 4 """

usuariocorrecto = "alumno"
clavecorrecta = "python123"

for intento in range (0,3):
    usuario = input(f"Intento {intento+1}\nIngresa el usuario: ")
        
    if usuario ==  usuariocorrecto:
        print("El usuario ingresado es correcto.")
        break
    elif usuario != usuariocorrecto:
        print("El usuario no es correcto, vuelva a ingresarlo")
    else:
        print("Cuenta Bloqueada")
        exit()
        
for intento in range(0,3):   
    clave = input(f"Intento {intento+1}\nIngresa la clave: ")
    
    if clave == clavecorrecta:
        print("La clave ingresada es correcta")
        break
    elif clave != clavecorrecta:
        print("La clave ingresada es incorrecta, vuelva a intentar")
    else:
        print("Cuenta Bloqueada")
        exit()
    
print("Acceso concedido")

menu = ("1. Ver estado de inscripcion\n" "2. Cambiar clave\n" "3. Mostrar mensaje\n" "4. Salir")
print(menu)
seleccion = input("Seleccione la opcion deseada: ")
while seleccion != "4":
    while (not seleccion.isdigit() or (int(seleccion) < 1 or int(seleccion) > 4)):
        print("La opcion ingresada no es valida.")
        seleccion = input("Seleccione la opcion deseada: ")
    if seleccion == "1":
        print("Inscripto")
    elif seleccion == "2":
        print("Cambiar clave")
        clavenueva = input("Ingrese su clave actual: ") 
        while True:
            if clavenueva != clavecorrecta:
                print("Clave incorrecta")
                clavenueva = input("Vuelva a ingresar la clave: ")
            elif clavenueva == clavecorrecta:
                clavenueva = input("Ingrese su nueva clave: ")
                while not (len(clavenueva)) > 6:
                    print ("Su clave debe tener mas de 6 digitos")
                    clavenueva = input("Intente con otra clave: ")
                print("Su clave a sido actualizada.")
                clavecorrecta = clavenueva 
                break
    elif seleccion == "3":
        print("La mejor manera de predecir el futuro es crearlo")
    else:
        print("Opcion no encontrada")
    print(menu)
    seleccion = input("Seleccione la opcion deseada: ")

print("Sesion finalizada")