alphabet_lowercase = [chr(i) for i in range(ord("a"), ord("z") + 1)]
plain_to_cipher_lowercase_letters = dict()
cipher_to_plain_lowercase_letters = dict()

alphabet_uppercase = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
plain_to_cipher_uppercase_letters = dict()
cipher_to_plain_uppercase_letters = dict()


def monoalphabet_encrypt(key):
    with open("../text/plain_text.txt", "r") as file:
        plain_text = file.read()

    create_plain_to_cipher_mappings(key)

    cipher_text = []
    for char in plain_text:
        if (not is_lowercase(char)) and (not is_uppercase(char)):
            cipher_text.append(char)
        elif is_lowercase(char):
            cipher_text.append(plain_to_cipher_lowercase_letters[char])
        elif is_uppercase(char):
            cipher_text.append(plain_to_cipher_uppercase_letters[char])
        else:
            cipher_text.append("?")

    return "".join(cipher_text)


def monoalphabet_decrypt(key):
    with open("../text/cipher_text.txt", "r") as file:
        cipher_text = file.read()

    create_cipher_to_plain_mappings(key)

    plain_text = []
    for char in cipher_text:
        if (not is_lowercase(char)) and (not is_uppercase(char)):
            plain_text.append(char)
        elif is_lowercase(char):
            plain_text.append(cipher_to_plain_lowercase_letters[char])
        elif is_uppercase(char):
            plain_text.append(cipher_to_plain_uppercase_letters[char])
        else:
            plain_text.append("?")

    return "".join(plain_text)


def create_plain_to_cipher_mappings(key):
    create_plain_to_cipher_lowercase_mappings(key.lower())
    create_plain_to_cipher_uppercase_mappings(key.upper())


def create_plain_to_cipher_lowercase_mappings(key):
    current_letter_ascii_index = ord("a")
    for char in key:
        plain_to_cipher_lowercase_letters[chr(current_letter_ascii_index)] = char
        current_letter_ascii_index += 1


def create_plain_to_cipher_uppercase_mappings(key):
    current_letter_ascii_index = ord("A")
    for char in key:
        plain_to_cipher_uppercase_letters[chr(current_letter_ascii_index)] = char
        current_letter_ascii_index += 1


def create_cipher_to_plain_mappings(key):
    create_cipher_to_plain_lowercase_mappings(key.lower())
    create_cipher_to_plain_uppercase_mappings(key.upper())


def create_cipher_to_plain_lowercase_mappings(key):
    current_letter_ascii_index = ord("a")
    for char in key:
        cipher_to_plain_lowercase_letters[char] = chr(current_letter_ascii_index)
        current_letter_ascii_index += 1


def create_cipher_to_plain_uppercase_mappings(key):
    current_letter_ascii_index = ord("A")
    for char in key:
        cipher_to_plain_uppercase_letters[char] = chr(current_letter_ascii_index)
        current_letter_ascii_index += 1


def is_uppercase(char):
    return char in alphabet_uppercase


def is_lowercase(char):
    return char in alphabet_lowercase
