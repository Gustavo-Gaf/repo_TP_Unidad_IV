#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla. 

texto = input("Ingrese una frase o una palabra: ")
vocal = ("a", "A" ,"e", "E","i","I","o","O","u","U")
if texto.endswith (vocal):
    texto = texto + ("!")
    print(texto)
else:
    print(texto)