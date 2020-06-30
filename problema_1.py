print("Problema 1")

def es_vocal(c):
    vocal = "aeiouáéíóú"
    if c in vocal:
        return True
    return False
def porcentaje(suma, total):
    if total > 0:
        p = round((suma * 100) / total, 2)
    else:
        p = 0
    return p

def promedio(suma, total):
    if total > 0:
        prom = round(suma / total, 2)
    else:
        prom = 0
    return prom


cont_letras = 0
flag_s = flag_si = False
cont_ini_si = 0
pal_imparv = 0
car_anterior = ""
fin_vocal = False
cont_vocal = 0
pal_solov = 0
primera = ""
pal_inifin = 0
flag_cc = False
cont_c = 0
pal_cc = 0
palabra = 0
acu_letras = 0
texto = input("Cargue un texto. Termina con un punto: ")
texto = texto.lower()

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if cont_letras == 1 and caracter == "s":
            flag_s = True
        else:
            if flag_s and caracter == "i":
                flag_si = True
            flag_s = False
        # if es_vocal(car_anterior):
        #     fin_vocal = True
        if es_vocal(caracter):
            cont_vocal += 1

        if caracter == "c":
            cont_c += 1
            if cont_c == 2:
                flag_cc = True
        else:
            cont_c = 0
        if cont_letras == 1:
            primera = caracter
        car_anterior = caracter
    else:
        if cont_letras == 0:
            continue
        palabra += 1
        acu_letras += cont_letras
        if flag_si:
            cont_ini_si += 1
        if es_vocal(car_anterior) and (cont_letras % 2 != 0):
            pal_imparv += 1
        if cont_vocal == 1:
            pal_solov += 1
        if primera == car_anterior:
            pal_inifin += 1
        if flag_cc:
            pal_cc += 1
        if palabra == 1 or cont_letras < menor:
            menor = cont_letras
        cont_letras = 0
        flag_si = False
        # fin_vocal = False
        flag_cc = False
        cont_vocal = 0

porc_pvimpar = porcentaje(pal_imparv, palabra)
prom_letras = promedio(acu_letras, palabra)
print("Cantidad de palabras que comienzan con 'si':",cont_ini_si)
print("Cantidad de palabras que terminan con vocal y tienen cantidad impar "
      "de letras:",pal_imparv)
print("Cantidad de palabras que tienen una sola vocal:",pal_solov)
print("Cantidad de palabras que comienzan y terminan con la misma letra:",
      pal_inifin)
print("Cantidad de palabras con la expresión 'cc':",pal_cc)
print("Porcentaje de palabras impar y terminan en vocal:",porc_pvimpar)
print("Longitud de la palabra más corta:",menor)
print("Promedio de letras por palabra:",prom_letras)