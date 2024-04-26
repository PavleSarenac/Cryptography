alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]


def decrypt_feistel(ciphertext):
    plaintext = ""
    for i in range(0, len(ciphertext), 10):
        digram = feistel_algorithm(ciphertext[i: i + 10])
        plaintext += digram
    return plaintext


def feistel_algorithm(block):
    prev_left_half = int(block[0:5], 2)
    prev_right_half = int(block[5:10], 2)
    left_half = right_half = None
    for _ in range(16):
        left_half = prev_right_half
        right_half = prev_left_half ^ feistel_round_function(prev_right_half)
        prev_left_half = left_half
        prev_right_half = right_half
    char_1 = alphabet[right_half % len(alphabet)]
    char_2 = alphabet[left_half % len(alphabet)]
    digram = char_1 + char_2
    return digram


def feistel_round_function(x):
    return pow(7, x, 26)


def main():
    with open("ciphertext.txt", "r") as file:
        ciphertext = file.read().replace("\n", "")
    with open("plaintext.txt", "w") as file:
        file.write(decrypt_feistel(ciphertext))


if __name__ == "__main__":
    main()
