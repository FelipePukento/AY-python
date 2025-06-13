import math

def distancia(lat1, lon1, lat2, lon2):
    """
    Calculates the great-circle distance between two points on the Earth 
    specified by their latitude and longitude using the Haversine formula.
    The result is returned in kilometers.
    """
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    R = 6371  # Earth's radius in kilometers
    distance = R * c
    return distance



dependencias = {
    "1" : "MUNI",
    "2" : "SUBV",
    "3" : "PAGA",
    "4" : "CAD",
    "5" : "SLE"
}


archivo_establecimientos = open("src/examples/Certamen-2/establecimientos.csv", "r",encoding="UTF-8")
count = 0

#nombre;region;comuna;dependencia;rural;latitud;longitud;matricula
lista_final = [

]
for i in archivo_establecimientos:
    line = i.strip().split(";")
    count +=1
    if count == 10:
        break
    nombre = line[0]
    adv_dep = dependencias[line[3]]
    latitud = float(line[5])
    longitud = float(line[6])
    if latitud == "SIN INFO":
        continue
    resultado = distancia(-33.4918,-70.6175,latitud, longitud)
    if resultado <= 1:
        temp = [nombre, adv_dep]

    lista_final.append(temp)

print(lista_final)