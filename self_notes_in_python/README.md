
# ▣ Python self Study Notes

---

> Some of Advanced Topics (Content Table)

- [▣ Python self Study Notes](#-python-self-study-notes)
  - [Advanced Topics](#advanced-topics)
    - [**Nested function**](#nested-function)
      - [Python Closures (Closure)](#python-closures-closure)
        - [When to use closures?](#when-to-use-closures)
      - [**Generators** (Generator)](#generators-generator)
        - [Generator function vs. List comprehension`(Generator Expression)`](#generator-function-vs-list-comprehensiongenerator-expression)
      - [Python Decorators](#python-decorators)

---

## Advanced Topics

### **Nested function**

#### Python Closures [(Closure)](closure.py)

##### When to use closures?
>
> - Closures can be used to avoid global values and provide data hiding, and can be an elegant solution for simple cases with one or few methods.
> - However, for larger cases with multiple attributes and methods, a `class` implementation may be more appropriate.

- Ex:

- ```python
    def calculate():
        num = 1
        def inner_func():
            nonlocal num
            num += 2
            return num
        return inner_func

    odd = calculate() # Call the outer function
    print(odd())   # Call the inner function
    ```

> Here `nonlocal` mean the variable in the outer functions

- ```python
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

#### **Generators** [(Generator)](generator.py)

##### Generator function vs. List comprehension`(Generator Expression)`
>>
>> - It do the same thing as `[list comprehension]` = `(Python Generator Expression)` show file called generator to show.
>> - Generator function is better in performance(memory usage).
>> - List comprehension is better in speed (Execution time).
>>
>>> - Use Case (Practicality)
>>> - **`Generator`**:
>>>   - Excellent for **`streaming data`** or **`partial consumption`** of results.
>>>   - Handles **`infinite`** or **`very large datasets`** that cannot fit into memory.
>>> - **`List Comprehension`**:
>>>   - Best for tasks requiring **`repeated access`** to the entire dataset.
>>>   - Suitable for computations on small to moderately sized data.
>>> - **`Winner`**: Depends on the use case:
>>>   - **`Generator`**: For large or infinite datasets, one-time or partial use.
>>>   - **`List Comprehension`**: For small datasets or frequent access to all elements.
>> (yield) Keyword
>
> - How It Works:
>
> 1. The function `generate_squares(n)` is a generator function because it uses the `yield` keyword.
> 2. When called, it doesn't execute the loop immediately but returns a generator object.
> 3. Each time the generator is iterated (e.g., in a for loop), it produces the next square and pauses.
> 4. When all values are exhausted, the iteration stops.
>
>

- ```python
    def square_numbers(nums):
    for i in nums:
        yield(i*i)  # return one value for each call.
    
    my_nums = square_numbers([1,2,3,4,5])
    my_nums=[x*x for x in [1,2,3,4,5]]
    print(my_nums)
    for num in my_nums:
        print(num, end=" ")
    ```

---

#### Python Decorators

>> - it allows programmers to modify the **`behavior`** of a function or class.
>> - Decorators allow us to **`wrap another function`** in order to extend the behavior of the wrapped function, without permanently modifying it
>
>> In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.
>
>
>

---------- [Content Table 🔝](#-python-self-study-notes)-------
