class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon
    
    def __lt__(self, otro):
        return self.lat
    
coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

#print(coords == coords2) 
# Comparamos dos objetos utlizando el metodo magico __eq__ ya que sin el metodo devuelve false por la direccion física de la memoria RAM


print(coords != coords2) 