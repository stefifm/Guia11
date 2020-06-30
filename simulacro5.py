# 1) Determinar la cantidad de palabras que incluyeron alguna letra 'e'
# 2) Determinanr la cantidad de palabras que tienen la letra 'h' pero dentro
# de la misma (ni en el comienzo ni en el final)
# 3) Determinar la posicion de la palabra más corta del texto.
# 4) Determinar la cantidad de palabras que comienzan con la última letra de
# la primera palabra del texto y tienen más de 2 vocales.


print("Quinto simulacro de parcial")

# Funciones
def es_vocal(c):
    vocal = "aeiouáéíóú"
    if c in vocal:
        return True
    return False



# Contadores y banderas
cont_letras = 0
palabras = 0
flag_e = False
pal_e = 0
pos_h = 0
pal_medio_h = 0
pos_menor = 0
primera = ""
ultima = ""
car_anterior = ""
pal_ini_texto_fin_2vocales = 0
cont_vocales = 0


#Carga de texto
texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

#Análiis de los puntos
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if caracter == "e":
            flag_e = True
        if cont_letras > 1 and caracter == "h":
            pos_h = cont_letras
        if es_vocal(caracter):
            cont_vocales += 1
        if cont_letras == 1:
            primera = caracter


    else:
        if cont_letras == 0:
            continue
        palabras += 1
        if flag_e == True:
            pal_e += 1
        if 0 < pos_h < cont_letras:
            pal_medio_h += 1
        if palabras == 1 or cont_letras < menor:
            menor = cont_letras
            pos_menor = palabras
        if palabras == 1:
            ultima = car_anterior
        if primera == ultima and cont_vocales > 2:
            pal_ini_texto_fin_2vocales += 1
        cont_letras = 0
        flag_e = False
        pos_h = 0
        cont_vocales = 0
    car_anterior = caracter


# Resultados
print()
print("======================== RESULTADOS ========================")
print()

print("Punto 1...")
print("Cantidad de palabras que incluyeron alguna 'e':",pal_e)
print()

print("Punto 2...")
print("Cantidad de palabras que tienen la letra 'h' en el medio:",pal_medio_h)
print()

print("Punto 3...")
print("Posición de la palabra más corta del texto:",pos_menor)
print()

print("Punto 4...")
print("Cantidad de palabras que comienzan con la última letra de la primera "
      "palabra del texto y tienen más de 2 vocales:",pal_ini_texto_fin_2vocales)
print()