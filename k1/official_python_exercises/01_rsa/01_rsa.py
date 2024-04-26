import math

e = 509
n = 64507


def find_ana_d():
    p = q = None
    for potential_factor in range(3, int(math.sqrt(n)) + 1, 2):
        if n % potential_factor == 0:
            p = potential_factor
            q = n // p
            break
    phi_n = (p - 1) * (q - 1)
    d = pow(e, -1, phi_n)
    return d


def decrypt(ciphertext, d):
    plaintext = ""
    for i in range(0, len(ciphertext), 4):
        cipher_block_hex_string = ciphertext[i:i+4]
        cipher_block_hex_int = int(cipher_block_hex_string, 16)
        plain_block_hex_int = pow(cipher_block_hex_int, d, n)
        plaintext += get_digram(plain_block_hex_int)
    return plaintext


def get_digram(plain_block_hex_int):
    char_1_ascii_code = plain_block_hex_int // 256
    char_2_ascii_code = plain_block_hex_int % 256
    digram = chr(char_1_ascii_code) + chr(char_2_ascii_code)
    return digram


def main():
    d = find_ana_d()
    with open("ciphertext.txt", "r") as file:
        ciphertext = file.read().replace("\n", "")
    plaintext = decrypt(ciphertext, d)
    with open("plaintext.txt", "w") as file:
        file.write(plaintext)


if __name__ == "__main__":
    main()
