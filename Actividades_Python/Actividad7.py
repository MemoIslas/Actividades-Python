"""Guess the number
You ask a user to guess a number between 1 and 50.

If they guess outside that range, you prompt with an error encouraging them to choose a number within the proper range.

Whenever they guess the wrong number you ask if they want to keep playing or if they'd like to quit.

Finally, when the user eventually guesses the right number you congratulate them and show the number of attempts they had."""

"""Adivina el número
Le pides a un usuario que adivine un número entre 1 y 50.

Si adivinan fuera de ese rango, les indicará un mensaje de error alentándolos a elegir un número dentro del rango adecuado.

Cada vez que adivinan el número equivocado, les preguntas si quieren seguir jugando o si quieren dejarlo.

Finalmente, cuando el usuario finalmente adivina el número correcto, lo felicita y le muestra la cantidad de intentos que tuvo.
"""

import random
randNumber = random.randint(1,50)

choise = "Y"

while choise == "Y" or choise == "y":
    number = int(input("Try to guess the number between 1 and 50: "))
    
    while number > 50 or number < 0:
        number = int(input("Try to guess the number between 1 and 50: "))
        print ("Choose number between 1 and 50")

    if number == randNumber:
        print("You guessed")
        choise = "N"
    else:
        print("You missied")
        choise = input("Wanna try again?: Y or N")

print (randNumber)