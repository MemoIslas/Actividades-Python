"""Mad libs game
Ask the user for an input.

This could be anything such as a name, an adjective, a pronoun or even an action. 
Once you get the input, you can rearrange it to build up your own story."""

"""
Pida al usuario una entrada.

Esto podría ser cualquier cosa, como un nombre, un adjetivo, un pronombre o incluso una acción. 
Una vez que obtenga la entrada, puede reorganizarla para construir su propia historia."""

# Loop back to this point once code finishes
loop = 1

while (loop < 10):

    # All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1