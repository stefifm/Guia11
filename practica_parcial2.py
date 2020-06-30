# Desarrollar un programa python que cargue por teclado un texto. Termina en
# punto y hay espacios.
# 1) Determinar el promedio de letras por palabra
# 2) Determinar la cantidad de palabras que incluyeron la sílaba 'de'
# 3) Determinanr la cantidad de palabras que comienzan con 'll'
# 4) Determinar la cantidad de palabras que comienzan con la misma letra que
# terminó la anterior

print("Segundo ejercicio de práctica para parcial 2")

def promedio(acumulador, contador):
    if contador > 0:
        prom = acumulador / contador
    else:
        prom = 0
    return prom

cont_letras = 0
palabras = 0
acu_letras = 0
cont_de = 0
flag_d = flag_de = False
flag_l = flag_ll = False
pal_ini_ll = 0
pal_ini_fin_igual = 0
ultima_letra = ""
texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if caracter == "d":
            flag_d = True
        else:
            if flag_d and caracter == "e":
                flag_de = True
            flag_d = False
        if cont_letras == 1 and caracter == "l":
            flag_l = True
        else:
            if flag_l and caracter == "l":
                flag_ll = True
            flag_l = False
        if cont_letras == 1 and palabras > 0 and caracter == ultima_letra:
            pal_ini_fin_igual += 1
        ultima_letra = caracter
    else:
        if cont_letras == 0:
            continue
        palabras += 1
        acu_letras += cont_letras
        if flag_de == True:
            cont_de += 1
        if flag_ll == True:
            pal_ini_ll += 1
        cont_letras = 0
        flag_de = flag_ll = False

prom_letras = promedio(acu_letras, palabras)

print("Promedio de letras por palabra:",prom_letras)
print("Cantidad de palabras que incluyeron la sílaba 'de':",cont_de)
print("Cantidad de palabras que comienzan con 'll':",pal_ini_ll)
print("Cantidad de palabras que comienzan con la misma letra que terminó la "
      "anterior:",pal_ini_fin_igual)