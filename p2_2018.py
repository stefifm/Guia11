print("Parcial 2 1k10 2018")

#Funciones
def es_vocal(c):
    vocal = "aeiouáéíóúAEIOU"
    if c in vocal:
        return True
    return False

def es_letra(c):
    if c >= "a" and c <= "z" or c >= "A" and c <= "Z":
        return True
    return False

def es_consonante(c):
    if es_letra(c) and es_vocal(c) == False:
        return True
    return False

def porcentaje (n1, total):
    if total > 0:
        p = n1 * 100 / total
    else:
        p = 0
    return p



#Carga de contadores y banderas
cont_letras = 0
palabras = 0
cont_vocales = 0
pal_3vocales_4letras = 0
flag_seg_consonante = False
flag_ini_v_p = False
flag_fin_n_a = False
pal_ini_vp_fin_na = 0
pos_na = 0
flag_g = flag_ga = False
cont_ga = 0


# Carga de texto
texto = input("Cargue un texto. Termina en punto: ")

# Ciclo For y resolución de las letras y palabras
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        # Punto 1: Ver cantidad de vocales.
        if es_vocal(caracter):
            cont_vocales += 1
        # Punto 2: ver si hay una consonante en la segunda posición.
        if cont_letras == 2 and es_consonante(caracter):
            flag_seg_consonante = True
        if cont_letras == 1:
            if caracter == "v" or caracter == "V" or caracter == "p" or \
                    caracter == "P":
                flag_ini_v_p = True
        if caracter == "n" or caracter == "a":
            pos_na = cont_letras
        if caracter == "g":
            flag_g = True
        else:
            if flag_g and caracter == "a":
                flag_ga = True
            flag_g = False

    else:
        if cont_letras == 0:
            continue
        palabras += 1
        # Punto 1
        if cont_vocales >= 3 and cont_letras > 4:
            pal_3vocales_4letras += 1
        # Punto 2: Determinar la menor palabra con consonante en segunda
        # posición
        if flag_seg_consonante:
            if palabras == 1 or cont_letras < menor:
                menor = cont_letras
        # Punto 3
        if flag_ini_v_p and pos_na == cont_letras:
            pal_ini_vp_fin_na += 1
        # Punto 4
        if flag_ga:
            cont_ga += 1

        # Reinicio
        cont_letras = 0
        cont_vocales = 0
        flag_seg_consonante = False
        pos_na = 0
        flag_ini_v_p = False
        flag_g = flag_ga = False

# Cálculos
porcentaje_ga = porcentaje(cont_ga, palabras)

# Muestra de resultados
print("Palabras que tenían al menos 3 vocales y más de 4 letras:",
      pal_3vocales_4letras)

print("La longitud de la palabra más corta dentro de los que tenían una "
      "consonante en la segunda posición:",menor)

print("Cantidad de palabras que empiezan con v o p y terminan con n o a:",
      pal_ini_vp_fin_na)

print("Porcentaje de palabras con la expresión ga:",porcentaje_ga,"%")