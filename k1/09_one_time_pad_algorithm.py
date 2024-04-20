import random

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


def get_key(plain_text):
    return "".join([random.choice(alphabet) for _ in range(len(plain_text))])


def main():
    key = get_key("onetimepadistheonlytrulyunbreakablecipher")
    cipher_text = encrypt("onetimepadistheonlytrulyunbreakablecipher", key)
    plain_text = decrypt(cipher_text, key)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
One time pad is the only truly unbreakable cipher - even with unlimited time and computational resources it can
never be broken. The key is completely randomly generated and new key is generated for every encryption. The 
attacker can potentially get numerous good looking plaintexts by trying out different keys for decryption, but he 
can never find out which one is the real plaintext because there is no statistical correlation between plaintext
and key whatsoever, hence the cipher is unbreakable.

This cipher is generally not used because it is impractical - it requires generation of new key per every encryption,
and also the key has to be the same length as plaintext, so for example, for 5 GB of plaintext, another 5 GB is
necessary for the key, and that is obviously unacceptable.
"""