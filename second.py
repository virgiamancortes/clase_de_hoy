def contarPares(n):
    """Función cuenta pares hasta n"""
    for i in range(n):
        if i % 2 == 0:
            print(i)


x = 0
while x < 10:
    x = int(input("enter a number: "))
    print(x)
    contarPares(x)


print("Hola Mundo")

