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