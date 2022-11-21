"""Word count
Ask the user what's on their mind. Then after the user responds, 
count the number of words in the sentence and print that as an output."""

"""
Pregunte al usuario qué tiene en mente. Luego, después de que el usuario responda, 
cuente la cantidad de palabras en la oración e imprímala como salida."""

import csv
import string

translator = str.maketrans('', '', string.punctuation)

word_count = {}
text = open('declaration.txt').read()

words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

output_file = open('words.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word_count[word]])