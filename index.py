import sqlite3
from tkinter import *
from tkinter import ttk

from numpy import pad
from tkinter_map_prueba import mapa
from consultas import *





class Menu (): 
    
    
#menu principal
    def __init__(self,window):
          self.wind = window
          self.wind.title('UTN MAPS')
          
#Contenedor de la ventana
          self.frame=LabelFrame(self.wind , text="Ingrese Los Datos ")
          self.frame.grid(row=0, column=0,pady=20,padx=20)

#inputs
          #ingreso de la direccion
         
          Label(self.frame,text = 'Ingrese la direccion = ').grid(row=1, column=0)
          ttk.Button(self.frame, text="Buscar en el mapa").grid(row=1,column=1,padx=60)
          
          #ingreso del nombre 
          Label(self.frame,text = 'Nombre/s del Destinatario = ').grid(row=2, column=0,padx=60)
          self.nombre=Entry(self.frame)
          self.nombre.grid(row=2,column=1,padx=60)
          #ingreso del apellido
          Label(self.frame,text = 'Apellido/s del Destinatario = ').grid(row=3, column=0,padx=60)
          self.apellido=Entry(self.frame)
          self.apellido.grid(row=3,column=1,padx=60)
          #ingreso del dni
          Label(self.frame,text = 'DNI del Destinatario = ').grid(row=4, column=0,padx=60)
          self.dni=Entry(self.frame)
          self.dni.grid(row=4,column=1,padx=60)
          #boton de guardado
          self.boton_de_guardado=ttk.Button(self.frame,text='Guardar ',command= lambda :   self.agregarPedido()).grid(row=5,column=0,columnspan=1,sticky=W+E)
          self.boton_de_reseteo=ttk.Button(self.frame,text='Resetear ',command= lambda :   self.borar_datos()).grid(row=5,column=1,columnspan=1,sticky=W+E)

          #boton para eliminar dato guardado

          #tabla de direcciones 
          self.tree2=ttk.Treeview(columns=("id","direccion","latitud","longitud"))
          self.tree2.grid(row=7,column=1)
          self.tree=ttk.Treeview(columns=("id","nombre","apellido","dni","direccion_id"))
          self.tree.grid(row=7,column=0,padx=60)
         
         
         
          self.tree.heading('#0',text="id",anchor=CENTER)
          self.tree.heading('#1',text="nombre",anchor=CENTER)
          self.tree.heading('#2',text="apellido",anchor=CENTER)
          self.tree.heading('#3',text="dni",anchor=CENTER)
          self.tree.heading('#4',text="direccion_id",anchor=CENTER)
          



          self.tree2.heading('#0',text="id",anchor=CENTER)
          self.tree2.heading('#1',text="direccion",anchor=CENTER)
          self.tree2.heading('#2',text="latitud",anchor=CENTER)
          self.tree2.heading('#3',text="longitud",anchor=CENTER)
          

          self.tree.column('#0',width=90)
          self.tree.column('#1',width=90)
          self.tree.column('#2',width=90)
          self.tree.column('#3',width=90)
          self.tree.column('#4',width=90)
          


          
          self.tree2.column('#0',width=90)
          self.tree2.column('#1',width=90)
          self.tree2.column('#2',width=90)
          self.tree2.column('#3',width=90)
          
          self.lista_de_entregas()
# borrar datos una vez se hayan guardado
    def getDirecciones(self):
        query="SELECT * FROM direcciones ORDER BY id DESC"
        result=database_conexion(query)
        return result 
        
    def getDireccion(self,id):
        query=" SELECT * FROM datos "
        result=database_conexion(query,id)
        return result
      
        
    def borar_datos(self):
        self.nombre.delete(0, END)
        self.apellido.delete(0, END)
        self.dni.delete(0, END)
	
   
  #mostrar base de datos en una tabla
    def lista_de_entregas(self):
        records= self.tree.get_children()
        
        for element in records:
            self.tree.delete(element)
       
        rows = database_conexion("SELECT * FROM datos ORDER BY id DESC")
        
        records2= self.tree2.get_children()
       
        for element in records2:
            self.tree2.delete(element)
       
        rows2=self.getDirecciones()
       
        for row in rows:
               self.tree.insert('',0,text=row[0],values=(row[1],row[2],row[3],row[4])) 
      
        for row2 in rows2:
               self.tree2.insert('',0,text=row2[0],values=(row2[1],row2[2],row2[3]))
        
    #Verificar  y insertar datos a la base de datos                   
    def agregarPedido(self):
          if(self.validarPedidoVacio()):
            if (self.pedidoRepetido()==FALSE):
              if(self.validarDni()==True):
                query="INSERT INTO `datos` (`id`, `nombre`, `apellido`, `dni`,`id_direccion`) VALUES (NULL,?,?,?,?) "           
                parameters=(self.nombre.get(),self.apellido.get(),self.dni.get(),1)
                database_conexion(query,parameters)
                self.lista_de_entregas()
                self.borar_datos()
              else:
                   print("error el dni de la persona ingresada es erronea")
            else : 
                print("error pedido repetido")
            
          else:
                print("no se puede ingresar datos vacios")
                self.lista_de_entregas()
    def validarPedidoVacio(self):
        return len(self.nombre.get()) != 0 or len(self.apellido.get())!= 0  or len(self.dni.get())!= 0
    def validarDni(self):
        return len(self.dni.get()) ==8

        
    def pedidoRepetido(self):
        rows = database_conexion("SELECT * FROM datos ORDER BY id DESC")
        validacion=FALSE
        for row in rows:
            if row[1] == self.nombre.get()  and row[2] == self.apellido.get() and row[3] ==self.dni.get() :
                
                validacion=TRUE
                break
    
        return validacion
#llamada al menu principal
if __name__ == '__main__':
    window = Tk()
    window.geometry("1520x707")
    application= Menu(window)
    window.mainloop()


