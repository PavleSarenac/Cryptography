from algorithms.symmetric_algorithms.supstitution_algorithms.cesar_algorithm import CesarAlgorithm


def test_cesar_algorithm():
    cesar_algorithm = CesarAlgorithm()

    cipher_text = cesar_algorithm.encrypt()
    cesar_algorithm.set_cipher_text(cipher_text)

    plain_text = cesar_algorithm.decrypt()
    cesar_algorithm.set_plain_text(plain_text)

    brute_force_attack_output = cesar_algorithm.brute_force_attack()
    cesar_algorithm.set_brute_force_attack_output(brute_force_attack_output)


def main():
    test_cesar_algorithm()


if __name__ == "__main__":
    main()
