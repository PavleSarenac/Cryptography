alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
alphabet_indexes = [i for i in range(len(alphabet))]

first_rotor_list_1 = [24, 5, 15, 18, 21, 6, 2, 25, 1, 4, 26, 13, 23, 3, 20, 9, 11, 7, 12, 22, 8, 17, 10, 19, 14, 16]
first_rotor_list_2 = [26, 10, 15, 5, 13, 23, 1, 19, 25, 3, 17, 2, 8, 24, 11, 4, 22, 16, 6, 21, 14, 20, 7, 18, 9, 12]

second_rotor_list_1 = [5, 16, 24, 12, 4, 19, 3, 18, 26, 1, 7, 14, 23, 25, 17, 9, 2, 6, 15, 22, 21, 13, 8, 10, 20, 11]
second_rotor_list_2 = [1, 26, 18, 19, 11, 2, 23, 5, 12, 25, 14, 3, 7, 13, 20, 24, 16, 4, 21, 6, 15, 8, 22, 10, 17, 9]

third_rotor_list_1 = [9, 14, 22, 16, 20, 21, 1, 7, 12, 26, 17, 13, 2, 3, 8, 15, 25, 23, 18, 4, 11, 5, 10, 19, 6, 24]
third_rotor_list_2 = [4, 24, 14, 7, 16, 25, 1, 26, 18, 10, 2, 15, 23, 19, 13, 8, 3, 12, 22, 20, 17, 11, 21, 5, 9, 6]

number_of_encrypted_chars = 671


def encrypt(plain_text):
    cipher_text = ""
    global number_of_encrypted_chars
    for plain_char in plain_text:
        if plain_char not in alphabet:
            cipher_text += plain_char
        else:
            cipher_text += get_cipher_char(plain_char)
            number_of_encrypted_chars += 1
            update_rotors_encryption()
    return cipher_text


def decrypt(cipher_text):
    plain_text = ""
    global number_of_encrypted_chars
    for cipher_char in cipher_text[::-1]:
        if cipher_char not in alphabet:
            plain_text = cipher_char + plain_text
        else:
            update_rotors_decryption()
            number_of_encrypted_chars -= 1
            plain_text = get_plain_char(cipher_char) + plain_text
    return plain_text


def get_cipher_char(plain_char):
    first_rotor_input = first_rotor_list_1[alphabet.index(plain_char)]
    first_rotor_output = first_rotor_list_2.index(first_rotor_input)
    second_rotor_input = second_rotor_list_1[first_rotor_output]
    second_rotor_output = second_rotor_list_2.index(second_rotor_input)
    third_rotor_input = third_rotor_list_1[second_rotor_output]
    third_rotor_output = third_rotor_list_2.index(third_rotor_input)
    cipher_char = alphabet[third_rotor_output]
    return cipher_char


def get_plain_char(cipher_char):
    third_rotor_output = third_rotor_list_2[alphabet.index(cipher_char)]
    third_rotor_input = third_rotor_list_1.index(third_rotor_output)
    second_rotor_output = second_rotor_list_2[third_rotor_input]
    second_rotor_input = second_rotor_list_1.index(second_rotor_output)
    first_rotor_output = first_rotor_list_2[second_rotor_input]
    first_rotor_input = first_rotor_list_1.index(first_rotor_output)
    plain_char = alphabet[first_rotor_input]
    return plain_char


def update_rotors_encryption():
    global first_rotor_list_1, first_rotor_list_2
    global second_rotor_list_1, second_rotor_list_2
    global third_rotor_list_1, third_rotor_list_2
    first_rotor_list_1 = rotate_rotor_down(first_rotor_list_1)
    first_rotor_list_2 = rotate_rotor_down(first_rotor_list_2)
    if number_of_encrypted_chars % len(alphabet) == 0:
        second_rotor_list_1 = rotate_rotor_down(second_rotor_list_1)
        second_rotor_list_2 = rotate_rotor_down(second_rotor_list_2)
    if number_of_encrypted_chars % pow(len(alphabet), 2) == 0:
        third_rotor_list_1 = rotate_rotor_down(third_rotor_list_1)
        third_rotor_list_2 = rotate_rotor_down(third_rotor_list_2)


def update_rotors_decryption():
    global first_rotor_list_1, first_rotor_list_2
    global second_rotor_list_1, second_rotor_list_2
    global third_rotor_list_1, third_rotor_list_2
    first_rotor_list_1 = rotate_rotor_up(first_rotor_list_1)
    first_rotor_list_2 = rotate_rotor_up(first_rotor_list_2)
    if number_of_encrypted_chars % len(alphabet) == 0:
        second_rotor_list_1 = rotate_rotor_up(second_rotor_list_1)
        second_rotor_list_2 = rotate_rotor_up(second_rotor_list_2)
    if number_of_encrypted_chars % pow(len(alphabet), 2) == 0:
        third_rotor_list_1 = rotate_rotor_up(third_rotor_list_1)
        third_rotor_list_2 = rotate_rotor_up(third_rotor_list_2)


def rotate_rotor_down(rotor_list):
    return [rotor_list[-1]] + rotor_list[:-1]


def rotate_rotor_up(rotor_list):
    return rotor_list[1:] + [rotor_list[0]]


def main():
    cipher_text = encrypt("nebo je vedro")
    plain_text = decrypt(cipher_text)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- cryptanalysis
    * known plaintext attack - by knowing enough pairs plaintext-ciphertext, rotor positions can be figured out, and
    that way the cipher is broken because the attacker can decrypt messages
"""