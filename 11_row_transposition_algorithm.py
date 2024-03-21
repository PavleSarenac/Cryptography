import numpy as np


def encrypt(plain_text, key):
    reformatted_plain_text = list(reformat_plain_text(plain_text, key))
    plain_text_matrix = np.array(reformatted_plain_text).reshape(len(reformatted_plain_text) // len(key), len(key))
    cipher_text = ""
    for i in range(len(key)):
        cipher_text += "".join(plain_text_matrix[:, key[i]])
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    original_columns = ["" for _ in range(len(key))]
    cipher_char_index = 0
    for i in range(len(key)):
        for _ in range(len(cipher_text) // len(key)):
            original_columns[key[i]] += cipher_text[cipher_char_index]
            cipher_char_index += 1
    for row_index in range(len(cipher_text) // len(key)):
        for column_index in range(len(key)):
            plain_text += original_columns[column_index][row_index]
    return "".join(plain_text)


def reformat_plain_text(plain_text, key):
    while len(plain_text) % len(key) != 0:
        plain_text += "x"
    return plain_text


def main():
    key = [5, 4, 3, 6, 1, 2, 0, 7]
    cipher_text = encrypt("row transposition applied only once is not very safe, but multiple times is better", key)
    plain_text = decrypt(cipher_text, key)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- brute-force attack
    * if the key is not large, this cipher can be broken by brute-force attack easily
- cryptanalysis
    * for larger plaintexts and keys this cipher can be broken by analysing letter frequency statistics
    
Multiple transpositions improve security drastically because that way cipher text becomes less structured, and less
prone to cryptanalysis attacks that way
"""