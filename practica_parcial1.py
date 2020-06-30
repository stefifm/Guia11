# Ejercicio 1 para Parcial 2
# Programa Python que cargue un texto. El mismo termina en punto y hay
# espacios.
# Consignas:
# 1) Determinar la cantidad de palabras del texto
# 2) Determinar la cantidad de palabras que presentan la letra 'rr'
# 3) Determinar la cantidad de palabras que comienzan con 'la'
# 4) Determiananr la cantidad de palabras que incluyeron '10' después de la
# mitad

print("Primer ejercicio de práctica")


cont_letras = 0
palabras = 0
flag_rr = False
flag_l = flag_la = False
flag_1 = flag_10 = False
pal_rr = 0
cont_rr = 0
pal_ini_la = 0
pal_10 = 0
#pos_10 = 0
texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if caracter == "r":
            cont_rr += 1
            if cont_rr == 2:
                flag_rr = True
        else:
            cont_rr = 0
        if cont_letras == 1 and caracter == "l":
            flag_l = True
        else:
            if flag_l and caracter == "a":
                flag_la = True
            flag_l = False

        if caracter == "1":
            flag_1 = True
        else:
            if flag_1 and caracter == "0":
                flag_10 = True
                pos_10 = cont_letras
            flag_1 = False
    else:
        if cont_letras == 0:
            continue
        palabras += 1
        if flag_rr == True:
            pal_rr += 1
        if flag_la == True:
            pal_ini_la += 1
        if flag_10 == True and pos_10 >= (cont_letras // 2):
            pal_10 += 1
        cont_letras = 0
        cont_rr = 0
        flag_rr = False
        flag_la = False
        flag_10 = False

print("Cantidad de palabras en el texto:",palabras)
print("Cantidad de palabras que tienen la letra 'rr':",pal_rr)
print("Cantidad de palabras que comienzan con 'la':",pal_ini_la)
print("Cantidad de palabras que tienen '10' después de la mitad:",pal_10)
