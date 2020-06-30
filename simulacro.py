print("Simulacro de parcial")

def es_digito(n):
    digito = "0123456789"
    if n in digito:
        return True
    return False

def suma_digitos(c):
    res_dig = 0
    if es_digito(c):
        res_dig = int(c)
    return res_dig

def promedio(suma, total):
    if total > 0:
        prom = suma / total
    else:
        prom = 0
    return prom

def porcentaje(division, total):
    if total > 0:
        p = (division * 100) / total
    else:
        p = 0
    return p


cont_letras = 0
pal_dosdigito = 0
cont_digitos = 0
acu_letras = 0
palabras = 0
pal_l = 0
pos_l = 0
pos_en = 0
cont_l = 0
flag_e = False
pal_en = 0
acu_digitos = 0
flag_suma_digitos = False

texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_digito(caracter):
            cont_digitos += 1
            acu_digitos += suma_digitos(caracter)
        if cont_letras > 1 and caracter == "l":
            pos_l = cont_letras
        if caracter == "e":
            flag_e = True
        else:
            if flag_e and caracter == "n":
                pos_en = cont_letras
            flag_e = False
    else:
        if cont_letras == 0:
            continue
        palabras += 1
        if cont_digitos > 2:
            pal_dosdigito += 1
            acu_letras += cont_letras
        if 0 < pos_l < cont_letras:
            pal_l += 1
        if palabras == 1 or cont_letras < menor:
            menor = cont_letras
            orden = palabras
        if pos_en > 0 and pos_en >= (cont_letras / 2 + 2):
            pal_en += 1
        if acu_digitos > 0:
            flag_suma_digitos = True
        if palabras == 1 or acu_digitos > mayor:
            mayor = acu_digitos
            pos = palabras
        cont_letras = 0
        cont_digitos = 0
        pos_en = 0
        pos_l = 0
        flag_e = False
        acu_digitos = 0

prom_mas_dosdigi = promedio(acu_letras, pal_dosdigito)
porc_en = porcentaje(pal_en, palabras)

if pal_dosdigito > 0:
    print("Promedio de letras con palabras de más de dos dígitos:",
          prom_mas_dosdigi)
else:
    print("No hubo palabras con más de dos dígitos")

print("Palabras con la letra 'l' dentro de la misma:",pal_l)
print("Longitud de la palabra más corta:",menor,"Y su posición:",orden)
print("Porcentaje de palabras con 'en' en la segunda mitad:",porc_en)

if flag_suma_digitos:
    print("Posición de la palabra cuya suma de dígitos es mayor:",pos)
else:
    print("No hubo palabras con dígitos")
