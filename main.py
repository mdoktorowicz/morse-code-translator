from ascii import lock
from morse_code import code

def translator(msg):
    morse = ""

    for letter in msg:
        try:
            morse = morse + code[letter] + " "
        except KeyError:
            break

    print("Here's the translation: \n")
    print(morse)

print(lock)
print("Welcome to the text-to-Morse code generator!\n")


message = input("Please type the message you want to have translated into morse code.\n")

translator(message)