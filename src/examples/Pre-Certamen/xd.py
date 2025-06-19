r_arch = open("src/examples/Pre-Certamen/pajaros.txt","r")
v_pajaros = {
    #"pajaro" : cant_veces
}
lista_p = []
for line in r_arch:
    dato = line.strip().split(":")

    date = dato[0]
    city = dato[1]
    avistamientos = dato[2].split(",")
    
    for pajaro in avistamientos:
        if pajaro not in v_pajaros:
            v_pajaros[pajaro] = 1
        else:
            v_pajaros[pajaro] += 1



for i in v_pajaros:
    lista_p.append([v_pajaros[i],i])
lista_p.sort()
lista_p.reverse()
print(lista_p)



