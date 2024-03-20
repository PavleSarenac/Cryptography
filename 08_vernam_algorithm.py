alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
extended_alphabet = alphabet + [chr(i) for i in range(ord("A"), ord("A") + 6)]


def encrypt(plain_text, key):
    cipher_text = ""
    for plain_char, key_char in zip(plain_text, key):
        cipher_text += extended_alphabet[extended_alphabet.index(plain_char) ^ extended_alphabet.index(key_char)]
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    for cipher_char, key_char in zip(cipher_text, key):
        plain_text += extended_alphabet[extended_alphabet.index(cipher_char) ^ extended_alphabet.index(key_char)]
    return plain_text


def get_key(plain_text, initial_key):
    key = ""
    for key_char_index in range(len(plain_text)):
        key += initial_key[key_char_index % len(initial_key)]
    return key


def main():
    initial_key = "longrepeatedkeyonatape"
    key = get_key("vernamcipherisnotunbreakablebecauseoftherepeatingkey", initial_key)
    cipher_text = encrypt("vernamcipherisnotunbreakablebecauseoftherepeatingkey", key)
    plain_text = decrypt(cipher_text, key)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- cryptanalysis 
    * the longer the key, the more difficult it is to break this cipher, but still because the key is a repeated
    sequence of letters, it is possible to perform a known plaintext attack if the cryptanalyst knows some 
    plaintext-ciphertext pairs and there is sufficient ciphertext for analysis
"""