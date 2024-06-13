import random

q, alpha, y_a, y_b = (None, None, None, None)


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


def diffie_hellman_find_q():
    global q
    for potential_q in range(10000, 1000000):
        if is_prime_number_miller_rabin_algorithm(potential_q):
            q = potential_q
            break


def diffie_hellman_find_alpha():
    global alpha, q
    alpha = 2
    while True:
        numbers_set = set()
        for j in range(1, q):
            numbers_set.add(pow(alpha, j, q))
        if len(numbers_set) == q - 1:
            break
        alpha += 1


def print_info(x_a, x_b, k_a, k_b):
    global q, alpha, y_a, y_b
    print(f"q = {q};")
    print(f"alpha = {alpha};")
    print(f"x_a = {x_a};")
    print(f"x_b = {x_b};")
    print(f"y_a = (alpha ^ x_a) mod q = {y_a};")
    print(f"y_b = (alpha ^ x_b) mod q = {y_b};")
    print(f"k_a = (y_b ^ x_a) mod q =  {k_a};")
    print(f"k_b = (y_a ^ x_b) mod q = {k_b};")


def main():
    global q, alpha, y_a, y_b
    diffie_hellman_find_q()
    diffie_hellman_find_alpha()
    x_a = random.randint(1, q - 1)
    x_b = random.randint(1, q - 1)
    y_a = pow(alpha, x_a, q)
    y_b = pow(alpha, x_b, q)
    k_a = pow(y_b, x_a, q)
    k_b = pow(y_a, x_b, q)
    print_info(x_a, x_b, k_a, k_b)


if __name__ == "__main__":
    main()
