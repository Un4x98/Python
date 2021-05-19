from tkinter import *
from tkinter import ttk

def calculate(*args):#metodo para convertir de pies a metros
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
#Nombre del programa
root.title("Conversor de pies a metros")
#Crear y configurar Tamaño del frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Widgets
#configuracion del "textview" de introducir los pies
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
#Metros
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#boton calcular
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)
#label pies
ttk.Label(mainframe, text="Pies").grid(column=3, row=1, sticky=W)
#label es igual a
ttk.Label(mainframe, text="es igual a").grid(column=1, row=2, sticky=E)
#label metros
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()