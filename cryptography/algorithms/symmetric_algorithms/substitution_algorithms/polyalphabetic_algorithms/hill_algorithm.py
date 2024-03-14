from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os
import numpy as np
import sympy as sy


class HillAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_path = os.path.dirname(__file__)
        testing_directory_path = f"../../../../testing/symmetric_algorithms/substitution_algorithms/polyalphabetic_algorithms/hill_algorithm"
        self.testing_directory = os.path.join(script_path, testing_directory_path)
        self.key = self.get_key()
        self.inverse_key_matrix = self.get_inverse_key_matrix()
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
            cipher_text_char_indexes_matrix = [char_index % len(self.english_alphabet) for char_index in np.matmul(plain_text_char_indexes_matrix, self.key)[0, :]]
            cipher_text += [self.english_alphabet[char_index] for char_index in cipher_text_char_indexes_matrix]
        return "".join(cipher_text)

    def decrypt(self):
        plain_text = []
        cipher_text_char_indexes = [self.english_alphabet.index(char) for char in self.cipher_text]
        for i in range(0, len(cipher_text_char_indexes), 3):
            cipher_text_char_indexes_matrix = np.array([
                cipher_text_char_indexes[i],
                cipher_text_char_indexes[i + 1],
                cipher_text_char_indexes[i + 2]
            ]).reshape(1, 3)
            plain_text_char_indexes_matrix = [char_index % len(self.english_alphabet) for char_index in np.matmul(cipher_text_char_indexes_matrix, self.inverse_key_matrix)[0, :]]
            plain_text += [self.english_alphabet[char_index] for char_index in plain_text_char_indexes_matrix]
        return "".join(plain_text)

    def get_key(self):
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            key = [int(matrix_element) for matrix_element in file.read().split(",")]
        return np.array(key).reshape(3, 3)

    def get_inverse_key_matrix(self):
        determinant = int(np.linalg.det(self.key)) % len(self.english_alphabet)
        inverse_determinant = pow(determinant, -1, len(self.english_alphabet))
        adjoint_matrix = sy.matrix2numpy(sy.matrices.matrices.MatrixDeterminant.adjugate(sy.Matrix(self.key)))
        inverse_matrix = (inverse_determinant * adjoint_matrix) % 26
        return inverse_matrix
