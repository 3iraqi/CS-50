"""Testing the calculator"""

from calculator import square


def main():
    """main"""
    test_square()


def test_square():
    """Test square calculation"""
    if square(2) != 4:
        print("2 Squared was not 4")
    if square(3) != 9:
        print("3 Squared was not 9")


if __name__ == "__main__":
    main()
