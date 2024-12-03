# ▣ Python self Study Notes

---

## Table of Contents

1. [Nested function-Closure](#nested-function-closure)
2. [Generator function](#generator-function-generator)
   * [Generator function vs list comprehension](#generator-function-vs-list-comprehension)
<!-- 
1. []()
2. []()
3. []()
4. []()
5. []()
6.  []()
7.  []()
8.  
9.  -->

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
>> ### Generator function vs. List comprehension
>>
>>> * It do the same thing as `[list comprehension]` show file called generator to show.
>>> * Generator function is better in performance(memory usage).
>>> * List comprehension is better in speed (Execution time).
>>>
>>>> * Use Case (Practicality)
>>>> * **`Generator`**:
>>>>   * Excellent for **`streaming data`** or **`partial consumption`** of results.
>>>>   * Handles **`infinite`** or **`very large datasets`** that cannot fit into memory.
>>>> * **`List Comprehension`**:
>>>>   * Best for tasks requiring **`repeated access`** to the entire dataset.
>>>>   * Suitable for computations on small to moderately sized data.
>>>> * **`Winner`**: Depends on the use case:
>>>>   * **`Generator`**: For large or infinite datasets, one-time or partial use.
>>>>   * **`List Comprehension`**: For small datasets or frequent access to all elements.
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
    my_nums=[x*x for x in [1,2,3,4,5]]
    print(my_nums)
    for num in my_nums:
        print(num, end=" ")
    ```
