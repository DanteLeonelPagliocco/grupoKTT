import gmaps
#configure api 
gmaps.configure(api_key=123)
#Definir ubicación 1 y 2 
Durango = (37.2753,-107.880067) 
SF = (37.7749,-122.419416)
#Crear el mapa 
fig = gmaps.figure()
#crear la capa 
capa = gmaps.directions.Directions(Durango, SF,mode='car')
#Añadir la capa 
fig.add_layer(layer) 
fig