import random


alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
key = [chr(i) for i in range(ord("a"), ord("z") + 1)]

# Gauss improvement applied only for letter "e"
e_char_additional_cipher_chars = ["?", "&"]


def encrypt(plain_text):
    cipher_text = ""
    e_char_cipher_char_index = 0
    for char in plain_text:
        if char not in alphabet:
            cipher_text += char
        elif char == "e":
            if e_char_cipher_char_index == 0:
                cipher_text += key[alphabet.index(char)]
            else:
                cipher_text += e_char_additional_cipher_chars[(e_char_cipher_char_index - 1) % (len(e_char_additional_cipher_chars) + 1)]
            e_char_cipher_char_index = (e_char_cipher_char_index + 1) % (len(e_char_additional_cipher_chars) + 1)
        else:
            cipher_text += key[alphabet.index(char)]
    return cipher_text


def decrypt(cipher_text):
    plain_text = ""
    for char in cipher_text:
        if char not in alphabet and char not in e_char_additional_cipher_chars:
            plain_text += char
        elif char in e_char_additional_cipher_chars:
            plain_text += "e"
        else:
            plain_text += alphabet[key.index(char)]
    return plain_text


def main():
    random.shuffle(key)
    cipher_text = encrypt("napad je u podneeeeeeeee")
    plain_text = decrypt(cipher_text)
    print(plain_text)
    print(cipher_text.upper())


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches (assumption is that 
all single letter frequencies are obliterated, not just for letter "e"):
- cryptanalysis 
    * analysis of letter frequencies (digrams, trigrams, etc.)
"""