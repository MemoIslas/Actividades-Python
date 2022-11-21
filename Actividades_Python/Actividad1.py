"""Odd or even
Welcome a user then ask them for a number between 1 and 1000.

When the user gives you the number, you check if it's odd or even and then you print a message letting them know."""

"""
Da la bienvenida a un usuario y luego pídele un número entre 1 y 1000.

Cuando el usuario te da el número, compruebas si es par o impar y luego imprimes un mensaje haciéndole saber."""

numero = int(input("Ingresa un número del 1 al 1000: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")