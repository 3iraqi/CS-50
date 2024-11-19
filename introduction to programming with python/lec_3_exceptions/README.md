# ▣ Lecture-3-{Exceptions}:

* **SyntaxError**: 
* **RuntimeError**:
* **ValueError**: 
  * When you input a different data type 
* **NameError:**
* **InvalidArgument**:
* 

### **▾ Solution**:
* ValueError solution: | `Try:` and `Except:`
    - ```python
        # if input is "string" or Boolean  
        # you can handle exception with this way:
        try:
            x=int(input("What's x?"))
            print(f"x is {x}")
        except ValueError:
            print("x is not a number")
        
        ```

* NameError solution: | `Try:` and `Except:`
  - ```python
        # output if input="string" will be NameError
        try:
           x=int(input("What's x?"))
        except ValueError:
            print("x is not a number")
           
        print(f"x is {x}")

        # if input is a string    
        # output NameError: name 'x' is not defined. 

    ```



