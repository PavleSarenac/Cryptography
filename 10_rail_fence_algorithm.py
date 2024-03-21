def encrypt(plain_text, key):
    rails = ["" for _ in range(key)]
    plain_char_index = 0
    while plain_char_index < len(plain_text):
        for i in range(key):
            if plain_char_index >= len(plain_text):
                break
            rails[i] += plain_text[plain_char_index]
            plain_char_index += 1
        for i in range(key - 2, 0, -1):
            if plain_char_index >= len(plain_text):
                break
            rails[i] += plain_text[plain_char_index]
            plain_char_index += 1
    cipher_text = "".join(rails)
    return cipher_text


def decrypt(cipher_text, key):
    number_of_letters_per_rail = get_number_of_letters_per_rail(cipher_text, key)
    original_rails = get_original_rails_before_encryption(cipher_text, number_of_letters_per_rail)
    plain_text = ""
    cipher_char_index = 0
    while cipher_char_index < len(cipher_text):
        for i in range(key):
            if cipher_char_index >= len(cipher_text):
                break
            plain_text += original_rails[i].pop(0)
            cipher_char_index += 1
        for i in range(key - 2, 0, -1):
            if cipher_char_index >= len(cipher_text):
                break
            plain_text += original_rails[i].pop(0)
            cipher_char_index += 1
    return plain_text


def get_number_of_letters_per_rail(cipher_text, key):
    number_of_letters_per_rail = [0 for _ in range(key)]
    cipher_char_index = 0
    while cipher_char_index < len(cipher_text):
        for i in range(key):
            if cipher_char_index >= len(cipher_text):
                break
            number_of_letters_per_rail[i] += 1
            cipher_char_index += 1
        for i in range(key - 2, 0, -1):
            if cipher_char_index >= len(cipher_text):
                break
            number_of_letters_per_rail[i] += 1
            cipher_char_index += 1
    return number_of_letters_per_rail


def get_original_rails_before_encryption(cipher_text, number_of_letters_per_rail):
    original_rails = []
    cipher_char_index = 0
    for i in range(len(number_of_letters_per_rail)):
        rail = []
        for j in range(number_of_letters_per_rail[i]):
            rail.append(cipher_text[cipher_char_index])
            cipher_char_index += 1
        original_rails.append(rail)
    return original_rails


def main():
    key = 3
    cipher_text = encrypt("rail fence cipher is trivial for cryptanalysis", key)
    plain_text = decrypt(cipher_text, key)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- brute-force attack
    * if the number of rails is not large, this cipher can be broken by brute-force attack easily
- cryptanalysis
    * for larger plaintexts and keys this cipher can be broken by analysing letter frequency statistics
"""