import numpy as np


alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def encrypt(plain_text, key_matrix):
    cipher_text = ""
    reformatted_plain_text = reformat_plain_text(plain_text)
    for plain_char_index in range(0, len(reformatted_plain_text), 2):
        char1 = reformatted_plain_text[plain_char_index]
        char1_coordinates = np.where(key_matrix == char1)
        char1_row = char1_coordinates[0][0]
        char1_column = char1_coordinates[1][0]

        char2 = reformatted_plain_text[plain_char_index + 1]
        char2_coordinates = np.where(key_matrix == char2)
        char2_row = char2_coordinates[0][0]
        char2_column = char2_coordinates[1][0]

        if char1_row == char2_row:
            new_char1 = key_matrix[char1_row, (char1_column + 1) % key_matrix.shape[0]]
            new_char2 = key_matrix[char2_row, (char2_column + 1) % key_matrix.shape[0]]
        elif char1_column == char2_column:
            new_char1 = key_matrix[(char1_row + 1) % key_matrix.shape[0], char1_column]
            new_char2 = key_matrix[(char2_row + 1) % key_matrix.shape[0], char2_column]
        else:
            new_char1 = key_matrix[char1_row, char2_column]
            new_char2 = key_matrix[char2_row, char1_column]

        cipher_text += f"{new_char1}{new_char2}"
    return cipher_text


def decrypt(cipher_text, key_matrix):
    plain_text = ""
    for cipher_char_index in range(0, len(cipher_text), 2):
        char1 = cipher_text[cipher_char_index]
        char1_coordinates = np.where(key_matrix == char1)
        char1_row = char1_coordinates[0][0]
        char1_column = char1_coordinates[1][0]

        char2 = cipher_text[cipher_char_index + 1]
        char2_coordinates = np.where(key_matrix == char2)
        char2_row = char2_coordinates[0][0]
        char2_column = char2_coordinates[1][0]

        if char1_row == char2_row:
            new_char1 = key_matrix[char1_row, (char1_column - 1) % key_matrix.shape[0]]
            new_char2 = key_matrix[char2_row, (char2_column - 1) % key_matrix.shape[0]]
        elif char1_column == char2_column:
            new_char1 = key_matrix[(char1_row - 1) % key_matrix.shape[0], char1_column]
            new_char2 = key_matrix[(char2_row - 1) % key_matrix.shape[0], char2_column]
        else:
            new_char1 = key_matrix[char1_row, char2_column]
            new_char2 = key_matrix[char2_row, char1_column]

        plain_text += f"{new_char1}{new_char2}"
    return plain_text


def reformat_plain_text(plain_text):
    reformatted_plain_text = ""
    plain_char_index = 0
    plain_text = plain_text.replace("j", "i")
    while plain_char_index < len(plain_text) - 1:
        if plain_text[plain_char_index] != plain_text[plain_char_index + 1]:
            reformatted_plain_text += f"{plain_text[plain_char_index]}{plain_text[plain_char_index + 1]}"
            plain_char_index += 2
        else:
            reformatted_plain_text += f"{plain_text[plain_char_index]}x"
            plain_char_index += 1
    if reformatted_plain_text[-1] != plain_text[-1]:
        reformatted_plain_text += f"{plain_text[-1]}x"
    return reformatted_plain_text


def create_key_matrix(key_word):
    matrix_elements = []
    key_word = key_word.replace("j", "i")
    for key_char in key_word:
        if key_char not in matrix_elements:
            matrix_elements.append(key_char)
    for char in alphabet:
        if char not in matrix_elements and char != "j":
            matrix_elements.append(char)
    return np.array(matrix_elements).reshape(5, 5)


def main():
    key_word = "monarchy"
    key_matrix = create_key_matrix(key_word)
    cipher_text = encrypt("balloon", key_matrix)
    plain_text = decrypt(cipher_text, key_matrix)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- cryptanalysis 
    * analysis of letter frequencies (digrams, trigrams, etc.)
"""