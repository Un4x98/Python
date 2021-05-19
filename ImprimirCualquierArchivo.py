from tkinter import *
import win32api
import win32print

from tkinter import filedialog


root = Tk() 
  
# Titulo
root.title('Imprimir') 
root.geometry("400x200") 


#Metodo Para Abrir el explorador de archivos e imprimir
def imprimir():
    
    imprimir_archivo=filedialog.askopenfilename(initialdir="C:/Users/Unax/Desktop", title="Selecciona un Archivo para Imprimir", filetypes=(("Block de Notas", "*.txt"),("Documentos de Microsoft Word","*.docx"), ("Todos los Archivos", "*.*"))) 
    if imprimir_archivo:
        win32api.ShellExecute(0,"print",imprimir_archivo,None,".",0)



#Boton Imprimir
Button(root,text='Imprimir Archivo',command=imprimir,).pack() #Con esto se pone el boton arriba del todo por defecto


root.mainloop()