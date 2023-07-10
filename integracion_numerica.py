
def sum_rieman(f, a, b, n):
    h = (b-a)/ n
    Acum= 0

    for i in range (n):
        x= a + i * h
        Acum = Acum + h * f(x)
    return Acum


def metodo_trapecio(f, a, b, n):
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i*h
        suma += f(x)
    integral = h * suma
    return integral

