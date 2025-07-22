def factoria(n):
    if n ==0:
        return 1
    else:
        return n*factoria(n-1)


def sumar(n):
    if n==0:
        return 0
    else:
        return n+sumar(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def contadordeletras(palabra, letra):

