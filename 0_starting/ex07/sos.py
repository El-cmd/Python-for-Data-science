import sys

NESTED_MORSE = {"A": ".- ", "B": "-... ", "C": "-.-. ",
                "D": "-.. ", "E": ". ", "F": "..-. ", "G": "--. ",
                "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
                "L": ".-.. ", "M": "-- ", "N": "-. ",
                "O": "--- ", "P": ".--. ",
                "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ", "U": "..- ",
                "V": "...- ", "W": ".-- ", "X": "-..- ",
                "Y": "-.-- ", "Z": "--.. ",
                "0": "----- ", "1": ".---- ", "2": "..--- ",
                "3": "...-- ", "4": "....- ",
                "5": "..... ", "6": "-.... ", "7": "--... ",
                "8": "---.. ", "9": "----. ",
                " ": "/ "}


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert sys.argv[1].isalnum(), "the arguments are bad"
        for char in sys.argv[1]:
            print(NESTED_MORSE[char.upper()], end="")
        print()
    except AssertionError as msg:
        print("AssertionError: " + str(msg))


if __name__ == "__main__":
    main()
