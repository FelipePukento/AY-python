linea = "Z-A-I-C|C-B-R-J|J-E-D-F-H-G|G-L-P-M"
# A - B
def misterio(linea, busca,ES_FINAL):
    i = 0
    pos = 0
    if ES_FINAL:
        while i < len(linea):
            if linea[i] == busca:
                return i
            i += 1
    else:
        while i < len(linea):
            if linea[i] == busca:
                pos = i
            i += 1    
        return pos
print(misterio(linea,"G", True))



def sacar_trayecto(linea, inicio, fin):
    inicio_p = misterio(linea, inicio, False)
    fin_p = misterio(linea, fin, True)   
    if inicio_p > fin_p: #FILRAR ORDEN
        inicio_p, fin_p = fin_p, inicio_p  

    trayecto = linea[inicio_p:fin_p + 1]
    return trayecto


print(sacar_trayecto(linea,"R", "Z"))