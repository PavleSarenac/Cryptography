from algorithms.symmetric_algorithms.substitution_algorithms.monoalphabetic_algorithms.cesar_algorithm import CesarAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.monoalphabetic_algorithms.monoalphabetic_algorithm import MonoalphabeticAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.polyalphabetic_algorithms.playfair_algorithm import PlayfairAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.polyalphabetic_algorithms.vigenere_algorithm import VigenereAlgorithm


def test_algorithm_basic(algorithm):
    cipher_text = algorithm.encrypt()
    algorithm.set_cipher_text(cipher_text)

    plain_text = algorithm.decrypt()
    algorithm.set_plain_text(plain_text)


def test_cesar_algorithm():
    cesar_algorithm = CesarAlgorithm()
    test_algorithm_basic(cesar_algorithm)

    brute_force_attack_output = cesar_algorithm.brute_force_attack()
    cesar_algorithm.set_brute_force_attack_output(brute_force_attack_output)


def test_monoalphabetic_algorithm():
    monoalphabet_algorithm = MonoalphabeticAlgorithm()
    test_algorithm_basic(monoalphabet_algorithm)

    monoalphabet_algorithm.cryptanalysis()


def test_playfair_algorithm():
    playfair_algorithm = PlayfairAlgorithm()
    test_algorithm_basic(playfair_algorithm)


def test_vigenere_algorithm():
    vigenere_algorithm = VigenereAlgorithm()
    test_algorithm_basic(vigenere_algorithm)
