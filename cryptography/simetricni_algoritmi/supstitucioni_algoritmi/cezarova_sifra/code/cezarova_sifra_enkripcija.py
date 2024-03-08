from cezarova_sifra import cesar_encrypt


def main():
    cipher_text = cesar_encrypt(3)
    with open("../text/cipher_text.txt", "w") as file:
        file.write("".join(cipher_text))


if __name__ == "__main__":
    main()
