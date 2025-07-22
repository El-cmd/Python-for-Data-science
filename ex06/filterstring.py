from ft_filter import ft_filter
import sys
import string


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        assert not any(char in string.punctuation for char in sys.argv[1]), \
            "the arguments are bad"
        split = sys.argv[1].split()
        n = int(sys.argv[2])
        print(list(ft_filter(lambda x: len(x) > n, split)))
    except AssertionError as msg:
        print("AssertionError: " + str(msg))


if __name__ == "__main__":
    main()
