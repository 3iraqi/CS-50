# Unit Tests

## `assert`

<details>
<summary>return bool</summary>

  ```python
     """Testing the calculator"""

from calculator import square


def main():
    """main"""

    test_square()


def test_square():
    """Test square calculation"""
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()

```

</details>

## `pytest`

<details>
<summary>py third party program</summary>

```python
    """PEP"""
from calculator import square


def test_square():
    """PEP"""
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

```

</details>
