alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def encrypt(plain_text, key):
    cipher_text = ""
    for plain_char, key_char in zip(plain_text, key):
        cipher_text += alphabet[(alphabet.index(plain_char) + alphabet.index(key_char)) % len(alphabet)]
    return cipher_text


def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for cipher_char in ciphertext:
        plain_char_index = (alphabet.index(cipher_char) - alphabet.index(key[key_index])) % len(alphabet)
        plain_char = alphabet[plain_char_index]
        plaintext += plain_char
        key += plain_char
        key_index += 1
    return plaintext


def main():
    initial_key = "deceptive"
    key = initial_key + "wearediscoveredsaveyourself"
    cipher_text = encrypt("wearediscoveredsaveyourself", key)
    plain_text = decrypt(cipher_text, initial_key)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()

"""
Cipher can be broken using following approaches:
- cryptanalysis
    * even though the key isn't repeating like with regular vigenere cipher, this cipher can be broken because
    plaintext and the key share almost identical frequency distribution of letters, so probability of situations where 
    a plaintext letter is encrypted using an identical key letter can be approximated using standard english letter
    frequency statistics; for example, frequency of letter "e" in plain text is 0.127, so probability that letter
    "e" is at the same position in the key is (0.127)^2 ~ 0.016 - these situations are significant because they
    reveal the plaintext ("e" encrypted by "e" will always be "i" in the ciphertext, so frequency of letter "i" is 
    also 0.016)
"""