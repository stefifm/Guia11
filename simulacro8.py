# Se pide desarrollar un programa en Python que permita cargar por teclado
# un texto completo en una variable de tipo
# cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario
# cargará el punto para indicar el final del
# texto, y que cada palabra de ese texto está separada de las demás por un
# espacio en blanco. El programa debe incluir
# al menos una función simple con parámetros y retorno de resultado,
# debe  procesar el texto caracter a caracter
# (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente  sin usar
# un menú de opciones:

# Determinar el promedio de consonantes por palabra. Por ejemplo,
# en el texto:  "El ciclo debe hacer 10 repeticiones
# y detenerse." hay 21 consonantes y 8 palabras,  el promedio será 2.65
# consonantes por palabra.
# Determinar la cantidad de palabras que tienen una letra “t” y menos de
# tres letras “a”. Por ejemplo, en el texto
# “Atencion con las materias o atraera malas pasadas.” Resultado: 2
# palabras cumplen con la condición
# (“Atencion” y “materias”).
# Determinar cuántas palabras comienzan con el úlitmo caracter de la
# primera palabra del texto. Por ejemplo, en el
# texto: "Esa alegria enorme." la primera palabra termina con 'a' y  hay una
# palabra que comienza con esa misma letra:
# "alegria".
# Determinar la cantidad de palabras que contienen ‘ll’ en el interior de
# la palabra, es decir sin tener en cuenta
# ni la primera ni la última letra de la palabra. Por ejemplo en el texto:
# “lloraba allá en la calle bajo la lluvia.“,
# las palabras “allá” y “calle” cumplen con la condición. Notar que lloraba
# y lluvia contienen “ll” pero en el comienzo
# de la palabra por lo tanto el resultado para este punto es 2 palabras.

print("Simulacro de parcial 8")

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

def es_digito(c):
    digito = "0123456789"
    if c in digito:
        return True
    return False

def es_consonante(c):
    if es_letra(c) and es_vocal(c) == False and es_digito(c) == False:
        return True
    return False

def promedio(suma, total):
    if total > 0:
        prom = suma / total
    else:
        prom = 0
    return prom



# Contadores y Banderas
cont_letras = 0
palabras = 0
cont_consonantes = 0
acu_consonantes = 0
con_t = 0
cont_a = 0
pal_1t_menos_3a = 0
primera_letra = ""
car_anterior = ""
ultima_letra_prim_texto = ""
pal_fin_texto_mismo_ini = 0
con_ll = 0
pos_ll = 0
pal_ll_medio = 0
# Carga de texto
texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

# Resolución de los puntos
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_consonante(caracter):
            cont_consonantes += 1
        if caracter == "t":
            con_t += 1
        if caracter == "a":
            cont_a += 1
        if cont_letras > 1 and caracter == "l":
            con_ll += 1
            if con_ll == 2:
                pos_ll = cont_letras
        else:
            con_ll = 0
        if cont_letras == 1:
            primera_letra = caracter
    else:
        if cont_letras == 0:
            continue
        acu_consonantes += cont_consonantes
        palabras += 1
        if con_t == 1 and cont_a < 3:
            pal_1t_menos_3a += 1
        if 0 < pos_ll < cont_letras:
            pal_ll_medio += 1
        if palabras == 1:
            ultima_letra_prim_texto = car_anterior
        if primera_letra == ultima_letra_prim_texto:
            pal_fin_texto_mismo_ini += 1
        cont_consonantes = 0
        cont_letras = 0
        con_t = 0
        cont_a = 0
        pos_ll = 0
        con_ll = 0
    car_anterior = caracter
# Cálculos
prom_consonantes = promedio(acu_consonantes, palabras)

# Resultados
print()
print("====================== RESULTADOS =====================")
print()

print("Punto 1...")
print("Promedio de palabras con consonantes:",prom_consonantes)
print()

print("Punto 2...")
print("Cantidad de palabras con una letra 't' y menos de 3 'a':",
      pal_1t_menos_3a)
print()

print("Punto 3...")
print("Cantidad de palabras que comienzan con el último caracter de la "
      "primera palabra del texto:",pal_fin_texto_mismo_ini)
print()

print("Punto 4...")
print("Cantidad de palabras que tienen 'll' en el interior de la palabra:",
      pal_ll_medio)
print()