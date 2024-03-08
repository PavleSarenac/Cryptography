from cezarova_sifra import cesar_decrypt


def main():
    plain_text = cesar_decrypt(3)
    with open("../text/plain_text.txt", "w") as file:
        file.write("".join(plain_text))


if __name__ == "__main__":
    main()
