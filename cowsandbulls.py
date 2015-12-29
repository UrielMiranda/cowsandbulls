# Este es el juego de vacas y toros
# Aleatoriamente "generar" un número de 4 dígitos. "Pida al usuario" que adivinar un número de 4 dígitos. "Por cada dígito que el usuario adivinó" correctamente
# en el lugar correcto, tienen una "vaca". Por cada dígito del usuario adivinó correctamente en el lugar equivocado es un "toro". Cada vez que
# el usuario realiza una conjetura, decirles cuántos "vacas" y "toros" tiene.
# Una vez que el usuario adivina el número correcto, el juego ha terminado
# Mantenga un "registro del número de intentos" que el usuario realiza en todo el juego y "mostrarlo al usuario" una vez finalizado el juego.

import random


def generate_digit():
        cows = 0
        bulls = 0
        digit = str(random.randint(1000,9999))
        numUser = input("Numero de 4 digitos\n")
        for i in digit:
            for j in numUser:
                if(j == i):
                    bulls += 1

        print("\nRandom: ",digit)
        print("User: ",numUser)
        print("\nTienes ",cows," cows y " ,bulls, " bulls")



generate_digit()
