alphabet_lowercase = [chr(i) for i in range(ord("a"), ord("z") + 1)]
plain_to_cipher_lowercase_letters = dict()
cipher_to_plain_lowercase_letters = dict()

alphabet_uppercase = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
plain_to_cipher_uppercase_letters = dict()
cipher_to_plain_uppercase_letters = dict()

known_letter_frequency = {
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

    return "".join(plain_text)


def monoalphabet_cryptoanalysis_decrypt():
    with open("../text/cryptoanalysis_cipher_text.txt", "r") as file:
        cipher_text = file.read().lower()

    calculated_letter_frequency = {char: 0.00 for char in alphabet_lowercase}
    total_number_of_letters = 0
    for char in cipher_text:
        if char not in alphabet_lowercase:
            continue
        calculated_letter_frequency[char] += 1
        total_number_of_letters += 1
    for char in calculated_letter_frequency.keys():
        calculated_letter_frequency[char] \
            = round((calculated_letter_frequency[char] / total_number_of_letters) * 100, 3)

    with open("../text/cryptoanalysis_results.txt", "w") as file:
        file.write("Known english letter frequency:\n")
        for letter, frequency in sorted(known_letter_frequency.items(), key=lambda item: item[1], reverse=True):
            file.write(f"{letter}: {frequency};\n")
        file.write("\nCalculated cipher text letter frequency:\n")
        for letter, frequency in sorted(calculated_letter_frequency.items(), key=lambda item: item[1], reverse=True):
            file.write(f"{letter}: {frequency};\n")


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
