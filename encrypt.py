import sys
import json
from operator import itemgetter

def encrypt(plain_text, key):
    reversed_key = {v: k for k, v in key.items()}
    cipher_text = ''
    for c in plain_text:
        if c in reversed_key.keys():
            cipher_text += reversed_key[c]
        else:
            cipher_text += c
    return cipher_text

if __name__ == "__main__":
    if len(sys.argv) == 3:
        key_string = sys.argv[2]
        key_dict = json.loads(key_string)
        sorted_key_list = sorted(key_dict.items(), key=itemgetter(0))
        plain_text = sys.argv[1]
        
        cipher_text = encrypt(plain_text, key_dict)
        key_applied = ''
        for c in plain_text:
            if c in key_dict.keys():
                key_applied += '+'
            else:
                key_applied += '-'

        print("Plain Text: ") 
        print(plain_text)
        print('-')
        print("Cipher Text: ") 
        print(cipher_text)
        print(key_applied)
        print('-')
    else:
        print("Two arguments required")
