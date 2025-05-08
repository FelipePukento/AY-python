linea = "Z-A-I-C|C-B-R-J|J-E-D-F-H-G|G-L-P-M"

# busca la posición de la estación
def misterio(linea, busca, No_Es_Fin):
    if No_Es_Fin:
        posicion = -1
        for i in range(len(linea)):
            if linea[i] == busca:
                posicion = i
        return posicion
    else:
        for i in range(len(linea)):
            if linea[i] == busca:
                return i
    return -1

def obtener_trayecto(linea, inicio, fin):
    inicio_p = misterio(linea, inicio, True)
    fin_p = misterio(linea, fin, False)
    
    if inicio_p > fin_p: #FILRAR ORDEN
        inicio_p, fin_p = fin_p, inicio_p  
    trayecto = linea[inicio_p:fin_p + 1]
    return trayecto

def obtener_precio(trayecto):
    tramos = 0
    transbordos = 0
    for i in trayecto:
        if i == "-":
            tramos += 1
        elif i == "|":
            transbordos += 1


    if transbordos == 0:
        costo = tramos * 10
        if costo > 30:
            return 30
        return costo

    else:
        costo = tramos * 10 + transbordos * 40
        return costo

# Ejemplos
trayecto = obtener_trayecto(linea, "Z", "R")
print("Trayecto:", trayecto)
print("Precio:", obtener_precio(trayecto))

trayecto2 = obtener_trayecto(linea, "J", "G")
print("Trayecto:", trayecto2)
print("Precio:", obtener_precio(trayecto2))

trayecto3 = obtener_trayecto(linea,"J","E")
print("Trayecto:", trayecto3)
print("Precio:", obtener_precio(trayecto3))