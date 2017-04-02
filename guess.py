import sys
import json
from operator import itemgetter

def guess(cipher_text, key):
    guess_text = ''
    for c in cipher_text:
        if c in key.keys():
            guess_text += key[c]
        else:
            guess_text += c
    return guess_text

if __name__ == "__main__":
    if len(sys.argv) == 3:
        key_string = sys.argv[2]
        key_dict = json.loads(key_string)
        sorted_key_list = sorted(key_dict.items(), key=itemgetter(0))
        cipher_text = sys.argv[1]
        
        plain_text = guess(cipher_text, key_dict)
        key_applied = ''
        for c in cipher_text:
            if c in key_dict.keys():
                key_applied += '+'
            else:
                key_applied += '-'

        print("Cipher Text: ") 
        print(cipher_text)
        print('-')
        print("Guess Text: ") 
        print(plain_text)
        print(key_applied)
        print('-')
        print("Sorted Key: ")
        for element in sorted_key_list:
            print(element)
    else:
        print("Two arguments required")
