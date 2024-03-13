from utils import test_cesar_algorithm
from utils import test_monoalphabetic_algorithm
from utils import test_playfair_algorithm
from utils import test_vigenere_algorithm
from utils import test_autokey_algorithm


def main():
    test_cesar_algorithm()
    test_monoalphabetic_algorithm()
    test_playfair_algorithm()
    test_vigenere_algorithm()
    test_autokey_algorithm()


if __name__ == "__main__":
    main()
