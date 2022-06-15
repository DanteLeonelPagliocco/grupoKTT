
from tkinter import *
from tkinter import ttk

class Menu ():  
    db_name='database.db'
    def __init__(self,window):
          self.wind = window
          self.wind.title('UTN MAPS')

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
          ttk.Button(frame,text='Guardar la direccion').grid(row=5,columnspan=2,sticky=W+E)
          #tabla de direcciones 
          self.tree=ttk.Treeview(columns=("id","nombre","apellido","direccion"))
          self.tree.grid(row=6,column=0)

          self.tree.heading('#0',text="id",anchor=CENTER)
          self.tree.heading('#1',text="nombre",anchor=CENTER)
          self.tree.heading('#2',text="apellido",anchor=CENTER)
          self.tree.heading('#3',text="direccion",anchor=CENTER)
          self.tree.heading('#4',text="dni",anchor=CENTER)


if __name__ == '__main__':
    window = Tk()
    application= Menu(window)
    window.mainloop()


