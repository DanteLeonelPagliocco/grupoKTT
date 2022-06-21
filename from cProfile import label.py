from cProfile import label
from tkinter import*
from tkinter.ttk import Labelframe
from folium import Marker
import tkintermapview

ventanamapa= Tk()
ventanamapa.title('Mapa de la ciudad')
ventanamapa.geometry("900x700")

my_label= Labelframe(ventanamapa)
my_label.pack(pady=20)
map_widget= tkintermapview.TkinterMapView(my_label,width=800,height=600,corner_radius=0)
map_widget.pack()


#set cordenadas o set direccion
#map_widget.set_position(-32.89675945608357, -68.85342117668434,marker=True)
map_widget.set_address("coronel rodriguez 273, Capital, Mendoza",marker=True)

#marker_2= map_widget.set_address("Av. Arístides Villanueva 405,ciudad, Mendoza")
#marker_3=map_widget
#path_1 = map_widget.set_path([marker_2.position, marker_3.position, (52.57, 13.4), (52.55, 13.35)])


#zoom del mapa
map_widget.set_zoom(15)

ventanamapa.mainloop()