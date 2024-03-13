from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os
import random


class MonoalphabeticAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_path = os.path.dirname(__file__)
        testing_directory_path = f"../../../../testing/symmetric_algorithms/substitution_algorithms/monoalphabetic_algorithms/monoalphabetic_algorithm"
        self.testing_directory = os.path.join(script_path, testing_directory_path)
        self.key = self.get_key()
        self.plain_text = self.get_plain_text()
        self.cipher_text = self.get_cipher_text()
        self.plain_to_cipher = self.get_plain_to_cipher_mappings()
        self.cipher_to_plain = self.get_cipher_to_plain_mappings()
        self.english_char_frequency = {
            "a": 8.167,
            "b": 1.492,
            "c": 2.782,
            "d": 4.253,
            "e": 12.702,
            "f": 2.228,
            "g": 2.015,
            "h": 6.094,
            "i": 6.996,
            "j": 0.153,
            "k": 0.772,
            "l": 4.025,
            "m": 2.406,
            "n": 6.749,
            "o": 7.507,
            "p": 1.929,
            "q": 0.095,
            "r": 5.987,
            "s": 6.327,
            "t": 9.056,
            "u": 2.758,
            "v": 0.978,
            "w": 2.360,
            "x": 0.150,
            "y": 1.974,
            "z": 0.074
        }

    def encrypt(self):
        cipher_text = []
        for char in self.plain_text:
            if char not in self.english_alphabet:
                cipher_text.append(char)
            else:
                cipher_text.append(self.plain_to_cipher[char])
        return "".join(cipher_text)

    def decrypt(self):
        plain_text = []
        for char in self.cipher_text:
            if char not in self.english_alphabet:
                plain_text.append(char)
            else:
                plain_text.append(self.cipher_to_plain[char])
        return "".join(plain_text)

    def cryptanalysis(self):
        cipher_text = self.get_cryptanalysis_cipher_text()
        calculated_char_frequency = {char: 0.0 for char in self.english_alphabet}
        total_number_of_chars = 0

        for char in cipher_text:
            if char in self.english_alphabet:
                calculated_char_frequency[char] += 1
                total_number_of_chars += 1

        for char in calculated_char_frequency.keys():
            calculated_char_frequency[char] \
                = round((calculated_char_frequency[char] / total_number_of_chars) * 100, 3)

        english_char_frequency_text = ["Known english char frequency:\n"]
        for char, frequency in sorted(self.english_char_frequency.items(), key=lambda item: item[1], reverse=True):
            english_char_frequency_text.append(f"{char}: {frequency};\n")

        calculated_char_frequency_text = ["\nCalculated cipher text char frequency:\n"]
        for char, frequency in sorted(calculated_char_frequency.items(), key=lambda item: item[1], reverse=True):
            calculated_char_frequency_text.append(f"{char}: {frequency};\n")

        file_path = os.path.join(self.testing_directory, "cryptanalysis/cryptanalysis_results.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("".join(english_char_frequency_text + calculated_char_frequency_text))

    def get_key(self):
        key = "".join(random.sample(self.english_alphabet, len(self.english_alphabet))).lower()
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(key)
        return key

    def get_plain_to_cipher_mappings(self):
        current_char_ascii_index = ord("a")
        plain_to_cipher = dict()
        for char in self.key:
            plain_to_cipher[chr(current_char_ascii_index)] = char
            current_char_ascii_index += 1
        return plain_to_cipher

    def get_cipher_to_plain_mappings(self):
        current_char_ascii_index = ord("a")
        cipher_to_plain = dict()
        for char in self.key:
            cipher_to_plain[char] = chr(current_char_ascii_index)
            current_char_ascii_index += 1
        return cipher_to_plain

    def get_cryptanalysis_cipher_text(self):
        file_path = os.path.join(self.testing_directory, "cryptanalysis/cryptanalysis_cipher_text.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            cipher_text = file.read().lower()
        return cipher_text
