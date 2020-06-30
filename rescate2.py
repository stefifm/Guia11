# 6. Parcial 2 [1k03] 2018
# Se pide desarrollar un programa en Python que permita cargar por teclado
# un  texto completo en una variable de tipo cadena de caracteres.
#
# El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para
# indicar el final del texto, y que cada palabra de ese texto está separada
# de  las demás por un espacio en blanco. El programa debe:
#
# Determinar cuántas palabras tenían más de cuatro letras y contenían al
# menos  una "n". Por ejemplo, en el texto: “La universidad es una etapa más
# en el camino.”, hay 2 palabras que cumplen la condición ("universidad" y
# "camino").
# Determinar el promedio de letras por palabra entre las que comenzaban con
# "t". Por ejemplo, en el texto: “Ahora tenemos otra tarea.”, hay 2 palabras
# que comienzan con "t" ("tenemos" y "tarea") y suman un total de 12 letras,
# por lo que el promedio pedido es p = 12 / 2= 6 letras por palabra.
#
# Determinar cuántas palabras contenían una "a" y también una "s", pero no
# contenían una "e". Por ejemplo, en el texto: "Ahora estamos en octavos de
# final del mundial.", hay una palabra que cumple la condición ("octavos").
# La palabra "estamos" tiene una "a" y una "s", pero no cuenta porque tiene
# también una "e".
#
# Determinar cuántas palabras contenían al menos una vez la expresión "re"
# pero terminaban con la letra "o". Por ejemplo, en el texto: "El registro
# de goles ha revelado que el réferi se equivoca.". hay dos palabras que
# cumplen la condición ("registro" y "revelado"). La palabra "réferi" tiene
# la expresión "re", pero no cumple porque no termina en "o".

print("Más práctica")

#Funciones

def promedio(suma, total):
    if total > 0:
        prom = suma / total
    else:
        prom = 0
    return prom



#Contadores y banderas
cont_letras = 0
cont_n = 0
pal_mas4_n = 0
comienza_t = False
pal_ini_t = 0
acu_palabras_t = 0
flag_a = flag_s = flag_e = False
pal_as_sin_e = 0
car_anterior = ""
flag_r = False
cont_re = 0
pal_re_o = 0

#Carga de texto

texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()

#Análisis de cada punto

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if caracter == "n":
            cont_n += 1
        if cont_letras == 1 and caracter == "t":
            comienza_t = True
        if caracter == "a":
            flag_a = True
        if caracter == "s":
            flag_s = True
        if caracter == "e":
            flag_e = True
        if caracter == "r":
            flag_r = True
        else:
            if flag_r and caracter == "e":
                cont_re += 1
            flag_r = False
    else:
        if cont_letras == 0:
            continue
        if cont_letras > 4 and cont_n == 1:
            pal_mas4_n += 1
        if comienza_t == True:
            pal_ini_t += 1
            acu_palabras_t += cont_letras
        if flag_a and flag_s and flag_e == False:
            pal_as_sin_e += 1
        if cont_re == 1 and car_anterior == "o":
            pal_re_o += 1

        cont_letras = 0
        cont_n = 0
        comienza_t = False
        flag_a = flag_s = flag_e = False
        cont_re = 0
        flag_r = False

    car_anterior = caracter


#Cálculos
promedio_ini_t = promedio(acu_palabras_t, pal_ini_t)

#Muestra de resultados
print()
print("===================== RESULTADOS =====================")
print()

print("Punto 1...")
print("Cantidad de palabras con más de 4 letras y tenían al menos una 'n':",
      pal_mas4_n)
print()

print("Punto 2...")
print("Promedio de letras por palabras entre que comenzaban con 't':",
      pal_ini_t)
print()

print("Punto 3...")
print("Cantidad de palabras que tenían una 'a' y 's', pero no tenían 'e':",
      pal_as_sin_e)
print()

print("Punto 4...")
print("Cantidad de palabras que tenían al menos la expresión 're' y terminan "
      "con 'o':",pal_re_o)