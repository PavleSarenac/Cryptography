import math

e = 52127
n = 868165516507

alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]


def find_d_ana():
    p = q = None
    for potential_factor in range(3, int(math.sqrt(n)) + 1, 2):
        if n % potential_factor == 0:
            p = potential_factor
            q = n // p
            break
    phi_n = (p - 1) * (q - 1)
    d = pow(e, -1, phi_n)
    return d


def get_vigenere_key(d):
    with open("encrypted_vigenere_key", "r") as file:
        encrypted_vigenere_key = file.read()
    decrypted_vigenere_key = str(pow(int(encrypted_vigenere_key), d, n))
    vigenere_key_letter_indexes = [
        int(decrypted_vigenere_key[0:2]),
        int(decrypted_vigenere_key[2]),
        int(decrypted_vigenere_key[3:5]),
        int(decrypted_vigenere_key[5:7]),
        int(decrypted_vigenere_key[7]),
        int(decrypted_vigenere_key[8:10]),
        int(decrypted_vigenere_key[10])
    ]
    vigenere_key = "".join([alphabet[i] for i in vigenere_key_letter_indexes])
    return vigenere_key


def decrypt_vigenere(ciphertext, vigenere_key):
    plaintext = ""
    key_index = 0
    for cipher_char in ciphertext:
        plain_char_index = (alphabet.index(cipher_char) - alphabet.index(vigenere_key[key_index])) % len(alphabet)
        plain_char = alphabet[plain_char_index]
        plaintext += plain_char
        vigenere_key += plain_char
        key_index += 1
    return plaintext


def main():
    d = find_d_ana()
    vigenere_key = get_vigenere_key(d)
    with open("ciphertext.txt", "r") as file:
        ciphertext = file.read()
    plaintext = decrypt_vigenere(ciphertext, vigenere_key)
    with open("plaintext.txt", "w") as file:
        file.write(plaintext)


if __name__ == "__main__":
    main()
