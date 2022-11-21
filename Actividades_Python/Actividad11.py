"""Lyrics generator
Ask a user to choose from a list of 10 songs. When the user does, you print out the lyrics to the song they selected."""

"""Generador de letras
Pida a un usuario que elija de una lista de 10 canciones. Cuando el usuario lo hace, imprime la letra de la canción que seleccionó."""

## Yo lo voy a hacer con 3 canciones

print("1) It's Time - Imagine Dragons")
print("2) Vida Buena - Eladio Carrion")
print("3) my strange addiction - Billie Eilish")
print("4) EL NENE - Anuel AA")

cancion = int(input("Selecciona una de las cacniones de la lista (con 1, 2 o 3)"))

if cancion == 1:
    text = open('Its Time - Imagine Dragons.txt').read()
elif cancion == 2:
    text = open('Vida Buena - Eladio Carrion.txt').read()
elif cancion == 3:
    text = open('my strange addiction - Billie Eilish.txt').read()
else:
    text = open('EL NENE - Anuel AA.txt').read()
print ("------------------------------------------")
print(text)
print ("------------------------------------------")