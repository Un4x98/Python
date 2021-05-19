from tkinter import *
from tkinter import messagebox
import pygame

root= Tk()
root.title('3 en Raya')
root.iconbitmap('C:/Users/Unax/Desktop/Python/3enraya/descarga.ico')


#Musica de Fondo

pygame.mixer.init()
pygame.mixer.music.load("C:/Users/Unax/Desktop/Python/3enraya/pokemonFondo.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=0)
#para que empieze siempre el jugador X
clicked= True
count=0
#cambiar cancion al terminar la partida
def musicaFinal():
    pygame.mixer.music.stop
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/Unax/Desktop/Python/3 en raya/win.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=0)

    
#Metodo deshabilitar botones
def disableButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    

#Metodo para saber quien ha ganado
def heganado():
    global ganador
    ganador=False

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los X han ganado")
        disableButtons()
        
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los X han ganado")
        disableButtons()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los X han ganado")
        disableButtons()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los X han ganado")
        disableButtons()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los X han ganado")
        disableButtons()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los X han ganado")
        disableButtons()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los X han ganado")
        disableButtons()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los X han ganado")
        disableButtons()
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los O han ganado")
        disableButtons()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los O han ganado")
        disableButtons()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los O han ganado")
        disableButtons()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los O han ganado")
        disableButtons()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los O han ganado")
        disableButtons()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los O hann ganado")
        disableButtons()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los O han ganado")
        disableButtons()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        ganador=True
        musicaFinal()
        messagebox.showinfo("3 en raya","Los O han ganado")
        disableButtons()
#Button clicked
def b_click(b):
   global clicked,count

   if b ["text"]==" " and clicked==True:
       b["text"]="X"
       clicked=False
       count +=1
       heganado()
   elif b ["text"]==" " and clicked==False:        
       b["text"]="O"
       clicked=True
       count +=1
       heganado()
   else:
       messagebox.showwarning("3 en raya","Esa opcion ya esta cogida, elige otro!!")
        
       
b1=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b1))
b2=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b2))
b3=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b3))
b4=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b4))
b5=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b5))
b6=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b6))
b7=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b7))
b8=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b8))
b9=Button(root,text=" ",font=("Helvetica,20"),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b9))

#Grid buttons

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)



root.mainloop()