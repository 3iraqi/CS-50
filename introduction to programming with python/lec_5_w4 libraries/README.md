# Libraries

- [Libraries](#libraries)
  - [APIs package](#apis-package)
    - [requests](#requests)
    - [Json](#json)

> Ex: `• random  library` `statistics` `command-line arguments`

- to use any library you need a new key word called: `import`
- `import` allows you to import the contents of the functions from some module in Python.
  - > to import all library and use custom name using `as`
  - > here  u use the choice as a method of class random
  
  - ```python
        # to import all library and use custom name using `as`
        import random as rndm
        # that is a Ex:
        # here  u use the choice as a method of class random
        dice=rndm.choice([1,2,3,4,5,6])
        print(dice) 
    ```

- if you choose specific function from some library you use `from` key word to call the function as its name.
- `from`

  - ```python
      from random import choice

      dice=choice([1,2,3,4,5,6])
      print(dice)
    ```

## APIs package

### [requests](https://pypi.org/project/requests/)

>> pip install requests
>> applied in [itunes.py](itunes.py)

### Json

>> APIs Third-party Library.
>