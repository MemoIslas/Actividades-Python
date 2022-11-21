"""Email Slicer
Collect an email address from the user and then find out if the user has a custom domain name or a popular domain name. 

This is a convenient python project that has a lot of use in the future. 
The program helps get you the username and domain name from an email address.

If you want to push this further, you can customize the application and send a message to the host with this information.
"""

"""Cortador de correo electrónico
Recopile una dirección de correo electrónico del usuario y 
luego averigüe si el usuario tiene un nombre de dominio personalizado o un nombre de dominio popular.

Este es un proyecto de python conveniente que tiene mucho uso en el futuro. 
El programa le ayuda a obtener el nombre de usuario y el nombre de dominio de una dirección de correo electrónico.

Si desea llevar esto más lejos, puede personalizar la aplicación y enviar un mensaje al anfitrión con esta información.
"""

# Get user email address
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice the domain name
domain_name = email[email.index("@")+1:]

# Format message
output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

# Display output message
print(output)