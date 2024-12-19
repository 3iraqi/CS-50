"""Testing the calculator"""

from calculator import square


def main():
    """main"""
    test_square()


def test_square():
    """Test square calculation"""
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()
