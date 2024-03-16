from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os
import numpy as np


class RowTranspositionAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_path = os.path.dirname(__file__)
        testing_directory_path = f"../../../testing/symmetric_algorithms/transposition_algorithms/row_transposition_algorithm"
        self.testing_directory = os.path.join(script_path, testing_directory_path)
        self.invalid_char = "ш"
        self.key = self.get_key()
        self.plain_text = self.get_plain_text()
        self.cipher_text = self.get_cipher_text()

    def encrypt(self):
        cipher_text = ["" for _ in range(len(self.key))]
        matrix = np.array(list(self.plain_text)).reshape(len(self.plain_text) // len(self.key), len(self.key))
        new_column_indexes = [int(column_index) for column_index in list(self.key)]
        for old_column_index, new_column_index in enumerate(new_column_indexes):
            for char in matrix[:, old_column_index]:
                cipher_text[new_column_index] += char
        return "".join(cipher_text)

    def decrypt(self):
        number_of_rows = len(self.plain_text) // len(self.key)
        plain_text = ["" for _ in range(number_of_rows)]
        new_column_indexes = [int(column_index) for column_index in list(self.key)]
        for old_column_index, new_column_index in enumerate(new_column_indexes):
            current_row = 0
            for char_index in range(new_column_index * number_of_rows, new_column_index * number_of_rows + number_of_rows):
                if self.cipher_text[char_index] != self.invalid_char:
                    plain_text[current_row] += self.cipher_text[char_index]
                current_row += 1
        return "".join(plain_text)

    def get_key(self):
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            key = file.read()
        return key

    def get_plain_text(self):
        file_path = os.path.join(self.testing_directory, "plain_text.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            plain_text = file.read()
        if len(plain_text) % len(self.key) != 0:
            for _ in range(len(self.key) - (len(plain_text) % len(self.key))):
                plain_text += self.invalid_char
        return plain_text.lower()
