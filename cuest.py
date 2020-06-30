def mensaje(m):
    print('El mensaje es:', m)


def invertir(m):
    print('El mensaje (invertido) es:')

    n = len(m)
    for i in range(n - 1, -1, -1):
        print(m[i], end='')


def test():
    cadena = input('Ingrese un mensaje: ')
    mensaje(cadena)
    invertir(cadena)


test()