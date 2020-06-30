print("Práctica de parcial - 2017")

# Se pide desarrollar un programa en Python que permita cargar por teclado
# un texto completo en una variable de tipo cadena de caracteres.
# El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para
# indicar el final del texto, y que cada palabra de ese texto está separada de
# las demás por un espacio en blanco. El programa debe:
#
# Determinar la cantidad de palabras que incluyeron al menos 2 dígitos,
# por ejemplo, el texto: “Argentina ganó 2 mundiales en 1978 y en 1986.”
# contiene 2 palabras con al menos 2 dígitos.
# Determinar la cantidad de palabras que comienzan con “la”, por ejemplo,
# el texto: “Las laderas de las montañas están labradas.” contiene 4 palabras
# que comienzan con “la”.
# Determinar el promedio de letras de las palabras que cumplieron con el punto
# 2, por ejemplo, en el texto anterior “laderas” y “labradas” cumplieron la
# condición y su promedio de letras por palabra fue 7.5.
# Determinar la cantidad de palabras que comenzaron con “ll” y además
# incluyeron alguna “v”. Por ejemplo, en el texto: “Las lluvias se llevaron
# los llantos.”, contiene 2 palabras que cumplen la condición.

def es_digitos(n):
    digitos = "0123456789"
    if n in digitos:
        return True
    return False
def porcentaje(contador, acumulador):
    if acumulador > 0:
        p = (contador * 100) / acumulador
    else:
        p = 0
    return p

cont_letras = 0
cont_digitos = 0
pal_digitos = 0
flag_la = flag_l = flag_ll = False
flag_v = False
pal_ini_la = 0
pal_ll_v = 0
cont_ll = 0
acu_letras = 0

texto = input("Ingrese un texto. Termina en punto: ")
texto = texto.lower()

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_digitos(caracter):
            cont_digitos += 1
        if cont_letras == 1 and caracter == "l":
            flag_l = True
        else:
            if flag_l and caracter == "a":
                flag_la = True
            flag_l = False
        if flag_l == True and caracter == "l":
            flag_ll = True
        if caracter == "v":
            flag_v = True
    else:
        if cont_letras == 0:
            continue
        if cont_digitos > 2:
            pal_digitos += 1
        if flag_la:
            pal_ini_la += 1
            acu_letras += cont_letras
        if flag_ll and flag_v:
            pal_ll_v += 1
        cont_letras = 0
        cont_digitos = 0
        flag_la = False
        flag_ll = False
        flag_v = False

porc_pal_la = porcentaje(pal_ini_la, acu_letras)

print("Palabras que tienen al menos dos dígitos:",pal_digitos)
print("Cantidad de palabras que inician con la:",pal_ini_la)
print("Porcentaje de palabras que inician con la:",porc_pal_la)
print("Cantidad de palabras que comienzan con ll y tienen v:",pal_ll_v)
