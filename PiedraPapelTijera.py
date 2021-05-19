from tkinter import *
from random import randint
from tkinter import ttk
root=Tk()
root.title("Piedra Papel Tijera")
root.geometry("500x600")
#Fondo blanco
root.config(bg="white")

piedra= PhotoImage(file='C:/Users/Unax/Desktop/Python/Ejercicios_Simples/imagenes/piedra.png')
papel= PhotoImage(file='C:/Users/Unax/Desktop/Python/Ejercicios_Simples/imagenes/papel.png')
tijera= PhotoImage(file='C:/Users/Unax/Desktop/Python/Ejercicios_Simples/imagenes/tijera.png')

def aleatorio():
    numero_aleatorio= randint(0,2)
    imagen_elegida.config(image=lista_imagenes[numero_aleatorio])

#Añadir las imagenes a una lista
lista_imagenes=[piedra,papel,tijera]

#Elegir numero aleatorio de 0 a 2 
numero_aleatorio= randint(0,2)

imagen_elegida=Label(root,image=lista_imagenes[numero_aleatorio],bd=0)
imagen_elegida.pack(pady=20)

    

#Mi elegido
mi_elegido=ttk.Combobox(root,value=("Piedra","Papel","Tijeras"))
mi_elegido.current(0)
mi_elegido.pack(pady=20)


if mi_elegido.get()=="Piedra":
    valor_elegido=0
elif mi_elegido.get()=="Papel":
    valor_elegido=1
elif mi_elegido.get()=="Tijeras":
    valor_elegido=2

#Boton aleatorio
boton_aleatorio=Button(root,text="Aleatorio!",command=aleatorio)
boton_aleatorio.pack(pady=10)
#Ganador
resultado=Label(root,text="Ha ganado: ",font=("Helvetica","18"))
resultado.pack(pady=50)


root.mainloop()