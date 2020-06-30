# Palabras que incluyeron la primera letra de todo el texto

print("Prácticas de comienzo")

comienza = False
cont_letras = 0
prim_letra_texto = ""
pal_incluye_ini = 0
palabras = 0

texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if cont_letras == 1 and palabras == 0:
            prim_letra_texto = caracter
        if caracter == prim_letra_texto:
            comienza = True

    else:
        if cont_letras == 0:
            continue
        palabras += 1
        if comienza == True:
            pal_incluye_ini += 1
        comienza = False
        cont_letras = 0

print("Palabras que incluyen la primera letra del texto:",pal_incluye_ini)
