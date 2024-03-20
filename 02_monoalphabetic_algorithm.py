import random


alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
key = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def encrypt(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char not in alphabet:
            cipher_text += char
        else:
            cipher_text += key[alphabet.index(char)]
    return cipher_text


def decrypt(cipher_text):
    plain_text = ""
    for char in cipher_text:
        if char not in alphabet:
            plain_text += char
        else:
            plain_text += alphabet[key.index(char)]
    return plain_text


def main():
    random.shuffle(key)
    cipher_text = encrypt("napad je u podne")
    plain_text = decrypt(cipher_text)
    print(plain_text)
    print(cipher_text.upper())


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- cryptanalysis 
    * analysis of letter frequencies (single letters, digrams, trigrams, etc.)
"""