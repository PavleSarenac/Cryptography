from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os
import numpy as np


class PlayfairAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_path = os.path.dirname(__file__)
        testing_directory_path = f"../../../../testing/symmetric_algorithms/substitution_algorithms/polyalphabetic_algorithms/playfair_algorithm"
        self.testing_directory = os.path.join(script_path, testing_directory_path)
        self.key = self.get_key()
        self.plain_text = self.get_plain_text()
        self.reformat_plain_text()
        self.cipher_text = self.get_cipher_text()
        self.key_based_matrix = self.create_key_based_matrix()

    def encrypt(self):
        cipher_text = []
        for char_index in range(0, len(self.plain_text), 2):
            char_1_coordinates = np.where(self.key_based_matrix == self.plain_text[char_index])
            char_1_row = char_1_coordinates[0][0]
            char_1_column = char_1_coordinates[1][0]

            char_2_coordinates = np.where(self.key_based_matrix == self.plain_text[char_index + 1])
            char_2_row = char_2_coordinates[0][0]
            char_2_column = char_2_coordinates[1][0]

            if char_1_row == char_2_row:
                cipher_text.append(str(self.key_based_matrix[char_1_row, (char_1_column + 1) % 5]))
                cipher_text.append(str(self.key_based_matrix[char_2_row, (char_2_column + 1) % 5]))
            elif char_1_column == char_2_column:
                cipher_text.append(str(self.key_based_matrix[(char_1_row + 1) % 5, char_1_column]))
                cipher_text.append(str(self.key_based_matrix[(char_2_row + 1) % 5, char_2_column]))
            else:
                cipher_text.append(str(self.key_based_matrix[char_1_row, char_2_column]))
                cipher_text.append(str(self.key_based_matrix[char_2_row, char_1_column]))
        return "".join(cipher_text)

    def decrypt(self):
        plain_text = []
        for char_index in range(0, len(self.cipher_text), 2):
            char_1_coordinates = np.where(self.key_based_matrix == self.cipher_text[char_index])
            char_1_row = char_1_coordinates[0][0]
            char_1_column = char_1_coordinates[1][0]

            char_2_coordinates = np.where(self.key_based_matrix == self.cipher_text[char_index + 1])
            char_2_row = char_2_coordinates[0][0]
            char_2_column = char_2_coordinates[1][0]

            if char_1_row == char_2_row:
                plain_text.append(str(self.key_based_matrix[char_1_row, (char_1_column - 1) % 5]))
                plain_text.append(str(self.key_based_matrix[char_2_row, (char_2_column - 1) % 5]))
            elif char_1_column == char_2_column:
                plain_text.append(str(self.key_based_matrix[(char_1_row - 1) % 5, char_1_column]))
                plain_text.append(str(self.key_based_matrix[(char_2_row - 1) % 5, char_2_column]))
            else:
                plain_text.append(str(self.key_based_matrix[char_1_row, char_2_column]))
                plain_text.append(str(self.key_based_matrix[char_2_row, char_1_column]))
        return "".join(plain_text)

    def get_key(self):
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            key = file.read().strip().lower()
        return key

    def reformat_plain_text(self):
        if len(self.plain_text) == 0:
            return

        reformatted_plain_text = []
        char_index = 0
        while char_index < len(self.plain_text) - 1:
            current_char = self.plain_text[char_index]
            next_char = self.plain_text[char_index + 1]
            if current_char != next_char:
                reformatted_plain_text += [current_char, next_char]
                char_index += 2
            else:
                reformatted_plain_text += [current_char, "x"]
                char_index += 1
        if reformatted_plain_text[-1] != self.plain_text[-1]:
            reformatted_plain_text += [self.plain_text[-1], "x"]

        self.plain_text = "".join(reformatted_plain_text)

    def create_key_based_matrix(self):
        matrix_elements = []
        for char in self.key:
            if char not in matrix_elements:
                matrix_elements.append(char)
        matrix_elements += [char for char in self.english_alphabet if char not in self.key and char != "j"]
        return np.array(matrix_elements).reshape(5, 5)
