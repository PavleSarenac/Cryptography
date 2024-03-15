from abc import ABC, abstractmethod
import os


class CryptographicAlgorithm(ABC):
    def __init__(self):
        self.english_alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        self.extended_english_alphabet = self.english_alphabet + [chr(i) for i in range(ord("A"), ord("A") + 6)]
        self.serbian_cyrillic_alphabet = list("абвгдђежзијклљмнњопрстћуфхцчџш")
        self.plain_text = None
        self.cipher_text = None
        self.testing_directory = None

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass

    @abstractmethod
    def get_key(self):
        pass

    def get_plain_text(self):
        file_path = os.path.join(self.testing_directory, "plain_text.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            plain_text = file.read()
        return plain_text.lower()

    def get_cipher_text(self):
        file_path = os.path.join(self.testing_directory, "cipher_text.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            cipher_text = file.read()
        return cipher_text.lower()

    def set_plain_text(self, plain_text):
        self.plain_text = plain_text.lower()
        file_path = os.path.join(self.testing_directory, "plain_text.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.plain_text)

    def set_cipher_text(self, cipher_text):
        self.cipher_text = cipher_text.lower()
        file_path = os.path.join(self.testing_directory, "cipher_text.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.cipher_text)
