from tkinter import *
from tkinter import messagebox
root=Tk()

def infoAdicional():
    messagebox.showinfo("Programa Menus","Lo que sea")

barramenu=Menu(root)
root.config(menu="barramenu",width="300",height="300")

archivoMenu=Menu(barramenu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")

archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


archivoEdicion=Menu(barramenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barramenu,tearoff=0)


root.mainloop() 
