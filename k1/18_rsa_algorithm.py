import math
import random


alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]

e = None
n = None


def is_prime_number_miller_rabin_algorithm(p):
    k, q = miller_rabin_get_k_and_q(p - 1)
    a = miller_rabin_get_a(p)
    if miller_rabin_is_first_condition_true(a, q, p) or miller_rabin_is_second_condition_true(a, k, q, p):
        return True
    return False


def miller_rabin_get_k_and_q(decremented_number):
    k = 0
    current_number = decremented_number
    while current_number % 2 == 0:
        current_number //= 2
        k += 1
    q = decremented_number // pow(2, k)
    return k, q


def miller_rabin_get_a(p):
    return random.randint(2, p - 2)


def miller_rabin_is_first_condition_true(a, q, p):
    return pow(a, q, p) == 1


def miller_rabin_is_second_condition_true(a, k, q, p):
    for j in range(k):
        if pow(a, pow(2, j) * q, p) == p - 1:
            return True
    return False


def rsa_get_p_and_q():
    p = q = None
    for potential_factor_of_n in range(1 << 1024, 1 << 1025):
        if is_prime_number_miller_rabin_algorithm(potential_factor_of_n):
            p = potential_factor_of_n
            break
    for potential_factor_of_n in range(1 << 1024, 1 << 1025):
        if potential_factor_of_n != p and is_prime_number_miller_rabin_algorithm(potential_factor_of_n):
            q = potential_factor_of_n
            break
    return p, q


def rsa_get_e(phi_n):
    while True:
        potential_e = random.randint(2, phi_n)
        if math.gcd(potential_e, phi_n) == 1:
            return potential_e


def print_info(p, q, phi_n, d):
    global n, e
    print(f"p = {p};")
    print(f"q = {q};")
    print(f"n = p * q = {n};")
    print(f"phi_n = phi_p * phi_q = (p - 1) * (q - 1) = {phi_n};")
    print(f"e = {e};")
    print(f"d = {d};")


def encrypt(plain_text):
    global n, e
    cipher_text = []
    for char in plain_text:
        cipher_text.append(pow(alphabet.index(char), e, n))
    return cipher_text


def decrypt(cipher_text, d):
    global n
    plain_text = []
    for num in cipher_text:
        plain_text.append(alphabet[pow(num, d, n)])
    return "".join(plain_text)


def main():
    global n, e
    p, q = rsa_get_p_and_q()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = rsa_get_e(phi_n)
    d = pow(e, -1, phi_n)
    print_info(p, q, phi_n, d)
    cipher_text = encrypt("desfirujovo")
    plain_text = decrypt(cipher_text, d)
    print(plain_text)
    print(cipher_text)


if __name__ == "__main__":
    main()
