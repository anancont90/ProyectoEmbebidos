import sqlite3
from tkinter import *
from clases.Recursos import *
from clases.BebidasConAlchol import *
from clases.BebidasSinAlchol import *
from tkinter import messagebox as mb

def Configuracion():
    
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
    
    def editar():
        if(nombre.get()==''):
            mb.showwarning('Faltan datos','Debe llenar todos los formularios',parent=root)
        elif(img.get()==''):
            mb.showwarning('Faltan datos','Debe llenar todos los formularios',parent=root)
        elif(cont.get()==''):
            mb.showwarning('Faltan datos','Debe llenar todos los formularios',parent=root)
        else:
            conexion = sqlite3.connect("Bebidas")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM BEBIDAS")
            bebidas = cursor.fetchall()
            bebidaID=''
            for b in bebidas:
                if(b[1]==nombre.get()):
                    bebidaID = b[0]
            cursor.execute("UPDATE BEBIDAS SET Nombre='"+nombre.get()+
                           "',Imagen='"+img.get()+
                           "',Contenido='"+cont.get()+
                           "',Fondo='"+fondo.get()+
                           "'WHERE ID="+ID.get())
            conexion.commit()
            conexion.close()
            
    def agregar():
        if(nombre.get()==''):
            mb.showwarning('Faltan datos','Debe llenar todos los formularios',parent=root)
        elif(img.get()==''):
            mb.showwarning('Faltan datos','Debe llenar todos los formularios',parent=root)
        elif(cont.get()==''):
            mb.showwarning('Faltan datos','Debe llenar todos los formularios',parent=root)
        else:
            conexion = sqlite3.connect("Bebidas")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO BEBIDAS VALUES(NULL,'"+nombre.get()+
                           "','"+img.get()+
                           "','"+cont.get()+
                           "','"+fondo.get()+"')")
            conexion.commit()
            conexion.close()
        
        
    def buscar():
        if(nombre.get()==''):
            mb.showwarning('Faltan datos','Debe llenar todos los formularios',parent=root)
        else:
            conexion = sqlite3.connect("Bebidas")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM BEBIDAS WHERE Nombre='"+nombre.get()+"'")
            bebidas = cursor.fetchall()
            for b in bebidas:
                nombre.set(b[1])
                img.set(b[2])
                cont.set(b[3])
                fondo.set(b[4])
                ID.set(b[0])
            conexion.commit()
            conexion.close()
                
    def cancelar():
        root.destroy()
    
    #Se crea la base de datos
    
    root = Toplevel()
    root.geometry('490x320+0+0')
    root.resizable(0,0)
    root.title('Configuracion')
    
    #Configuracion de la interfaz
    frame = Frame(root,width=490,height=320,bg=bd(9,4))
    frame.pack(fill='both',expand='True')
    
    #Se ajusta el tamagno de las imagenes
    coctel = imageSize("cocteles",150,130)
    
    #Se le agrega elementos a la interfaz
    label(frame,'Nombre:',0,0,14)
    nombre = StringVar()
    entry(frame,nombre,0,1,14)
    
    label(frame,'Imagen:',1,0,14)
    img = StringVar()
    entry(frame,img,1,1,14)
    
    label(frame,'Contenido:',2,0,14)
    cont = StringVar()
    entry(frame,cont,2,1,14)
    
    label(frame,'Fondo:',3,0,14)
    fondo=StringVar()
    entry(frame,fondo,3,1,14)
    
    ID=StringVar()
    entrada = Entry(frame,textvariable=ID,font=('Verdana',14,'bold'),
                    state=DISABLED,justify=CENTER)
    entrada.place(x=45,y=265,width=50,height=35)
    
    crearBoton(frame,'Buscar','buttonG',4,1,null,buscar)
    crearBoton(frame,'Editar','buttonG',4,2,null,editar)
    crearBoton(frame,'Cancelar','buttonG',4,3,null,cancelar)
    
    root.mainloop()

