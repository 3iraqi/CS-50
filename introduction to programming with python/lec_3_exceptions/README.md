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

* NameError solution: | `Try:` and `Except:` and `else`
  - ```python
        # output if input="string" will be NameError
        try:
            x=int(input("What's x?"))
        except ValueError:
            print("x is not a number")
        else:        
            print(f"x is {x}")

        # if input is a string    
        # output NameError: name 'x' is not defined. 
        # but when we use else the output will be x is {x}
    ```
 
* Another example for `break` key word
    - ```python
        def ex1():
           while True:
                try:
                    x=int(input("What's X?"))
                except ValueError:
                    print("X is not an Integer")
                else:        
                    break
             
           print(f"X is {x}")
        ```



* Another example for `return` key word
    - ```python
        def ex1():
           while True:
                try:
                    x=int(input("What's X?"))
                except ValueError:
                    print("X is not an Integer")
                else:        
                    return x
             
        ```
* Another example for `return` key word and normalize code
    - ```python
        def ex1():
           while True:
                try:
                    return int(input("What's X?"))
                except ValueError:
                    print("X is not an Integer")
            
        ```
* Another example for `pass` key word and normalize code
    - ```python
        def ex1():
           while True:
                try:
                    return int(input("What's X?"))
                except ValueError:
                    pass
            
        ```



# MEDIOCRACY : The Politics of the Extreme Center


