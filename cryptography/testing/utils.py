from algorithms.symmetric_algorithms.substitution_algorithms.monoalphabetic_algorithms.cesar_algorithm import CesarAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.monoalphabetic_algorithms.monoalphabetic_algorithm import MonoalphabeticAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.polyalphabetic_algorithms.playfair_algorithm import PlayfairAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.polyalphabetic_algorithms.vigenere_algorithm import VigenereAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.polyalphabetic_algorithms.autokey_algorithm import AutokeyAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.polyalphabetic_algorithms.hill_algorithm import HillAlgorithm
from algorithms.symmetric_algorithms.substitution_algorithms.polyalphabetic_algorithms.vernam_algorithm import VernamAlgorithm


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


def test_autokey_algorithm():
    autokey_algorithm = AutokeyAlgorithm()
    test_algorithm_basic(autokey_algorithm)


def test_hill_algorithm():
    hill_algorithm = HillAlgorithm()
    test_algorithm_basic(hill_algorithm)


def test_vernam_algorithm():
    vernam_algorithm = VernamAlgorithm()
    test_algorithm_basic(vernam_algorithm)
