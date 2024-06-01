import random
import os

S = []
T = []
cnt1 = cnt2 = 0


def generate_key() -> bytes:
    key_size = random.randint(1, 256)
    key_bytes = os.urandom(key_size)
    return key_bytes


def initialize_s_and_t(key):
    for i in range(256):
        S.append(i)
        T.append(key[i % len(key)])


def swap_s_elements(i, j):
    tmp = S[i]
    S[i] = S[j]
    S[j] = tmp


def initial_s_permutation():
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        swap_s_elements(i, j)


def get_next_key_byte() -> int:
    global cnt1, cnt2
    cnt1 = (cnt1 + 1) % 256
    cnt2 = (cnt2 + S[cnt1]) % 256
    swap_s_elements(cnt1, cnt2)
    t = (S[cnt1] + S[cnt2]) % 256
    k = S[t]
    return k


def encrypt(plaintext) -> tuple:
    ciphertext = ""
    keys_used = []
    plaintext_hex_string = plaintext.encode("utf-8").hex()  # Ova hex() metoda garantuje da je duzina stringa umnozak dvojke.
    for i in range(0, len(plaintext_hex_string), 2):
        new_key = get_next_key_byte()
        ciphertext_int = int(plaintext_hex_string[i:i+2], 16) ^ new_key
        keys_used.append(new_key)
        ciphertext_hex = hex(ciphertext_int)[2:]  # Ova hex() metoda ne garantuje da ce bajt biti uvek predstavljen sa dve hex cifre.
        if len(ciphertext_hex) == 1:
            ciphertext_hex = "0" + ciphertext_hex
        ciphertext += ciphertext_hex
    return ciphertext, keys_used


def decrypt(ciphertext, keys_used) -> str:
    plaintext = []
    key_index = 0
    for i in range(0, len(ciphertext), 2):
        plaintext_int = int(ciphertext[i:i+2], 16) ^ keys_used[key_index]
        plaintext_byte = bytes.fromhex(hex(plaintext_int)[2:])
        plaintext.append(plaintext_byte.decode("utf-8"))
        key_index += 1
    return "".join(plaintext)


def main():
    key = generate_key()
    initialize_s_and_t(key)
    initial_s_permutation()
    ciphertext, keys_used = encrypt("Structural flaw was discovered with RC4, so it is forbidden in TLS since 2015.")
    plaintext = decrypt(ciphertext, keys_used)
    print(plaintext)
    print(ciphertext)


if __name__ == "__main__":
    main()
