from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os
import numpy as np
import sympy as sy
import scipy


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
        determinant = int(scipy.linalg.det(self.key)) % len(self.english_alphabet)
        inverse_determinant = pow(determinant, -1, len(self.english_alphabet))
        adjoint_matrix = self.get_adjoint_matrix_numpy_and_scipy()
        inverse_matrix = (inverse_determinant * adjoint_matrix) % 26
        return inverse_matrix

    def get_adjoint_matrix_numpy_and_scipy(self):
        cofactors_matrix = np.empty_like(self.key, int)
        for i in range(self.key.shape[0]):
            for j in range(self.key.shape[1]):
                submatrix = np.delete(np.delete(self.key, i, 0), j, 1)
                minor = int(scipy.linalg.det(submatrix))
                cofactor = pow(-1, i + j) * minor
                cofactors_matrix[i, j] = cofactor
        adjoint_matrix = cofactors_matrix.transpose()
        return adjoint_matrix

    def get_adjoint_matrix_sympy(self):
        return sy.matrix2numpy(sy.matrices.matrices.MatrixDeterminant.adjugate(sy.Matrix(self.key)))
