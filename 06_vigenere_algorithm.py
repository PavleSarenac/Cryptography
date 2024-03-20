alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def encrypt(plain_text, key):
    cipher_text = ""
    for plain_char, key_char in zip(plain_text, key):
        cipher_text += alphabet[(alphabet.index(plain_char) + alphabet.index(key_char)) % len(alphabet)]
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    for cipher_char, key_char in zip(cipher_text, key):
        plain_text += alphabet[(alphabet.index(cipher_char) - alphabet.index(key_char)) % len(alphabet)]
    return plain_text


def get_key(plain_text, initial_key):
    key = ""
    key_char_index = 0
    for _ in range(len(plain_text)):
        key += initial_key[key_char_index % len(initial_key)]
        key_char_index += 1
    return key


def main():
    initial_key = "deceptive"
    key = get_key("wearediscoveredsaveyourself", initial_key)
    cipher_text = encrypt("wearediscoveredsaveyourself", key)
    plain_text = decrypt(cipher_text, key)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- cryptanalysis
    * kasiski method - find repeating sequences of letters in the ciphertext and using that data try to
    figure out the key length - once that is done, this cipher can be analyzed as series of monoalphabetic
    ciphers for every letter of the key separately
"""