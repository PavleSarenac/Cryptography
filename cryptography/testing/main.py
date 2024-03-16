from utils import *


def main():
    # Symmetric substitution monoalphabetic algorithms
    test_cesar_algorithm()
    test_monoalphabetic_algorithm()

    # Symmetric substitution polyalphabetic algorithms
    test_playfair_algorithm()
    test_vigenere_algorithm()
    test_autokey_algorithm()
    test_hill_algorithm()
    test_vernam_algorithm()
    test_one_time_pad_algorithm()

    # Symmetric transposition algorithms
    test_rail_fence_algorithm()


if __name__ == "__main__":
    main()
