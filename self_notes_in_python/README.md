# ▣ Python self Study Notes

---

## Table of Contents

1. [Nested function-Closure](#nested-function-closure)
2. [Generator function](#generator-function)
<!-- 
1. []()
2. []() 
3. []()
4. []()
5. []()
6. []()
7. []()
8.  []()
9.  []()
10. 
11. -->

## Closure

>> ## **Nested function** [(Closure)](closure.py)
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

> ## **Generator function** [(Generator)](generator.py)
>
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

* ```python
    def square_numbers(nums):
    for i in nums:
        yield(i*i)  # return one value for each call.
    
    my_nums = square_numbers([1,2,3,4,5])
   
    for num in my_nums:
        print(num, end=" ")
    ```
