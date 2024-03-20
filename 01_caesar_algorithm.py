alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char not in alphabet:
            cipher_text += char
        else:
            cipher_text += alphabet[(alphabet.index(char) + key) % len(alphabet)]
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        if char not in alphabet:
            plain_text += char
        else:
            plain_text += alphabet[(alphabet.index(char) - key) % len(alphabet)]
    return plain_text


def main():
    key = 3
    cipher_text = encrypt("danas duva jak vetar", key)
    plain_text = decrypt(cipher_text, key)
    print(plain_text)
    print(cipher_text.upper())


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- brute-force attack
- cryptanalysis
    * analysis of single letter frequencies
"""