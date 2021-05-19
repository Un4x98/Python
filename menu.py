from tkinter import *
from tkinter import messagebox

# Configuración de la raíz
root = Tk()

def infoAdicional():
    messagebox.showinfo("Programa de Menus","Creado por Unax")
def infoLicencia():
    messagebox.showinfo("Licencia","Licencia valida hasta 2025")
def salirApp():
    valor=messagebox.askyesno("Salir","Desea Salir de la app?")
    if valor==True:
        root.destroy()



print(16*16)
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar",command=salirApp)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Licencia",command=infoLicencia)
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...",command=infoAdicional)

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Finalmente bucle de la aplicación
root.mainloop()