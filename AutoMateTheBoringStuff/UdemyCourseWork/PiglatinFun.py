# English to pig latin
print('Enter the English message to translate into pig latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

piglatin = [] # the list of words in pig latin
for word in message.split():
    #Seperate the non-letters at the start of this word:
    prefixNonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonletters += word[0]
        word = word[1:]
    if len(word) == 0:
        piglatin.append(prefixNonletters)
        continue
    # Seperate the non-letters at the end of the word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:1]
    # Remember if the word was in uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation.

    # seperate the consonants at te start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pog Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    piglatin.append(prefixNonletters + word + suffixNonLetters)
# Join all the words back together into a single string:
print(" ".join(piglatin))



