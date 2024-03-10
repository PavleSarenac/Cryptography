from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os
import random


class MonoalphabetAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_directory = os.path.dirname(__file__)
        self.testing_directory = os.path.join(script_directory, "../../../testing/symmetric_algorithms/supstitution_algorithms/monoalphabet_algorithm")
        self.alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        self.key = self.get_key()
        self.plain_text = self.get_plain_text()
        self.cipher_text = self.get_cipher_text()

    def encrypt(self):
        cipher_text = []
        for char in self.plain_text:
            if char not in self.alphabet:
                cipher_text.append(char)
            else:
                cipher_text.append(self.alphabet[(self.alphabet.index(char) + self.key) % len(self.alphabet)])
        return "".join(cipher_text)

    def decrypt(self):
        plain_text = []
        for char in self.cipher_text:
            if char not in self.alphabet:
                plain_text.append(char)
            else:
                plain_text.append(self.alphabet[(self.alphabet.index(char) - self.key) % len(self.alphabet)])
        return "".join(plain_text)

    def get_key(self):
        key = "".join(random.sample(alphabet_uppercase, len(alphabet_uppercase)))
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "r") as file:
            key = file.read()
        return int(key)
