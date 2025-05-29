import json

def load_data_from_json():
    try:
        with open("output.json", "r") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print("Error: El archivo 'output.json' no existe.")
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo 'output.json' no contiene un JSON válido.")
        return {}

# Ejemplo de uso
data = load_data_from_json()
print(data[0])
