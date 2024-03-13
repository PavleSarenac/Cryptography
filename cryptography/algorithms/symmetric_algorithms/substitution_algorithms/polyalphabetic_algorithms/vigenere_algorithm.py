from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os


class VigenereAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_path = os.path.dirname(__file__)
        testing_directory_path = f"../../../../testing/symmetric_algorithms/substitution_algorithms/polyalphabetic_algorithms/vigenere_algorithm"
        self.testing_directory = os.path.join(script_path, testing_directory_path)
        self.plain_text = self.get_plain_text()
        self.cipher_text = self.get_cipher_text()
        self.key = self.get_key()

    def encrypt(self):
        cipher_text = []
        for plain_char, key_char in zip(self.plain_text, self.key):
            if plain_char not in self.english_alphabet:
                cipher_text.append(plain_char)
            else:
                cipher_text.append(self.english_alphabet[(self.english_alphabet.index(plain_char) + self.english_alphabet.index(key_char)) % len(self.english_alphabet)])
        return "".join(cipher_text)

    def decrypt(self):
        plain_text = []
        for cipher_char, key_char in zip(self.cipher_text, self.key):
            if cipher_char not in self.english_alphabet:
                plain_text.append(cipher_char)
            else:
                plain_text.append(self.english_alphabet[(self.english_alphabet.index(cipher_char) - self.english_alphabet.index(key_char)) % len(self.english_alphabet)])
        return "".join(plain_text)

    def get_key(self):
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            initial_key = file.read().strip().lower()
        final_key = ""
        for char_index in range(len(self.plain_text)):
            final_key += initial_key[char_index % len(initial_key)]
        final_key = final_key.lower()
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(final_key)
        return final_key
