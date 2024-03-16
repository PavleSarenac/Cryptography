from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os


class RailFenceAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_path = os.path.dirname(__file__)
        testing_directory_path = f"../../../testing/symmetric_algorithms/transposition_algorithms/rail_fence_algorithm"
        self.testing_directory = os.path.join(script_path, testing_directory_path)
        self.plain_text = self.get_plain_text()
        self.cipher_text = self.get_cipher_text()
        self.key = self.get_key()

    def encrypt(self):
        cipher_text = [[] for _ in range(self.key)]
        plain_char_index = 0
        while plain_char_index < len(self.plain_text):
            for i in range(self.key):
                if plain_char_index >= len(self.plain_text):
                    break
                cipher_text[i].append(self.plain_text[plain_char_index])
                plain_char_index += 1
            for i in range(self.key - 2, 0, -1):
                if plain_char_index >= len(self.plain_text):
                    break
                cipher_text[i].append(self.plain_text[plain_char_index])
                plain_char_index += 1
        return "".join("".join(row) for row in cipher_text)

    def decrypt(self):
        plain_text = ""
        original_rows = self.get_original_rows_used_for_encryption()
        cipher_char_index = 0
        while cipher_char_index < len(self.cipher_text):
            for i in range(self.key):
                if cipher_char_index >= len(self.cipher_text):
                    break
                plain_text += original_rows[i].pop(0)
                cipher_char_index += 1
            for i in range(self.key - 2, 0, -1):
                if cipher_char_index >= len(self.plain_text):
                    break
                plain_text += original_rows[i].pop(0)
                cipher_char_index += 1
        return plain_text

    def get_key(self):
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            key = int(file.read())
        return key

    def get_original_rows_used_for_encryption(self):
        original_rows = [[] for _ in range(self.key)]
        row_letter_counters = self.get_row_letter_counters()
        cipher_char_index = 0
        for row_index, row_letter_counter in row_letter_counters.items():
            for _ in range(row_letter_counter):
                original_rows[row_index].append(self.cipher_text[cipher_char_index])
                cipher_char_index += 1
        return original_rows

    def get_row_letter_counters(self):
        row_letter_counters = {row_index: 0 for row_index in range(self.key)}
        cipher_char_index = 0
        while cipher_char_index < len(self.cipher_text):
            for i in range(self.key):
                if cipher_char_index >= len(self.cipher_text):
                    break
                row_letter_counters[i] += 1
                cipher_char_index += 1
            for i in range(self.key - 2, 0, -1):
                if cipher_char_index >= len(self.plain_text):
                    break
                row_letter_counters[i] += 1
                cipher_char_index += 1
        return row_letter_counters
