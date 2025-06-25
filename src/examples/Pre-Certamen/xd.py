'''5. [50 %] Escriba la función fechas-por-especie(nombre_archivo), que recibe como parámetro el nombre de 
un archivo con el formato descrito. La función debe crear un archivo especies_por_fecha.txt,
 que agrupe por fecha todas las especies observadas ese día,
 ordenadas alfabéticamente. Las fechas deben aparecer ordenadas cronológicamente.'''

#por cada especie, guardar en un archivo las fechas en las cual se registre
#mes


def fpe(nombre_archivo):
    diccionario = {
       #especie : [fechas]
    }
    archivo = open(nombre_archivo, "r", encoding="UTF-8")
    for line in archivo:
        data = line.strip().split(":")
        date = data[0].split("/")
        city = data[1]
        especies = data[2].split(",")
        for i in especies:
            if i not in diccionario:
                diccionario[i] = []
            diccionario[i].append(date)
    for key in diccionario:
        nuevo_archivo = open(f"{key}_dias_visto.txt","w",encoding="UTF-8")
        for date in diccionario[key]:
            nuevo_archivo.write(f"El año {date[0]} en el mes {date[1]} en la fecha {date[2]} se vio un {key} \n")






fpe("src\examples\Pre-Certamen\pajaros.txt")