"""Computes the digit sum of a number entered by the user."""


def digit_sum(number):
    """
    Calculates the sum of all digits of a number.
    :param number: the number to calculate the digit sum of
    :return: the digit sum
    """
    number = str(number)  # Zuerst in einen String umwandeln, damit durch diesen iteriert werden kann
    total = 0
    for digit in number:
        total += int(digit)  # Das digit in ein int umwandeln zum addieren
    return total


def main():
    """
    Asks the user for a number and prints its digit sum.
    :return: None
    """
    number = input('Bitte eine Ganzzahl eingeben für Quersummenberechnung> ')
    print(f'Die Quersumme ist: {digit_sum(number)}')


if __name__ == '__main__':
    main()
