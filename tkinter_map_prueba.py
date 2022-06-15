

from turtle import width
from numpy import True_, size
import tkintermapview
import pyperclip

from tkinter import *
from consultas import id_actual
from consultas import database_conexion
    

        
def mapa( ):
          
         
          
            root = Toplevel()
            root.geometry("1000x1000")
            root.title("prueba de mapa con tkinter")
          
            my_frame = LabelFrame(root)
            my_frame.pack(pady=20)
          
            map_widget = tkintermapview.TkinterMapView(my_frame , width=800,height=600)
            map_widget.grid(row=0 ,column=0)
            
            
            direccion=Entry(my_frame,font=("Helvetica",29))
            direccion.grid(row=1,column=0,padx=10,pady=10)
            
            buscar=Button(my_frame,text="Buscar Direccion",font=("Helvetica",19),command= lambda: BuscarDireccion(map_widget,direccion))
            buscar.grid(row=2,column=0,padx=10,pady=10)

            
            confirmar=Button(my_frame,text="Confirmar Direccion",font=("Helvetica",19),command= lambda : [ConfirmarDireccion(direccion),Label(root,text = 'Dirreccion Guardada').pack()])
            confirmar.grid(row=2,column=1,pady=10)


           

            root.mainloop()

         

         


def BuscarDireccion(map_widget,direccion):
        map_widget.set_address(direccion.get(), marker=True)
        
def ConfirmarDireccion(direccion):
    
   
 address = tkintermapview.convert_address_to_coordinates(direccion.get())

 lat=address[0]
 long=address[1]
 query="INSERT INTO `direcciones` (id,direccion,latitud,longitud) VALUES (NULL,?,?,?)"
 parameters=(direccion.get(),lat,long)
 database_conexion(query,parameters)



