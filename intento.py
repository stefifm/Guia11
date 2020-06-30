print("Intento de mostrar el final de una palabra")

# 1 Determinar la cantidad de palabras que terminan en 'to'

cont_letras = 0
flag_t = False
cont_to = 0
cont_a = 0
pal_a = 0
palabra = 0
cont_palini = 0
pto = 0
pal_ini_todo_texto = 0
texto = input("Cargue un texto. Termina en punto: ")

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if cont_letras == 1:
            if palabra == 0:
                prim_letra_todo_texto = caracter
        if caracter == prim_letra_todo_texto:
            pal_ini_todo_texto += 1
        if caracter == "a":
            cont_a += 1
        if caracter == "t":
            flag_t = True
        else:
            if flag_t and caracter == "o":
                pto = cont_letras
            flag_t = False
    else:
        if cont_letras == 0:
            continue
        palabra += 1
        if pto == cont_letras:
            cont_to += 1
        if cont_a == 1:
            pal_a += 1
        cont_letras = 0
        cont_a = 0

print("Palabras que terminaron en 'to':",cont_to)
print("Cantidad de palabras que solo tienen una 'a':",pal_a)
print("Cantidad de palabras que inician con la primera letra de todo el "
      "texto:",pal_ini_todo_texto)

