"""What's my acronym?
Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user."""

"""
Pídale al usuario que ingrese el significado completo de una organización o concepto y le proporcionará el acrónimo al usuario."""

def fxn(stng): 
    oupt = stng[0] 
      
    for i in range(1, len(stng)): 
        if stng[i-1] == ' ':    
            oupt += stng[i] 
              
    oupt = oupt.upper() 
    return oupt 

organization = input("Organization name: ")
print(fxn(organization)) 