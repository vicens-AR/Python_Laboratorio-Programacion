informacion_personal = [
    {"nombre": "Vicente", "edad": 17},
    {"nombre": "Negro", "edad": 33},
    {"nombre": "Joaco", "edad": 28}
]

for informacion in informacion_personal:
    for clave, valor in informacion.items():
        print(f"{clave}: {valor}")


    