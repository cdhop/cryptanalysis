import sys
import re

def encrypt_vigenere(text, key):
    """Encrypt text using vigenere cipher"""
    vigenere_square = get_vigenere_square()
    plain_text = re.sub("[^a-z]", "", text.lower())
    cipher_text = ''
  
    for index in range(len(plain_text)):
        row_key = key[index % len(key)]
        row = vigenere_square[row_key]
        cipher_text += row[plain_text[index]]

    return cipher_text

def decrypt_vigenere(cipher_text, key):
    """Decrypt cipher_text using vigenere cipher"""
    vigenere_square = get_vigenere_square()
    plain_text = ''

    for index in range(len(cipher_text)):
        row_key = key[index % len(key)]
        row = vigenere_square[row_key]
        for k, v in row.items():
            if v == cipher_text[index]:
                plain_text += k 

    return plain_text

def get_vigenere_square():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vigenere_square = dict()

    for index in range(len(alphabet)):
        row = generate_row(index, alphabet)
        vigenere_square.update(row)

    return vigenere_square

def generate_row(shift, char_set):
    key = char_set[shift]
    set = dict()

    for index in range(len(char_set)):
        shift_index = (shift + index) % len(char_set) 
        set[char_set[index]] = char_set[shift_index].upper()
 
    row = { key: set }
    return row

def generate_alpha_string(input_string):
    alpha_string = ''
 
    for c in input_string:
        if c.isalpha():
            alpha_string += c
    return alpha_string


if __name__ == "__main__":
    if len(sys.argv) == 4:
        if sys.argv[1] == 'encrypt':
            plain_text = sys.argv[2]
            key = sys.argv[3]
  
            cipher_text = encrypt_vigenere(plain_text, key)

            print("Plain Text: " + plain_text)
            print("Cipher Text: " + cipher_text)  
        elif sys.argv[1] == 'decrypt':
            cipher_text = sys.argv[2]
            key = sys.argv[3]

            cipher_text_alpha = generate_alpha_string(cipher_text)
            plain_text = decrypt_vigenere(cipher_text_alpha, key)

            print("Cipher Text: " + cipher_text)
            print("Key: " + key)
            print("Plain Text: " + plain_text)         
        else:
            print("Unknown command")
    else:
       print("Three arguments required")

