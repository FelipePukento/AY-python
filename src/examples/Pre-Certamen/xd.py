'''3.-Función:	agrupa_por_ciudad_y_especie(nombre_archivo)	[30	%]
Objetivo: Agrupar	las	observaciones	por	ciudad	y	por	especie,	generando	un	archivo	
separado	para	cada	especie.
Instrucciones:
- Leer	el	archivo. #1
- Agrupar	las	observaciones	por	especie.
- Listar	las	ciudades	y	fechas	donde	fue	observada	cada	especie.
- Crear	un	archivo	para	cada	especie	llamado	vistos_por_ciudad_<especie>.txt.
- Ordenar	las	ciudades	alfabéticamente	y	las	fechas	cronológicamente.
'''
count = 0
archivo = open("src\examples\Pre-Certamen\pajaros.txt","r", encoding="UTF-8")

observaciones = {
#{'Pelicano': {'Valparaiso': ['2019/12/21', '2019/12/25', '2019/12/29', '2020/01/06']}
#'Gaviota': {'Valparaiso': ['2019/12/21', '2019/12/25', '2020/01/02', '2020/01/06']},
#'Chercan': {'Valparaiso': ['2019/12/21', '2020/01/02'], 'Curico': ['2019/12/23'], 'Santiago': ['2019/12/26', '2020/01/07']}, 
#'Zorzal': {'Santiago': ['2019/12/22', '2020/01/03']},
#'Tenca': {'Santiago': ['2019/12/22', '2019/12/30', '2020/01/03']},
}

for line in archivo:
    line = line.strip()
    dato = line.split(":")
    date = dato[0]
    city = dato[1]
    aves = dato[2].split(",")
    for especie in aves:
        if especie not in observaciones:
            observaciones[especie] = {}
        if city not in observaciones[especie]:
            observaciones[especie][city] = []
        observaciones[especie][city].append(date)
        observaciones[especie][city].sort()
#{'Pelicano': {'Valparaiso': ['2019/12/21', '2019/12/25', '2019/12/29', '2020/01/06']}
#'Gaviota': {'Valparaiso': ['2019/12/21', '2019/12/25', '2020/01/02', '2020/01/06']},
#'Chercan': {'Valparaiso': ['2019/12/21', '2020/01/02'], 'Curico': ['2019/12/23'], 'Santiago': ['2019/12/26', '2020/01/07']}, 
#'Zorzal': {'Santiago': ['2019/12/22', '2020/01/03']},
#'Tenca': {'Santiago': ['2019/12/22', '2019/12/30', '2020/01/03']},

#Chercan:
#Curico:
#2019/12/15
#Santiago:
#2019/12/15
#2019/12/20
#Valparaiso:
#2019/12/17




for especie in observaciones:
    new_arch = open(f"src/examples/Pre-Certamen/archivos_v2/vistos_por_ciudad_{especie}.txt","w", encoding="UTF-8")
    new_arch.write(f"{especie}: \n")
    print(observaciones[especie])
    for city in observaciones[especie]:
        new_arch.write(f"\n{city}:\n")
        for fecha in observaciones[especie][city]:
            new_arch.write(f"{fecha}\n")