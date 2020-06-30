# 4. Parcial 1 [1k01/05/14] 2017
# Se pide desarrollar un programa en Python que permita cargar por teclado un
# texto completo en una variable de tipo cadena de caracteres.  El texto
# finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar
# el final del texto, y que cada palabra de ese texto está separada de las
# demás por un espacio en blanco. El programa debe:
#
# 1- Determinar la cantidad de palabras que terminaron en vocal.  Por
# ejemplo, en el texto: “En el mar Dios me escucha.”, tiene 2 palabras
# terminadas en vocal.
#
# 2- El porcentaje de consonantes y el porcentaje de vocales en
#  todo el
#  texto (tener en cuenta que puede haber otros caracteres):  “La
#  universidad es una etapa mas de la vida entre los 18 y los 25 años.”
#  Contiene 27 consonantes, 23 vocales y 54 caracteres en total.
#
# 3- Determinar qué palabra tuvo la mayor cantidad de consonantes del texto
# y mostrar su número de orden entendiendo que la primera palabra tiene
# orden  1. Por ejemplo, en el texto: “Los mandriles de Brasil son material
# de  estudio.”, la palabra “mandriles” con 6 consonantes es la que más
# consonantes tiene y su número de orden es 2.
#
# 4- Determinar la cantidad de palabras que comenzaron con primera letra de
# todo el texto y además incluyeron “st”. Por ejemplo, en el texto:  “En
#  este parcial estamos evaluando lógica.”, encontramos 2 palabras que
#  cumplen la condición “este” y “estamos”.

print("Otra práctica de parcial")

# Funciones
def es_vocal(c):
    vocal = "aeiouáéíóú"
    if c in vocal:
        return True
    return False

def es_letra(c):
    if c >= "a" and c <= "z":
        return True
    return False

def es_consonante(c):
    if es_letra(c) and es_vocal(c) == False:
        return True
    return False

def porcentaje(n, total):
    if total > 0:
        p = n * 100 / total
    else:
        p = 0
    return p


# Contadores
cont_letras = 0
car_anterior = ""
pal_fin_vocal = 0
cont_consonantes = 0
acu_consonantes = 0
cont_vocales = 0
acu_vocales = 0
palabras = 0
acu_letras = 0
primera_letra_texto = ""
flag_s = flag_st = False
pal_ini_igual_st = 0
posicion_cons = 0
comienza = False

# Carga del texto
texto = input("Ingrese un texto. Termina en punto: ")
texto = texto.lower()

# Ciclo For y resolución de los puntos
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_vocal(caracter):
            cont_vocales += 1
        if es_consonante(caracter):
            cont_consonantes += 1
        if cont_letras == 1:
            if palabras == 0:
                primera_letra_texto = caracter
        if caracter == primera_letra_texto:
            comienza = True
        if caracter == "s":
            flag_s = True
        else:
            if flag_s and caracter == "t":
                flag_st = True
            flag_s = False
    else:
        if cont_letras == 0:
            continue
        palabras += 1
        acu_consonantes += cont_consonantes
        acu_vocales += cont_vocales
        acu_letras += cont_letras
        if es_vocal(car_anterior):
            pal_fin_vocal += 1
        if palabras == 1 or cont_consonantes > mayor:
            mayor = cont_consonantes
            posicion_cons = palabras
        if comienza and flag_st:
            pal_ini_igual_st += 1
        cont_letras = 0
        cont_consonantes = 0
        cont_vocales = 0
        flag_s = flag_st = False
        comienza = False
    car_anterior = caracter

porcentaje_consonantes = porcentaje(acu_consonantes, acu_letras)
porcentaje_vocales = porcentaje(acu_vocales, acu_letras)

print("============= RESULTADOS =============")
print()
print("Punto 1: Cantidad de palabras que terminaron con vocal:",pal_fin_vocal)

print("Punto 2...")
print("Porcentaje de consonantes:",porcentaje_consonantes)
print("Porcentaje de vocales:",porcentaje_vocales)

print("Punto 3...")
print("Palabra con mayor cantidad de consonantes:",mayor,"y su posición:",
      posicion_cons)

print("Punto 4...")
print("Cantidad de palabras que comenzaron con la primera letra del texto e "
      "incluyeron st:",pal_ini_igual_st)
