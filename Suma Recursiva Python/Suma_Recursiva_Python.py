
def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

try:
    n = int(input("Ingresa un número entero: "))
    resultado = suma_recursiva(n)
    print(f"La suma de los dígitos de {n} es: {resultado}")
except ValueError:
    print("Entrada no válida. Debes ingresar un número entero.")