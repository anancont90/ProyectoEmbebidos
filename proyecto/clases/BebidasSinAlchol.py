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

class BebidasSinAlcohol:
    def __init__(self):
        #Se configura la ventana
        self.root = Toplevel()
        self.root.geometry("490x320+0+0")
        self.root.resizable(0,0)
        self.root.title("Bebida sin alcohol")
        
        #Configuracion de la interfaz
        self.frame=Frame(self.root,width=490,height=320,bg=bd(9,4))
        self.frame.pack(fill='both',expand='True')
        
        #Imagenes
        coca = imageSize(bd(7,2),75,75)
        sprite = imageSize(bd(8,2),75,75)
        naranja = imageSize('naranjada',75,75)
        
        #Aniadir elementos
        titulo(self.frame,'Elija una de las bebidas disponibles')
        
        crearBoton(self.frame,bd(7,1),'grid',1,2,coca,colaNegra)
        crearBoton(self.frame,bd(8,1),'grid',1,0,sprite,colaBlanca)
        crearBoton(self.frame,'naranja','grid',1,1,naranja,colaNaranja)
        
        btn = Button(self.frame,text='Back',bg=bd(9,4),fg='white',
                       font=('Verdana',11,'bold'),command=self.root.destroy)
        btn.place(x=210,y=225)
        
        self.root.mainloop()
        
def colaNegra():
    puerto_ser.write([52])
    enviar('4')
    
def colaBlanca():
    puerto_ser.write([53])
    enviar('5')
    
def colaNaranja():
    puerto_ser.write([54])
    enviar('6')