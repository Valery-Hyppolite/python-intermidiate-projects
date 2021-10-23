with open("phonic_words.txt") as phonic:
    phonetic_al = phonic.read()
    list_phonic = phonetic_al.split()
    phonetic_dict = {word[0]: word for word in list_phonic}

def generate_phonic():

    user_word = input("Enter a word  ").upper()
    try:
        phonic_word = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print('Sorry, only letter in the alphabet please')
        #user_word = input("Type the word that you want ").upper()
        generate_phonic()  # making a function call itself creates a loop, withou habing to use a while loop in some program like this one.
    else:
        print(phonic_word)
        generate_phonic()

generate_phonic()