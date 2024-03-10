import random
from monoalfabetska_sifra import monoalphabet_encrypt
from monoalfabetska_sifra import alphabet_uppercase


def generate_key():
    key = "".join(random.sample(alphabet_uppercase, len(alphabet_uppercase)))
    with open("../../tekst/key.txt", "w") as file:
        file.write(key)
    return key


def encrypt(key):
    cipher_text = monoalphabet_encrypt(key)
    with open("../../tekst/cipher_text.txt", "w") as file:
        file.write("".join(cipher_text))


def main():
    key = generate_key()
    encrypt(key)


if __name__ == "__main__":
    main()
