from tkinter import *
from clases.Recursos import *
from clases.BebidasConAlchol import *
from clases.BebidasSinAlchol import *
from clases.Configuracion import *
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

class InterfazPrincipal():
    def __init__(self):
        #Se configura la ventana
        self.root = Tk()
        self.root.geometry('490x320+0+0')
        self.root.resizable(0,0)
        self.root.title('Bartender automatico')
        
        #Configuracion de la interfaz
        self.frame = Frame(self.root,width=490,height=320,bg=bd(9,4))
        self.frame.pack(fill='both',expand='True')
        
        #Se ajusta el tamagno de las imagenes
        coctel = imageSize("cocteles",150,130)
        bebida = imageSize("bebidas",150,130)
     
     
        #Se le agrega elementos a la interfaz
        titulo(self.frame,'Bienvenido, que desea beber hoy?')
        
        crearBoton(self.frame,'Bebidas con alchol','center',0,0,
                   coctel,btnBebidasConAlchol,50,80,150,130)
        crearBoton(self.frame,'Bebidas sin alcohol','center',0,0,
                   bebida,btnBebidasSinAlchol,250,80,150,130)
        crearBoton(self.frame,'Configuracion','buttonC',0,0,null,
                   configuracion,340,280)
        
        self.root.mainloop()
    
def btnBebidasConAlchol():
    BebidasConAlcohol()
    
def btnBebidasSinAlchol():
    BebidasSinAlcohol()

def configuracion():
    Configuracion()