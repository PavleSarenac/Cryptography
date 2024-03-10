from monoalfabetska_sifra import monoalphabet_decrypt


def get_key():
    with open("../../tekst/key.txt", "r") as file:
        key = file.read()
    return key


def decrypt(key):
    plain_text = monoalphabet_decrypt(key)
    with open("../../tekst/plain_text.txt", "w") as file:
        file.write("".join(plain_text))


def main():
    key = get_key()
    decrypt(key)


if __name__ == "__main__":
    main()
