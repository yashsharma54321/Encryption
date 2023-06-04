import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = ['f', 't', 'W', 'q', '"', 'j', 'L', '$', '+', '3', '8', 'D', '/', 'Z',
       '>', '_', 'r', 'w', 'V', 'x', 'o', '|', '?', 'i', 'Y', '=', 'z', 'U',
       '5', 'E', '{', 'u', '.', 'b', 'T', ' ', '}', 'H', '*', 'v', ';', 'J',
       'e', 'l', '&', '0', '<', 'Q', '\\', 'F', '4', 'S', '!', 'O', 'p', 'n',
       'm', '-', 'N', 's', 'X', ':', 'y', ')', 'k', 'I', 'a', 'K', '^', '~',
       '2', '`', '(', ',', '@', '1', 'B', '%', 'h', "'", '7', '[', 'A', '6',
       'd', 'g', ']', 'P', 'R', 'C', 'G', 'c', '9', '#', 'M']

while True:
    operator = input("Do you want to Encrypt(E) or Decode(D): ").upper()

    #ENCRYPT
    if operator == "E":
        plain_text = input("Enter a message to encrypt: ")
        cipher_text = ""

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]

        print(f"original message : {plain_text}")
        print(f"encrypted message: {cipher_text}")

        next = input("Again?(y/n): ").lower()
        if next == "n":
            print("Goodbye!")
            break
        elif next == "y":
            continue
        else:
            print("Invalid Input!")
            break

    #DECODE
    elif operator == "D":
        cipher_text = input("Enter a message to Decode: ")
        plain_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]

        print(f"encrypted message: {cipher_text}")
        print(f"original message : {plain_text}")

        next = input("Again?(y/n): ").lower()
        if next == "n":
            print("Goodbye!")
            break
        elif next == "y":
            continue
        else:
            print("Invalid Input!")
            break
    
    else:
        print("Invalid Input!")