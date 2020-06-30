print("Mayúsculas")

def es_digito(n):
    digitos = "0123456789"
    if n in digitos:
        return True
    return False
def promedio(suma, total):
    if total != 0:
        prom = round(suma / total, 2)
    else:
        prom = 0
    return prom
def es_mayuscual(c):
    if "A" <= c <= "Z":
        return True
    return False

cont_letras = 0
cont_mayus = 0
flag_mayus = False
cont_e = 0
pal_e = 0
cont_digitos = 0
acu_letras_impar = 0
pal_impar = 0

texto = input("Cargue un texto. Termina en punto: ")

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if cont_letras == 1 and es_mayuscual(caracter):
            flag_mayus = True
        if es_digito(caracter):
            cont_digitos += 1
        if caracter == "e" or caracter == "E":
            cont_e += 1
    else:
        if cont_letras == 0:
            continue
        if flag_mayus == True:
            cont_mayus += 1
        if cont_e > 1:
            pal_e += 1
        if cont_letras % 2 != 0:
            pal_impar += 1
            acu_letras_impar += cont_letras
        cont_letras = 0
        flag_mayus = False
        cont_e = 0

prom_pal_impar = promedio(acu_letras_impar, pal_impar)

print("Cantidad de palabras que empiezan con mayúscula:",cont_mayus)
print("Cantidad de números del 0 al 9 en todo el texto:",cont_digitos)
print("Cantidad de palabras que tienen más de una e:",pal_e)
print("Cantidad de palabras con longitud impar:",pal_impar)
print("Promedio de letras por palabra con longitud impar:",prom_pal_impar)