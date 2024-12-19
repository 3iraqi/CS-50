# Unit Tests

- [Unit Tests](#unit-tests)
  - [`assert`](#assert)
  - [`pytest`](#pytest)

>> Main Code Source

```python
"""Unit test example """

def main():
    """main"""
    x = int(input("What's X?"))
    print("x squared is", square(x))


def square(n):
    """Square number"""
    return n * n


if __name__ == "__main__":
    main()


```

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

- ```python
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

>> Another Ex

- ```python
    """PEP"""
    from calculator import square


    def test_positive():
        """PEP"""
        assert square(2) == 4
        assert square(3) == 9
    
    def test_negative():
        """PEP"""
        assert square(-2) == 4
        assert square(-3) == 9
    
    def test_zero():
        """PEP"""
        assert square(0) == 0
    

    ```

</details>
