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



def mas_cercanos(nombre_archivo, latitud_ori, longitud_ori):
    dependencias = {
    "1" : "MUNI",
    "2" : "SUBV",
    "3" : "PAGA",
    "4" : "CAD",
    "5" : "SLE"
}
    archivo_establecimientos = open(nombre_archivo, "r",encoding="UTF-8")

    lista_final = [
    ] 
    for i in archivo_establecimientos:
  
        line = i.strip().split(";")
        nombre = line[0]
        adv_dep = dependencias[line[3]]
        latitud = (line[5])
        longitud = (line[6])
        if latitud == "SIN INFO":
            continue
        resultado = distancia(latitud_ori,longitud_ori,float(latitud), float(longitud))
        if resultado <= 1:
            temp = [nombre, adv_dep, resultado]
            lista_final.append(temp)
    for i in range(len(lista_final)):
        for j in range(i + 1, len(lista_final)):
            if lista_final[i][2] > lista_final[j][2]:
                lista_final[i], lista_final[j] = lista_final[j], lista_final[i]
    for i in lista_final:
        i.remove(i[-1])
    return lista_final

#nombre;region;comuna;dependencia;rural;latitud;longitud;matricula
def establecimientos_x_region(nombre_archivo, tipo):
    archivo = open(nombre_archivo, "r", encoding="UTF-8")
    dict_f = {}
    lista_final = []
    tipo_dic = {
        "0": "urbano",
        "1": "rural"
    }
    for i in archivo:
        line = i.strip().split(";")
        if int(line[4]) == tipo:
            nombre = line[0]
            region = line[1]
            comuna = line[2]
            tipo_text = tipo_dic[line[4]]
            matriculados = int(line[7])
            if region not in dict_f:
                dict_f[region] = []
            x_23 = [nombre, comuna, matriculados]
            dict_f[region].append(x_23)
    for region in dict_f:
        lista = dict_f[region]
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j][2] < lista[j+1][2]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        dict_f[region] = lista
    for region_d in dict_f:

        top10 = dict_f[region_d][:10]

        lista_final.append([region_d,top10[0][0]])
        archivo_salida = open(f"src/examples/Certamen-2/salidas/{region_d}_{tipo_dic[str(tipo)]}.txt", "w", encoding="UTF-8")
        for i in top10:
            archivo_salida.write(f"{i[0]} ({i[1]}) : {i[2]} estudiantes\n")

    return lista_final
    
print(establecimientos_x_region("src/examples/Certamen-2/establecimientos.csv", 1))
    


