#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#magnitud = int(input("Ingrese la Magnitud del terremoto: "))

magnitud = int(input("Ingrese el valor del terremoto, segun la escala de Richter: "))
while True:
    if magnitud < 3 :
        print("'Muy leve' (imperceptible)")
        magnitud = int(input("Ingrese el valor del terremoto, segun la escala de Richter: "))
    elif magnitud >=3 and magnitud <4:
     print("'Leve' (ligeramente perceptible)")
     magnitud = int(input("Ingrese el valor del terremoto, segun la escala de Richter: "))
    elif magnitud >=4 and magnitud <5:
        print("'Moderado' (sentido por personas, pero generalmente no causa daños")
        magnitud = int(input("Ingrese el valor del terremoto, segun la escala de Richter: "))
    elif magnitud >=5 and magnitud <6:
        print( "'Fuerte' (puede causar daños en estructuras débiles)")
        magnitud = int(input("Ingrese el valor del terremoto, segun la escala de Richter: "))
    elif magnitud >=6 and magnitud <7:
        print( "'Muy Fuerte' (puede causar daños significativos)")
        magnitud = int(input("Ingrese el valor del terremoto, segun la escala de Richter: "))
    elif magnitud >=7:
        print("'Extremo' (puede causar graves daños a gran escala)")
        magnitud = int(input("Ingrese el valor del terremoto, segun la escala de Richter: "))
    else:
        print("El numero ingresado no es válido")
        magnitud = int(input("Ingrese el valor del terremoto, segun la escala de Richter: "))