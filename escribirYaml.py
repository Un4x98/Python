import yaml
from tkinter import *
from tkinter import messagebox
import os
from infi.systray import SysTrayIcon


root=Tk()
root.title("Escribir YAML")
miFrame=Frame(root) 
miFrame.pack()


def abrir(systray):
    pass    

menu_options = (("Abrir", None, abrir),)
systray = SysTrayIcon("formulario.ico", "Escribir en YAML",menu_options)
systray.start()

desktop = os.path.expanduser("~/Desktop/usuarios.yaml")
  

nombreEscrito=StringVar()
apellidoEscrito=StringVar()
edadEscrito=StringVar()

def cerrarApp():
    root.destroy()

def escribirYaml():
    nombre=nombreEscrito.get()
    apellido=apellidoEscrito.get()
    edad=edadEscrito.get()
    #Escribir en el archivo  
    try:
        int(edad)
        if len(nombre)==0 or len(apellido)==0 or len(edad)==0:
            messagebox.showerror("Campos vacios","Rellena todos los campos")

        else:
            data=[{'Nombre' : nombre, 'Apellido' : apellido, 'Edad' :int(edad) }] #formato YAML
            with open(desktop, 'w') as outfile: #w=write
                yaml.dump(data, outfile, default_flow_style=True,sort_keys=False)#default_flow_style=True todo en una linea, false=cada dato en una linea distinta.sort_keys false, sino ordena los datos alfabeticamente
                messagebox.showinfo("Insertado","Datos insertados correctamente")
                editar=messagebox.askyesno(title="Editar?", message="Quieres editar algun dato?")
            if editar:
                outfile.close()                  
            else:
                messagebox.showinfo("Cerrar","Se cerrara el programa")
                outfile.close()
                root.destroy()
           

    except ValueError:        
        messagebox.showerror("Edad no valida","No has introducido una edad valida")
        


    

if  os.path.exists(desktop):
        
        with open(desktop, 'r') as f: #r=read
            
            doc = yaml.load(f,Loader=yaml.SafeLoader)
        
        nombreRecogido=doc[0]['Nombre']
        apellidoRecogido=doc[0]['Apellido']
        edadRecogido=doc[0]['Edad']

        labelNombre=Label(miFrame,text="Nombre")
        labelNombre.grid(row=0,column=0,padx=10,pady=10)
        cuadroNombre=Entry(miFrame,textvariable=nombreEscrito,justify='center')
        cuadroNombre.insert(END,nombreRecogido)    
        cuadroNombre.grid(row=0,column=1,padx=10,pady=10)

        labelApellido=Label(miFrame,text="Apellido")
        labelApellido.grid(row=1,column=0)
        cuadroApellidos=Entry(miFrame,textvariable=apellidoEscrito,justify='center')
        cuadroApellidos.insert(END,apellidoRecogido)
        cuadroApellidos.grid(row=1,column=1,padx=10,pady=10)

        labelEdad=Label(miFrame,text="Edad:")
        labelEdad.grid(row=2,column=0)
        cuadroEdad=Entry(miFrame,textvariable=edadEscrito,justify='center')
        cuadroEdad.insert(END, edadRecogido)
        cuadroEdad.grid(row=2,column=1,padx=10,pady=10)

        b1=Button(miFrame,text="Guardar",font=("Helvetica,8"),height=1,width=4,command=lambda:[escribirYaml()],pady=10,padx=10)
        b1.grid(row=3,column=1)
else:
    
    labelNombre=Label(miFrame,text="Nombre:")
    labelNombre.grid(row=0,column=0,padx=10,pady=10)
    cuadroNombre=Entry(miFrame,textvariable=nombreEscrito,justify='center')
    cuadroNombre.grid(row=0,column=1,padx=10,pady=10)


    labelApellido=Label(miFrame,text="Apellidos:")
    labelApellido.grid(row=1,column=0)
    cuadroApellidos=Entry(miFrame,textvariable=apellidoEscrito,justify='center')
    cuadroApellidos.grid(row=1,column=1,padx=10,pady=10)

    labelEdad=Label(miFrame,text="Edad:")
    labelEdad.grid(row=2,column=0)
    cuadroEdad=Entry(miFrame,textvariable=edadEscrito,justify='center')
    cuadroEdad.grid(row=2,column=1,padx=10,pady=10)

    b1=Button(miFrame,text="Guardar",font=("Helvetica,8"),height=1,width=4,command=lambda:[escribirYaml()],pady=10,padx=10)
    b1.grid(row=3,column=1)

root.mainloop()
