palabras_generacion_z = {
                        "CRINGE": "Algo exepcionalmente raro o embarazoso"
                        "LOL": "una respuesta comù a algo gracioso"
                        "ROFL": "una respuesta a una broma"
                        "SHEESH": "ligera desaprobacion"
                        "CREEPY": "aterrador, siniestro"
                        "AGGRO": "ponerse agresivo/enojado"
}


word = input("escribe una palabra que no entiendas (en mayuscula)")

if word in palabras_generacion_z():
    print("esa palabra significa:", palabras_generacion_z[word])
else:
    print("esa palabra no la conozco")
