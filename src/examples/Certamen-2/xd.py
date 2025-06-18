
archivo = open("src\examples\Certamen-2\datos.csv","r")


#['Good', 'Within the past year', 'Yes', 'No', 'No', 'Yes', 'Male', '183.0', '77.11', '23.06']

estados = {
}

for line in archivo:
    dato = line.strip().split(";")
    p_state = dato[0]
    validation = dato[2]
    #EN CASO DE QUE NO EXISTA
    if p_state not in estados:
        estados[p_state] = {"count_yes": 0,
              "count_no": 0
              }
        print(estados[p_state])
        if validation =="Yes":
            estados[p_state]["count_yes"] += 1
        else:
            estados[p_state]["count_no"] += 1
    #EN CASO DE SI EXISTA
    else:
        if validation =="Yes":
            estados[p_state]["count_yes"] += 1
        else:
            estados[p_state]["count_no"] += 1
print(estados)