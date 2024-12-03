# ▣ Python self Study Notes

---

## Table of Contents

1. [Nested function](#nested-function-closure)

## Closure

>> ## **Nested function** [(Closure)](closure.py) [element: a]
>

* Ex:

* ```python
 
    def outer(a):
        def inner(b):
            return a+b
        return inner
    
    first=outer(a)
    result=first(b)
    print(result)
    # output: result=a+b
    ```

---

> **Generator function**
>> (yield) Keyword
>
> * How It Works:
>
> 1. The function `generate_squares(n)` is a generator function because it uses the `yield` keyword.
> 2. When called, it doesn't execute the loop immediately but returns a generator object.
> 3. Each time the generator is iterated (e.g., in a for loop), it produces the next square and pauses.
> 4. When all values are exhausted, the iteration stops.
>
>
