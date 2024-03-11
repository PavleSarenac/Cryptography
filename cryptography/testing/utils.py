from algorithms.symmetric_algorithms.supstitution_algorithms.cesar_algorithm import CesarAlgorithm
from algorithms.symmetric_algorithms.supstitution_algorithms.monoalphabet_algorithm import MonoalphabetAlgorithm
from algorithms.symmetric_algorithms.supstitution_algorithms.playfair_algorithm import PlayfairAlgorithm


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


def test_monoalphabet_algorithm():
    monoalphabet_algorithm = MonoalphabetAlgorithm()
    test_algorithm_basic(monoalphabet_algorithm)

    monoalphabet_algorithm.cryptanalysis()


def test_playfair_algorithm():
    playfair_algorithm = PlayfairAlgorithm()
    test_algorithm_basic(playfair_algorithm)
