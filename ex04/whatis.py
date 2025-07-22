import sys


def main():
    if len(sys.argv) == 1:
        return
    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        var = int(sys.argv[1])
        if var % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
