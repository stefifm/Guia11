# Determinar la cantidad de palabras que tienen 'll' más de una vez
# Determina la cantidad de palabras con vocales y consonantes alternadas

print("Más práctica")

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



cont_letras = 0
cont_ll = 0
ll = 0
pal_mas_ll = 0
flag_voc_conso_alter = True
pal_vc_alter = 0
car_anterior = ""

texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if caracter == "l":
            cont_ll += 1
            if cont_ll == 2:
                ll += 1
        else:
            cont_ll = 0
        if cont_letras > 1 and es_vocal(caracter) and es_vocal(car_anterior)\
                or es_consonante(caracter) and es_consonante(car_anterior):
            flag_voc_conso_alter = False


    else:
        if cont_letras == 0:
            continue
        if ll > 1:
            pal_mas_ll += 1
        if flag_voc_conso_alter == True:
            pal_vc_alter += 1
        cont_letras = 0
        cont_ll = 0
        ll = 0
        flag_voc_conso_alter = True
    car_anterior = caracter

print("Cantidad de palabras que tienen 'll' más de una vez:",pal_mas_ll)
print("Cantidad de palabras con vocal y consonante alternada:",pal_vc_alter)


