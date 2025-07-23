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
    if palabra == "":
        return 0
    else:
        return palabra.count(letra)


def invertircadena(texto):
    if texto == "":
        return 0
    else:
        return texto[::-1]
















def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente-1)






opcion = ""
while opcion != "0":
    print("\n seleccione una opcion")
    print("1. calcular la factorial de un numero")
    print("2. suma de los primero N numeros naturales")
    print("3. calcular N-esimo numero de fibonacci")
    print("4. contar cuantas veces aparece una letra")
    print("5. invertir una cadena de texto")
    print("6. calcular la potencia")
    print("0. salir del programa")
    opcion = input()


    if opcion == "1":
        n=int(input("ingrese numero: "))
        print(f"\nla factorial del numero es {factoria(n)}")

    elif opcion == "2":
        n=int(input("ingrese numero: "))
        print(f"\nla suma del numero es {sumar(n)}")



    elif opcion == "3":
        n=int(input("ingrese numero: "))
        print(f"el fibonacci es {fibonacci(n)}")


    elif opcion == "5":
        texto=input("ingrese texto: ")
        print(f"\nEl texto invertido es: {invertircadena(texto)}")






    elif opcion == "6":
        base=int(input("ingrese numero: "))
        expoente=int(input("ingrese numero: "))
        print(f"la potencia es {potencia(base, expoente)}")






