print()
print("English To German Translator: ")
print("==============================")

print()
print("***************************")
print("* Under Construction...   *")
print("* Under Construction...   *")
print("* Under Construction...   *")
print("***************************")
print()

def main():
    """
    Runs the English to German translation for predefined words.

    This function manages a dictionary of English words and their German translations. 
    It prompts the user to enter an English word and provides the German translation 
    if the word is in the dictionary. The function displays all translation options 
    before starting the translation loop. The translation loop continues until the 
    user decides to exit by entering an empty input. It handles cases where the 
    entered word is not in the dictionary.

    Parameters:
    None

    Returns:
    None: The function directly prints the German translation of the input word.
    """
        
    word_dictionary = {
        "Hello": "Hallo",
        "Bye" : "Tschüss",
        "Milk" : "Milch",
        "Please" : "Bitte",
        "Beer":"Bier",
        "Tea" : "Tee",
        "Or" : "Oder",
        "Coffee" : "Kaffee",
        "Bread" : "Brot",
        "Wine" : "Wein",
        "Water" : "Wasser",
        "Yes" : "Ja",
        "No" : "Nein",
        "Thank you" : "Danke",
        "A (Female)" : "Eine",
        "A (Male)" : "Ein",
        "Father" : "Vater",
        "Mother" : "Mutter",
        "I am" : "Ich Bin",
        "Du Bist" : "You are",
        "I" : "Ich",
        "Am" : "Bin",
        "My (Male)" : "Mein",
        "My (Female)" : "Meine",
        "Husband" : "Mann",
        "Wife" : "Frau",
        "Brother" : "Bruder",
        "Sister" : "Schwester",
        "Son" : "Sohn",
        "Tochter" : "Daughter",
        "Nice" : "Nett",
        "Tall" : "groß",
        "Very":"Sehr",
        "Smart":"Klug",
        "Very Smart":"Sehr Klug",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
        "":"",
    }
    Options = word_dictionary.keys()
    print("Translation options: ")
    print("---------------------")
    print(Options)


    while True: 
        print()
        word = input("Enter a word: ")
        if word == "":
            print()
            break
        if word in word_dictionary:
                print(word, ":", word_dictionary[word])

main()