from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import sleep
import sqlite3

def bd(fila,columna):
    conexion = sqlite3.connect("Bebidas")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM BEBIDAS")
    bebidas = cursor.fetchall()
    conexion.commit()
    conexion.close()
    for b in bebidas:
        if(b[0]==fila):
            return b[columna]

def imageSize(img,width,height):
    sImg = Image.open("/home/pi/Desktop/proyecto/imagenes/"+img+".png")
    sImg = sImg.resize((width,height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(sImg)
    return img

def crearBoton(frame,txt,mood,r,c,img,f
               ,posx=0,posy=0,x=75,y=75):
    if(mood=='grid'):
        lblImg = Label(frame, image=img)
        lblImg.grid(row=r,column=c,pady=12,padx=15)
        btn = Button(frame,text=txt,bg=bd(9,4),fg='white',
                       font=('Verdana',11,'bold'),command=f)
        btn.grid(row=r+1,column=c,pady=0,padx=5)
        
    if(mood=='center'):
        btn = Button(frame,text=txt,bg=bd(9,4),fg='white',
                       font=('Verdana',11,'bold'),command=f)
        btn.place(x=posx,y=posy+y+12)
        frame.update()
        c=(btn.winfo_width()-x)/2
        lblImg = Label(frame, image=img)
        lblImg.place(x=posx+c,y=posy)
        
    if(mood=='buttonG'):
        btn = Button(frame,text=txt,command=f,bg=bd(9,4),fg='white',
                       font=('Verdana',11,'bold'))
        btn.grid(row=r+1,column=c,pady=0,padx=15)
        
    if(mood=='buttonC'):
        btn = Button(frame,text=txt,bg=bd(9,4),fg='white',
                       font=('Verdana',11,'bold'),command=f)
        btn.place(x=posx,y=posy)
    
def titulo(frame,txt):
    lblMenu = Label(frame, text=txt,
        bg=bd(9,4), fg='white',font=('Verdana',15,'bold'))
    lblMenu.grid(row=0,column=0,padx=50,pady=10,columnspan=3)
    
def null():
    sImg = Image.open("/home/pi/Desktop/proyecto/imagenes/fondo.png")
    sImg = sImg.resize((1,1), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(sImg)
    return img


def label(frame,txt,row,column,size,cs=1):
    lbl = Label(frame, text=txt,
        bg=bd(9,4), fg='white',font=('Verdana',size,'bold'))
    lbl.grid(row=row,column=column,padx=10,pady=20,columnspan=cs)
    frame.update()
    return lbl.winfo_height()
    
def entry(frame,variable,row,column,size,cs=3):
    entrada = Entry(frame,textvariable=variable,
                    bg='white', fg='black',font=('Verdana',size))
    entrada.grid(row=row,column=column,columnspan=cs,padx=10,pady=5)
