import sqlite3
from tkinter import *
from tkinter import ttk






class Menu ():  
    db_name='database.db'
    def __init__(self,window):
          self.wind = window
          self.wind.title('UTN MAPS')
          
#Contenedor de la ventana
          frame=LabelFrame(self.wind , text="Ingrese una direccion",height=200,width=200)
          frame.grid(row=0, column=0,columnspan=30,pady=20)

#inputs
          #ingreso de la direccion
          Label(frame,text = 'Direccion = ').grid(row=1, column=0)
          self.direccion=Entry(frame)
          self.direccion.focus()
          self.direccion.grid(row=1,column=1)
          #ingreso del nombre 
          Label(frame,text = 'Nombre/s del Destinatario = ').grid(row=2, column=0)
          self.nombre=Entry(frame)
          self.nombre.grid(row=2,column=1)
          #ingreso del apellido
          Label(frame,text = 'Apellido/s del Destinatario = ').grid(row=3, column=0)
          self.apellido=Entry(frame)
          self.apellido.grid(row=3,column=1)
          #ingreso del dni
          Label(frame,text = 'DNI del Destinatario = ').grid(row=4, column=0)
          self.dni=Entry(frame)
          self.dni.grid(row=4,column=1)
          #boton de guardado
          ttk.Button(frame,text='Guardar la direccion',command= lambda :    self.agregarPedido()).grid(row=5,columnspan=2,sticky=W+E)
          #tabla de direcciones 
          self.tree=ttk.Treeview(columns=("id","nombre","apellido","direccion"))
          self.tree.grid(row=6,column=0)

          self.tree.heading('#0',text="id",anchor=CENTER)
          self.tree.heading('#1',text="nombre",anchor=CENTER)
          self.tree.heading('#2',text="apellido",anchor=CENTER)
          self.tree.heading('#3',text="direccion",anchor=CENTER)
          self.tree.heading('#4',text="dni",anchor=CENTER)
          self.lista_de_entregas()
    def database_conexion(self,query,parameters=()):
        with sqlite3.connect(self.db_name) as conn:
    
    
          cursor=conn.cursor()
          result=cursor.execute(query,parameters)
          conn.commit()
          return result
    def lista_de_entregas(self):
        records= self.tree.get_children()
        for element in records:
            self.tree.delete(element)



        rows = self.database_conexion("SELECT * FROM datos ORDER BY id DESC")
        
        for row in rows:
               self.tree.insert('',0,text=row[0],values=(row[1],row[2],row[3],row[4]))           
    def agregarPedido(self):
          if(self.validarPedidoVacio()):
            if (self.pedidoRepetido()==FALSE):
              if(self.validarDni()==TRUE):
                query="INSERT INTO `datos` (`id`, `nombre`, `apellido`, `dni`,`direccion`) VALUES (NULL,?,?,?,?) "           
                parameters=(self.direccion.get(),self.nombre.get(),self.apellido.get(),self.dni.get())
                self.database_conexion(query,parameters)
                self.lista_de_entregas()
              else:
                   print("Error el dni de la persona ingresada es erronea")
            else : 
                print("Error pedido repetido")
            
          else:
                print("no se puede ingresar datos vacios")
                self.lista_de_entregas()
    def validarPedidoVacio(self):
        return len(self.nombre.get()) != 0 and len(self.apellido.get())!= 0 and len(self.direccion.get())!= 0 and len(self.dni.get())!= 0
    def validarDni(self):
        return len(self.dni) < 9
    def pedidoRepetido(self):
        rows = self.database_conexion("SELECT * FROM datos ORDER BY id DESC")
        validacion=FALSE
        for row in rows:
            if row[1] == self.nombre.get()  and row[2] == self.apellido.get() and row[3] ==self.dni.get() and row[4]==self.direccion.get():
                
                validacion=TRUE
                break
    
        return validacion


if __name__ == '__main__':
    window = Tk()
    application= Menu(window)
    window.mainloop()


