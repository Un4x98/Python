from random import *

def generarNumeroAleatorio(minimo,maximo):
    
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux
 
        return randint(minimo, maximo)
    except TypeError:
        print("Debes escribir numeros")
        return -1
 
numero_buscado = generarNumeroAleatorio(1,100)

encontrado=False
intentos=0


while not encontrado:
    numero_usuario= int(input("Introduce un numero: "))

    if(numero_usuario > numero_buscado):
        print("El numero es menor")
        intentos=intentos+1
    elif(numero_usuario < numero_buscado):
        print("El numero es mayor")
        intentos=intentos+1
    else:
        encontrado=True
        print("Has encontrado el numero, era el ", numero_usuario," en ",intentos," intentos")
