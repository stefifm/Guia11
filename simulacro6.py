# 1) Determinar la cantidad de palabras que tuvieron exactamente 3 vocales
# 2) Determinar el porcentaje de palabras con 'si' y 'no'
# 3) Determinar la posición de la palabra más larga del texto
# 4) Determinar la cantidad de palabras que terminan con 'io' y tienen más
# de 3 letras.

print("Simulacro de parcial 6")

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
cont_vocales = 0
pal_3_vocales = 0
palabras = 0
flag_s = flag_si = False
flag_n = flag_no = False
pal_si_no = 0
pos_mayor = 0
flag_i = False
pos_io = 0
pal_fin_io = 0
# Carga de texto
texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()


# Resolución de los problemas
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_vocal(caracter):
            cont_vocales += 1
        if caracter == "s":
             flag_s = True
        else:
            if flag_s and caracter == "i":
                flag_si = True
            flag_s = False
        if caracter == "n":
            flag_n = True
        else:
            if flag_n and caracter == "o":
                flag_no = True
            flag_n = False
        if caracter == "i":
            flag_i = True
        else:
            if flag_i and caracter == "o":
                pos_io = cont_letras
            flag_i = False

    else:
        if cont_letras == 0:
            continue
        palabras += 1
        if cont_vocales == 3:
            pal_3_vocales += 1
        if flag_si and flag_no:
            pal_si_no += 1
        if palabras == 1 or cont_letras > mayor:
            mayor = cont_letras
            pos_mayor = palabras
        if pos_io == cont_letras and cont_letras > 3:
            pal_fin_io += 1
        cont_letras = 0
        cont_vocales = 0
        flag_s = flag_si = False
        flag_n = flag_no = False
        flag_i = False

# Cálculos
porc_si_no = porcentaje(pal_si_no, palabras)

# Resultados
print()
print("================ RESULTADOS ===============")
print()

print("Punto 1...")
print("Cantidad de palabras con 3 vocales:",pal_3_vocales)
print()

print("Punto 2...")
print("Porcentaje de palabras con 'si' y 'no':",porc_si_no)
print()

print("Punto 3...")
print("Posición de la palabra más larga del texto:",pos_mayor)
print()

print("Punto 4...")
print("Cantidad de palabras que terminan con 'io' y tienen más de 3 "
      "letras:",pal_fin_io)
print()