# Determinar la cantidad de palabras que terminan con una vocal y tienen una
# cantidad par de caracteres. Por ejemplo, en el texto:  “Se vienen las
# vacaciones de julio.” Resultado: 2 palabras cumplen con la condición  (
# “Se” y “de”).
# Determinar la cantidad de palabras que contienen al menos 1 vocal y una
# “t”,  en ese orden, pero no necesariamente pegadas. Por ejemplo,
# en el texto:  “Tristeza me dan los que no tienen la oportunidad de
# elegir.”  Resultado: 2 palabras cumplen con la condición (“Tristeza”  [
# tiene una "i" antes de la segunda "t"] y “oportunidad” [ tiene al menos
# una "o" antes de la "t"]).
# Determinar la cantidad de palabras que tienen una “n” justo en la mitad de
# la palabra, siempre que la palabra tenga una cantidad de letras impar.
# Por ejemplo, en el texto: “Junio es un mes lindo para jugar al bingo con
# amigos.” Resultado: 3 palabras cumplen con la condición (“Junio”, “lindo”
# y  “bingo”). Si la cantidad de letras es par, no contar esa palabra de
# ninguna forma.
# Determinar el porcentaje que representan las palabras que incluyen 2
# consonantes seguidas con respecto al total de palabras del texto.  Por
# ejemplo, para el texto: “Este cuatrimestre hubo 130 alumnos en el 1k02.”
# Resultado: Tiene 3 palabras con dos consonantes seguidas  ("Este",
# "cuatrimestre" y "alumnos") sobre un total de 8 palabras del texto,
# por lo que el porcentaje es 37.5 %

print("Simulacro de parcial 7")

# Funciones
def es_vocal(c):
    vocal = "aeiou"
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


# Contadores y Banderas
cont_letras = 0
palabras = 0
pal_fin_vocal_par = 0
car_anterior = ""
cont_vocales = 0
pal_vocal_t = 0
pos_n = 0
pal_n_medio = 0
flag_conso_seguidas = False
pal_conso_seguidas = 0
pos_t = 0

# Carga de texto
texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

# Resolución de los puntos
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_vocal(caracter):
           cont_vocales += 1
        if caracter == "t":
            pos_t = cont_letras
        if caracter == "n":
            pos_n = cont_letras
        if es_consonante(caracter) and es_consonante(car_anterior):
            flag_conso_seguidas = True
    else:
        if cont_letras == 0:
            continue
        palabras += 1
        if es_vocal(car_anterior) and cont_letras % 2 == 0:
            pal_fin_vocal_par += 1
        if cont_vocales >= 1 and pos_t >= cont_vocales:
            pal_vocal_t += 1
        if cont_letras % 2 != 0 and 0 < pos_n < cont_letras:
            pal_n_medio += 1
        if flag_conso_seguidas == True:
            pal_conso_seguidas += 1
        cont_letras = 0
        cont_vocales = 0
        pos_n = 0
        pos_t = 0
        flag_conso_seguidas = False
    car_anterior = caracter


# Cálculos
porc_conso_seguidas = porcentaje(pal_conso_seguidas, palabras)


# Resultados
print()
print("======================= RESULTADOS ===========================")
print()

print("Punto 1...")
print("Cantidad de palabras que terminan en vocal y tienen cantidad par de "
      "letras:",pal_fin_vocal_par)
print()

print("Punto 2...")
print("Cantidad de palabras que tienen al menos 1 vocal y la 't':",pal_vocal_t)
print()

print("Punto 3...")
print("Cantidad de palabras de letras impar con 'n' en el medio:",pal_n_medio)
print()

print("Punto 4...")
print("Porcentaje de palabras que tienen dos consonantes seguidas:",
      porc_conso_seguidas,"%")
print()