# Consignas.....

# 1) Determinar la cantidad de palabras con menos de 3 vocales. Ej: "Los
# objetos seran presentados en el juzgado" tiene 4 palabras que cumplen con
# la condición (los, seran, en y el).

# 2) Determinar la cantidad de palabras que comienzan con 't' y tienen al
# menos una letra 'x'. Ej: La carta no es copia exacta del texto original.
# Hay una palabra que cumple con la condición (texto).

# 3) Determinar el porcentaje de las palabras que comienzan y terminan con
# el mismo caracter, respecto al total de palabras del texto. Ej: Los cursos
# 1K01 y 1K14 son espejos. El porcentaje es de 14.28% (texto tiene 7
# palabras de las cuales 1 cumple con la condición: 1K01)

# 4) Determinar cuántas palabras incluyeron la sílaba 'de', pero no tenían
# ninguna letra 'b'. Ej: Debemos ceder y dejar la razón al otro. 2 palabras
# cumplen con la condición (ceder y dejar). La palabra 'debemos' tiene la
# expresión 'de' pero tiene la letra 'b' y es por eso que no es contada.

print("Simulacro de parcial 3")

# Funciones
def es_vocal(c):
    vocal = "aeiouáéíóú"
    if c in vocal:
        return True
    return False

def porcentaje(n, total):
    if total > 0:
        p = n * 100 / total
    else:
        p = 0
    return p



# Contadores y banderas
cont_letras = 0
palabras = 0
cont_vocales = 0
pal_menos_3vocales = 0
comienza_t = False
cont_x = 0
pal_ini_t_x = 0
car_anterior = ""
primera_letra = ""
ultima_letra = ""
pal_ini_mismo_fin = 0
flag_d = flag_de = False
flag_b = False
pal_de_sinb = 0


# Carga de texto
texto = input("Cargar un texto. Termina con un punto: ")
texto = texto.lower()


# Análisis de los puntos
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_vocal(caracter):
            cont_vocales += 1
        if cont_letras == 1 and caracter == "t":
            comienza_t = True
        if caracter == "x":
            cont_x += 1

        if caracter == "d":
            flag_d = True
        else:
            if flag_d and caracter == "e":
                flag_de = True
            flag_d = False
        if caracter == "b":
            flag_b = True
        if cont_letras == 1:
            primera_letra = caracter
        ultima_letra = car_anterior
    else:
        if cont_letras == 0:
            continue
        palabras += 1

        if cont_vocales < 3:
            pal_menos_3vocales += 1

        if comienza_t and cont_x == 1:
            pal_ini_t_x += 1

        if flag_de and flag_b == False:
            pal_de_sinb += 1

        if primera_letra == ultima_letra:
            pal_ini_mismo_fin += 1

        cont_letras = 0
        cont_vocales = 0
        comienza_t = False
        cont_x = 0
        flag_d = flag_de = flag_b = False
    car_anterior = caracter

# Cálculos
porc_mismo_ini_fin = porcentaje(pal_ini_mismo_fin, palabras)


# Resultados
print()
print("============= RESULTADOS =============")
print()

print("Punto 1...")
print("Cantidad de palabras con menos de 3 vocales:",pal_menos_3vocales)
print()

print("Punto 2...")
print("Cantidad de palabras que empiezan con 't' y tienen al menos una "
      "'x':",pal_ini_t_x)
print()

print("Punto 3...")
print("Porcentaje de palabras que comienzan y terminan con el mismo "
      "caracter:",porc_mismo_ini_fin)
print()

print("Punto 4...")
print("Cantidad depalabras que incluyeron 'de', pero no había 'b':",
      pal_de_sinb)
