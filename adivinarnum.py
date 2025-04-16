"""Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario adivinar el número. El programa debe brindar pistas
(ej. el número secreto es mayor) y debe continuar pidiendo al usuario que adivine hasta que acierte. Al finalizar, debe mostrar el número de intentos."""
import random

def main():
    random_number = random.randint(1, 100)
    print("He seleccionado un número aleatorio entre 1 y 100. ¡Intenta adivinarlo!")

    while True:
        try:
            user_guess = int(input("Ingresa tu número: "))

            if user_guess < random_number:
                print("El número es mayor.")
            elif user_guess > random_number:
                print("El número es menor.")
            else:
                print("¡Felicidades! Adivinaste el número.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

main()
