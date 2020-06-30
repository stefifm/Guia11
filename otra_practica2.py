# Determinar la cantidad de palabras que terminan con la primera letra de
# todo el texto


cont_letras = 0
car_anterior = ""
ultima = ""
primera = ""
pal_ini_texto_mismo_fin = 0
palabras = 0

texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if cont_letras == 1 and palabras == 0:
            primera = caracter
    else:
        if cont_letras == 0:
            continue
        palabras += 1
        ultima = car_anterior
        if primera == ultima:
            pal_ini_texto_mismo_fin += 1
    car_anterior = caracter

print("Cantidad de palabras que terminan con la primera letra del todo "
      "texto:",pal_ini_texto_mismo_fin)