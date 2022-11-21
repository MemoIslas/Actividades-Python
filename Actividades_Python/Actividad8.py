"""Is a palindrome
Ask the user to give you five words. Then check if any of the five words is a palindrome.

A palindrome is a word that remains the same whether it's read forward or backward."""

"""Es un palindromo
Pídele al usuario que te dé cinco palabras. Luego verifica si alguna de las cinco palabras es un palíndromo.

Un palíndromo es una palabra que permanece igual ya sea que se lea hacia adelante o hacia atrás."""

def convertInputString():
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ") 
    rawString = rawInput.lower() 
    rawList = list(rawString) 
    return rawList

def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in dirtyList: 
            dirtyList.remove(character) 
            return stripAnalphabetics(dirtyList)
    return dirtyList 

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "The text you have entered is a palindrome!" 
    else: 
        return "The text you have entered is not a palindrome." 

def main(): 
    print("\nPalindrome checker") 
    originalList = convertInputString()  
    originalList = stripAnalphabetics(originalList) 
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

main() 