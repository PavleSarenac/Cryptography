import math
import random


alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]

e = None
n = None


def is_prime_number_miller_rabin_algorithm(p):
    k, q = get_k_and_q(p - 1)
    a = get_a(p)
    if is_first_condition_true(a, q, p) or is_second_condition_true(a, k, q, p):
        return True
    return False


def get_k_and_q(decremented_number):
    k = 0
    current_number = decremented_number
    while current_number % 2 == 0:
        current_number //= 2
        k += 1
    q = decremented_number // pow(2, k)
    return k, q


def get_a(p):
    return random.randint(2, p - 2)


def is_first_condition_true(a, q, p):
    return pow(a, q, p) == 1


def is_second_condition_true(a, k, q, p):
    for j in range(k):
        if pow(a, pow(2, j) * q, p) == p - 1:
            return True
    return False


def rsa_get_e(phi_n):
    while True:
        potential_e = random.randint(2, phi_n)
        if math.gcd(potential_e, phi_n) == 1:
            return potential_e


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


def main():
    global n, e
    p, q = rsa_get_p_and_q()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = rsa_get_e(phi_n)
    d = pow(e, -1, phi_n)


if __name__ == "__main__":
    main()
