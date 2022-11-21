"""Biography info
Ask a user for their personal information one question at a time. Then check that the information they entered is valid.
 Finally, print a summary of all the information they entered back to them."""

"""Pídale a un usuario su información personal una pregunta a la vez. Luego verifique que la información que ingresaron sea válida. 
Finalmente, imprima un resumen de toda la información que ingresaron."""

# All the questions that the program asks the user
nombre = input("Nombre: ")
DiaNacimiento = input("Dia de Nacimiento: ")
Direccion = input("Address: ")
metas = input("Metas personal: ")


print ("------------------------------------------")
print ("Nombre: ",nombre)
print ("Dia de Nacimiento: ", DiaNacimiento)
print ("Direccion: ",Direccion)
print ("Metas personales: ", metas)
print ("------------------------------------------")