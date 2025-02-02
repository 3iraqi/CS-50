# CS'50 |regex ([Regular Expression](https://cs50.harvard.edu/python/2022/weeks/7/))

- [CS'50 |regex (Regular Expression)](#cs50-regex-regular-expression)
  - [Validation without Regular Expression](#validation-without-regular-expression)
    - [Validation Examples](#validation-examples)
  - [re | library](#re--library)
    - [That Contain regex patterns](#that-contain-regex-patterns)
    - [here some of regex patterns](#here-some-of-regex-patterns)
    - [re Examples](#re-examples)

## Validation without Regular Expression

### Validation Examples

<details>
<summary>
Validate.py
</summary>

[validate.py](./reqular_expressions.ipynb)

```python

email = input("what is your email? ").strip()

user_name, domain = email.split("@")

## first way
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

## Second way
if user_name and "." in domain:
    print("Valid")
else:
    print("Invalid")

"""
But we still need more control
"""

```

</details>

## re | [library](https://docs.python.org/3/library/re.html)
>
>> Regular Expression library
>
### That Contain [regex patterns](./regex_pattern.md)

### here some of regex patterns

| Pattern | Description |
|---------|------------|
|`.`|any character except a newline|
|`*`|0 or more repetitions|
|`+`|1 or more repetitions|
|`?`|0 or 1 repetition|
|`{m}`|m repetitions|
|`{m,n}`|m,n repetitions|

```python
re.search(pattern, string,flag=0)
```

### re Examples

<details>
  <summary>validate.py</summary>

[validate.py](./reqular_expressions.ipynb)

```python
import re

# email = input("what is your email? ").strip()
email= "Mohamed.8.eleraqi@gmail.com"

# if re.search("..*@..*",email):
if re.search(".+@.+",email):
    print("Valid")
else:
    print("Invalid")
```

</details>
