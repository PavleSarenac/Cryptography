from algorithms.cryptographic_algorithm import CryptographicAlgorithm
import os


class CesarAlgorithm(CryptographicAlgorithm):
    def __init__(self):
        super().__init__()
        script_path = os.path.dirname(__file__)
        testing_directory_path = f"../../../testing/symmetric_algorithms/supstitution_algorithms/cesar_algorithm"
        self.testing_directory = os.path.join(script_path, testing_directory_path)
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

    def brute_force_attack(self):
        brute_force_attack_output = []
        for key in range(1, 26):
            self.key = key
            brute_force_attack_output.append(f"key: {key}; plain_text: {self.decrypt()};" + "\n")
        brute_force_attack_output = "".join(brute_force_attack_output)
        return brute_force_attack_output

    def get_key(self):
        file_path = os.path.join(self.testing_directory, "key.txt")
        with open(file_path, "r") as file:
            key = file.read()
        return int(key)

    def get_brute_force_attack_output(self):
        file_path = os.path.join(self.testing_directory, "brute_force_attack_output.txt")
        with open(file_path, "r") as file:
            brute_force_attack_output = file.read()
        return brute_force_attack_output.lower()

    def set_brute_force_attack_output(self, brute_force_attack_output):
        file_path = os.path.join(self.testing_directory, "brute_force_attack_output.txt")
        with open(file_path, "w") as file:
            file.write(brute_force_attack_output)
