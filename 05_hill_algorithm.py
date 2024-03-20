import numpy as np
import scipy


alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def encrypt(plain_text, key_matrix):
    cipher_text = ""
    while len(plain_text) % key_matrix.shape[0] != 0:
        plain_text += "x"
    for plain_char_index in range(0, len(plain_text), 3):
        plain_subtext_matrix = np.array([
            alphabet.index(plain_text[plain_char_index]),
            alphabet.index(plain_text[plain_char_index + 1]),
            alphabet.index(plain_text[plain_char_index + 2])
        ]).reshape(1, 3)
        cipher_subtext_matrix = np.matmul(plain_subtext_matrix, key_matrix) % len(alphabet)
        for cipher_char_index in cipher_subtext_matrix[0, :]:
            cipher_text += alphabet[cipher_char_index]
    return cipher_text


def decrypt(cipher_text, inverse_key_matrix):
    plain_text = ""
    for cipher_char_index in range(0, len(cipher_text), 3):
        cipher_subtext_matrix = np.array([
            alphabet.index(cipher_text[cipher_char_index]),
            alphabet.index(cipher_text[cipher_char_index + 1]),
            alphabet.index(cipher_text[cipher_char_index + 2])
        ]).reshape(1, 3)
        plain_subtext_matrix = np.matmul(cipher_subtext_matrix, inverse_key_matrix) % len(alphabet)
        for plain_char_index in plain_subtext_matrix[0, :]:
            plain_text += alphabet[plain_char_index]
    return plain_text


def get_inverse_key_matrix(key_matrix):
    determinant = int(scipy.linalg.det(key_matrix)) % len(alphabet)
    inverse_determinant = pow(determinant, -1, len(alphabet))
    minors_matrix = np.empty_like(key_matrix, np.int64)
    for i in range(key_matrix.shape[0]):
        for j in range(key_matrix.shape[1]):
            submatrix = np.delete(np.delete(key_matrix, i, 0), j, 1)
            minors_matrix[i, j] = int(scipy.linalg.det(submatrix)) % len(alphabet)
    cofactors_matrix = np.empty_like(key_matrix, np.int64)
    for i in range(key_matrix.shape[0]):
        for j in range(key_matrix.shape[1]):
            cofactors_matrix[i, j] = (pow(-1, i + j) * minors_matrix[i, j]) % len(alphabet)
    adjoint_matrix = cofactors_matrix.transpose()
    inverse_key_matrix = (inverse_determinant * adjoint_matrix) % len(alphabet)
    return inverse_key_matrix


def main():
    key_matrix = np.array([3, 25, 4, 23, 6, 15, 13, 17, 21]).reshape(3, 3)
    inverse_key_matrix = get_inverse_key_matrix(key_matrix)
    cipher_text = encrypt("youhavetolearnhillcipher", key_matrix)
    plain_text = decrypt(cipher_text, inverse_key_matrix)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches (assumption is that 
all single letter frequencies are obliterated, not just for letter "e"):
- cryptanalysis 
    * analysis of letter frequencies (trigrams)
    * known plaintext attack - for MxM Hill algorithm key matrix, if cryptanalyst knows M plaintext-ciphertext
    pairs each of length M, then he can find out what the key matrix is by solving a system of linear equations
"""