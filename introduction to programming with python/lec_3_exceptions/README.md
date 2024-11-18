# ▣ Lecture-3-{Exceptions}:

* **SyntaxError**: 
* **RuntimeError**:
* **ValueError**: 
  * When you input a different data type 
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


