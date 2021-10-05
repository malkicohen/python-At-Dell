sentence = input("Please enter a sentence\n")
vowel_letters = ['a', 'A', 'e', 'E', ' i', 'I', 'o', 'O', 'u', 'U']
# words_arr = [word.lower() for word in sentence.split()]
# words_arr.append(sentence.split(' '))
for letter in vowel_letters:
    if sentence.startswith(letter):
        sentence = sentence+'way'
        print(sentence)
    else:
        first_letter = sentence[0]
        sentence = sentence+first_letter+'ay'
        print(sentence)

