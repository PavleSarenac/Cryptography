alphabet_lowercase = [chr(i) for i in range(ord("a"), ord("z") + 1)]
alphabet_uppercase = [chr(i) for i in range(ord("A"), ord("Z") + 1)]


def cesar_encrypt(key):
    with open("../text/plain_text.txt", "r") as file:
        plain_text = file.read()

    cipher_text = []
    for char in plain_text:
        if (not is_lowercase(char)) and (not is_uppercase(char)):
            cipher_text.append(char)
        elif is_lowercase(char):
            cipher_text.append(alphabet_lowercase[(alphabet_lowercase.index(char) + key) % 26])
        elif is_uppercase(char):
            cipher_text.append(alphabet_uppercase[(alphabet_uppercase.index(char) + key) % 26])
        else:
            cipher_text.append("?")

    return "".join(cipher_text)


def cesar_decrypt(key):
    with open("../text/cipher_text.txt", "r") as file:
        cipher_text = file.read()

    plain_text = []
    for char in cipher_text:
        if (not is_lowercase(char)) and (not is_uppercase(char)):
            plain_text.append(char)
        elif is_lowercase(char):
            plain_text.append(alphabet_lowercase[(alphabet_lowercase.index(char) - key) % 26])
        elif is_uppercase(char):
            plain_text.append(alphabet_uppercase[(alphabet_uppercase.index(char) - key) % 26])
        else:
            plain_text.append("?")

    return "".join(plain_text)


def cesar_brute_force_attack():
    with open("../text/brute_force_attack_output.txt", "w") as file:
        for key in range(1, 26):
            file.write(f"key: {key}; plain_text: {cesar_decrypt(key)};" + "\n")


def is_uppercase(char):
    return char in alphabet_uppercase


def is_lowercase(char):
    return char in alphabet_lowercase
