# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una
# variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto
# para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio
# en blanco. El programa debe:
# 1- Determinar la cantidad de palabras formadas por sólo dos caracteres, de forma que uno es
# consonante y el otro vocal (en cualquier orden). Por ejemplo, en el texto: "El paso de los
# jugadores por la copa fue al menos regular." hay 4 palabras que cumplen la condición: "El", "de",
# "la" y "al".
# 2- Determinar cuántas palabras tienen el primer carácter de la primera palabra ingresada más de
# una vez. Por ejemplo, en el texto: "nunca ninguna persona lo enterneció." hay 3 palabras que
# contienen más de una 'n', siendo la 'n' la primera letra del texto: "nunca", "ninguna" y
# "enterneció". Note que la primera palabra del texto podría ella misma cumplir la condición, y
# debe ser contada en ese caso (como "nunca" en este ejemplo).
# 3- Determinar el porcentaje de palabras en todo el texto que tienen la letra ‘a’ como segundo
# caracter. Por ejemplo, en el texto: "La balanza no funciona mas." hay 3 palabras cuya segunda
# letra es una 'a' ('La', 'balanza' y 'mas'), y el texto tiene en total 5 palabras. Por lo tanto, el
# porcentaje que se pide calcular es pc = 3 * 100 / 5 = 60%.
# 4- Determinar la cantidad de palabras que empiezan y terminan con el mismo caracter. Por ejemplo,
# en el texto: "la aldea no tiene ese producto." hay 2 palabras que cumplen lo pedido: "aldea" y
# "ese".

print("Simulacro 4 de parcial")

#Funciones
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

#Contadores y banderas
cont_letras = 0
palabras = 0
flag_vocal_consonante = False
pal_2_vocal_conso = 0
cont_prim_pal = 0
prim_letra_texto = ""
pal_prim_letra_texto = 0
flag_seg_a = False
cont_seg_a = 0
car_anterior = ""
ultimo_caracter = ""
primera = ""
pal_ini_mismo_fin = 0
#Carga de texto
texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()
#Análisis de cada punto
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_vocal(caracter) and es_consonante(car_anterior) or es_consonante(
                caracter) and es_vocal(car_anterior):
            flag_vocal_consonante = True
        if cont_letras == 1:
            if palabras == 0:
                prim_letra_texto = caracter
        if caracter == prim_letra_texto:
            cont_prim_pal += 1
        if cont_letras == 2 and caracter == "a":
            flag_seg_a = True
        if cont_letras == 1:
            primera = caracter

    else:
        if cont_letras == 0:
            continue
        palabras += 1
        if cont_letras == 2 and flag_vocal_consonante == True:
            pal_2_vocal_conso += 1
        if cont_prim_pal > 1:
            pal_prim_letra_texto += 1
        if flag_seg_a:
            cont_seg_a += 1
        ultimo_caracter = car_anterior
        if primera == ultimo_caracter:
            pal_ini_mismo_fin += 1
        cont_letras = 0
        flag_vocal_consonante = False
        flag_seg_a = False
        cont_prim_pal = 0
    car_anterior = caracter


#Cálculos
porcentaje_seg_a = porcentaje(cont_seg_a, palabras)


#Resultados
print()
print("============= RESULTADOS =============")
print()

print("Punto 1...")
print("Cantidad de palabras con 2 carcateres (vocal/consonante o vicerversa):",
      pal_2_vocal_conso)
print()

print("Punto 2...")
print("Cantidad de palabras que tienen el 1er caracter del texto más de una "
      "vez:",pal_prim_letra_texto)
print()

print("Punto 3...")
print("Porcentaje de palabras que tienen la letra 'a' como segundo caracter:",
      porcentaje_seg_a)
print(cont_seg_a)
print()

print("Punto 4...")
print("Cantidad depalabras que empiezan y terminan con el mismo caracter:",
      pal_ini_mismo_fin)