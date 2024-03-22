alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
extended_alphabet = alphabet + [chr(i) for i in range(ord("A"), ord("Z") + 1)]


def encrypt(plain_text, block_size_in_bits, char_size_in_bits):
    cipher_text = ""
    reformatted_plain_text = reformat_plain_text(plain_text, block_size_in_bits, char_size_in_bits)
    for i in range(0, len(reformatted_plain_text), 2):
        cipher_char_1_index, cipher_char_2_index = feistel_algorithm(
            extended_alphabet.index(reformatted_plain_text[i]),
            extended_alphabet.index(reformatted_plain_text[i + 1]),
            True
        )
        cipher_text += f"{extended_alphabet[cipher_char_1_index]}{extended_alphabet[cipher_char_2_index]}"
    return cipher_text


def decrypt(cipher_text):
    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        plain_char_1_index, plain_char_2_index = feistel_algorithm(
            extended_alphabet.index(cipher_text[i]),
            extended_alphabet.index(cipher_text[i + 1]),
            False
        )
        plain_text += f"{extended_alphabet[plain_char_1_index]}{extended_alphabet[plain_char_2_index]}"
    return plain_text


def reformat_plain_text(plain_text, block_size_in_bits, char_size_in_bits):
    if len(plain_text) * char_size_in_bits % block_size_in_bits != 0:
        plain_text += "x"
    return plain_text


def feistel_algorithm(left_block_half, right_block_half, is_encryption):
    number_of_rounds = 16
    for current_round_number in range(number_of_rounds):
        previous_left_block_half, previous_right_block_half = left_block_half, right_block_half
        left_block_half = previous_right_block_half
        right_block_half = previous_left_block_half ^ feistel_function(
            previous_right_block_half,
            get_current_round_key_encryption(current_round_number) if is_encryption else get_current_round_key_decryption(number_of_rounds, current_round_number)
        )
    return right_block_half, left_block_half


def feistel_function(right_block_half, current_round_key):
    return pow(7, right_block_half * current_round_key, len(alphabet))


def get_current_round_key_encryption(round_number):
    return round_number * 128 + 37


def get_current_round_key_decryption(number_of_rounds, round_number):
    return (number_of_rounds - 1 - round_number) * 128 + 37


def main():
    block_size_in_bits = 10
    char_size_in_bits = 5
    cipher_text = encrypt("itisonlywiththeheartthatonecanseerightly", block_size_in_bits, char_size_in_bits)
    plain_text = decrypt(cipher_text)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()
