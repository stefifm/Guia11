print("Simulacro de parcial 2")

def es_vocal(c):
    vocal = "aeiouáéíóú"
    if c in vocal:
        return True
    return False

def es_consonante(c):
    consonante = "bcdfghjklmnpqrstvwxyzñ"
    if c in consonante:
        return True
    return False

def promedio(suma, total):
    if total > 0:
        p = suma / total
    else:
        p = 0
    return p


cont_letras = 0
pal_sin_vocal = 0
flag_sinvocal = False
cont_consonantes = 0
cont_vocales = 0
primera = 0
car_anterior = ""
pal_ini_mismo_fin = 0
palabra = 0
ultimo_car_prim_pal = ""
acu_letras_vocales = 0
pal_mas_vocales = 0
prim_vocal_texto = ""
flag_ini_vocal = False
pal_ini_mismo_v = 0

texto = input("Cargue un texto. Termina con un punto: ")
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_consonante(caracter):
            cont_consonantes += 1
        if es_vocal(caracter):
            cont_vocales += 1
        if palabra == 0:
            if prim_vocal_texto == "" and es_vocal(caracter):
                prim_vocal_texto = caracter
        if cont_letras == 1 and prim_vocal_texto == caracter:
            flag_ini_vocal = True

    else:
        if cont_letras == 0:
            continue
        palabra += 1
        if cont_consonantes >= 1 and cont_vocales == 0:
            pal_sin_vocal += 1
        if palabra == 1:
            ultimo_car_prim_pal = car_anterior
        if car_anterior == ultimo_car_prim_pal:
            pal_ini_mismo_fin += 1
        if cont_vocales > cont_consonantes:
            pal_mas_vocales += 1
            acu_letras_vocales += cont_letras
        if flag_ini_vocal == True:
            pal_ini_mismo_v += 1
        cont_letras = 0
        cont_vocales = 0
        cont_consonantes = 0
        flag_ini_vocal = False
    car_anterior = caracter


prom_mas_vocales = promedio(acu_letras_vocales, pal_mas_vocales)

print("Palabras sin vocales:",pal_sin_vocal)
print("Cantidad de palabras que terminan con el último caracter del primer "
      "texto:",pal_ini_mismo_fin)
print("Promedio de palabras que tienen más vocales:",prom_mas_vocales)
print("Cantidad de palabras que comienzan con la primera vocal de todo el "
      "texto:",pal_ini_mismo_v)