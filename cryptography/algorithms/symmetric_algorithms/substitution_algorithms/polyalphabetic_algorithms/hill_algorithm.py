from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os
import numpy as np


class HillAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_path = os.path.dirname(__file__)
        testing_directory_path = f"../../../../testing/symmetric_algorithms/substitution_algorithms/polyalphabetic_algorithms/hill_algorithm"
        self.testing_directory = os.path.join(script_path, testing_directory_path)
        self.key = self.get_key()
        self.plain_text = self.get_plain_text()
        self.plain_text_char_indexes = [self.english_alphabet.index(char) for char in self.plain_text]
        self.cipher_text = self.get_cipher_text()

    def encrypt(self):
        cipher_text = []
        for i in range(0, len(self.plain_text_char_indexes), 3):
            plain_text_char_indexes_matrix = np.array([
                self.plain_text_char_indexes[i],
                self.plain_text_char_indexes[i + 1],
                self.plain_text_char_indexes[i + 2]
            ]).reshape(1, 3)
            cipher_text_char_indexes_matrix = [char_index % 26 for char_index in np.matmul(plain_text_char_indexes_matrix, self.key)[0]]
            cipher_text += [self.english_alphabet[char_index] for char_index in cipher_text_char_indexes_matrix]
        return "".join(cipher_text)

    def decrypt(self):
        plain_text = []
        return "".join(plain_text)

    def get_key(self):
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            key = [int(matrix_element) for matrix_element in file.read().split(",")]
        return np.array(key).reshape(3, 3)
