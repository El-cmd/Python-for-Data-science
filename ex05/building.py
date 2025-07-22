import sys
import string


def main():
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punctuation = 0
    var = ""
    try:
        if len(sys.argv) == 1:
            var = input("What is the text to count?\n")
        else:
            assert len(sys.argv) == 2, "Too many arguments"
        if var == "":
            var = sys.argv[1]
        print("The text contains", len(var), "characters:")
        for char in var:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isdigit():
                digit += 1
            elif char.isspace():
                space += 1
            elif char in string.punctuation:
                punctuation += 1
        print(upper, "upper letters")
        print(lower, "lower letters")
        print(punctuation, "punctuation marks")
        print(space, "spaces")
        print(digit, "digits")
    except AssertionError as msg:
        print("AssertionError: " + str(msg))


if __name__ == "__main__":
    main()
