from tkinter import *
from clases.Recursos import *
from clases.enviarDatos import *
import sqlite3
import serial
import os, time
puerto_ser=serial.Serial("/dev/ttyACM1",9600)

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

class BebidasConAlcohol:
    def __init__(self):
        #Se configura la ventana
        self.root = Toplevel()
        self.root.geometry("490x320+0+0")
        self.root.resizable(0,0)
        self.root.title("Bebida con alcohol")
        
        #Configuracion de la interfaz
        self.frame=Frame(self.root,width=490,height=320,bg=bd(9,4))
        self.frame.pack(fill='both',expand='True')
        
        #Imagenes
        moj = imageSize(bd(1,2),75,75)
        cb = imageSize(bd(5,2),75,75)
        ron = imageSize(bd(6,2),75,75)
        
        #Aniadir elementos
        titulo(self.frame,'Elija una de las bebidas disponibles')
        
        crearBoton(self.frame,bd(1,1),'grid',1,0,moj,mojito)
        crearBoton(self.frame,bd(5,1),'grid',1,1,cb,cubaLibre)
        crearBoton(self.frame,bd(6,1),'grid',1,2,ron,ronPuro)        
        
        btn = Button(self.frame,text='Back',bg=bd(9,4),fg='white',
                       font=('Verdana',11,'bold'),command=self.root.destroy)
        btn.place(x=210,y=225)
        
        self.root.mainloop()

def mojito():
    puerto_ser.write([49])
    enviar('1')

def cubaLibre():
    puerto_ser.write([50])
    enviar('2')

def ronPuro():
    puerto_ser.write([51])
    enviar('3')
