# FILE   I / O

---

<details>
  <summary>Ex-1:Save to List </summary>

```python
names=[]

for _ in range(3):
    names.append(input("what's your name?"))

for name in sorted(names):
    print(f"hello, {name}")

```

</details>

---

<details>
  <summary>TXT file </summary>

```python
    name = input("what is your name? ")
    
    file = open("names.txt","w",encoding="UTF-8" ) # w for create but override every time you run the code.
    file = open("names.txt","a",encoding="UTF-8" )# a for create and append every new data
    
    file.write(f"{name}\n")
    
    file.close()

```

</details>

---

<details>
  <summary>with [keyword] </summary>

> with handle open and then close the file
> > pythonic

```python
    name = input("what is your name? ")
    
    with open("names.txt","a",encoding="UTF-8" ) as file:
        file.write(f"{name}\n")  

```

</details>

---

<details>
  <summary>read an existing file</summary>

>first way explicitly

- ```python
    with open("names.txt",mode="r",encoding="UTF-8" ) as file: 
    # I used mode "r" to read the file 
        lines = file.readlines()

    for line in lines:
        print("hello,",line.rstrip())
  ```

> second way combine

- ```python
    with open("names.txt",mode="r",encoding="UTF-8" ) as file: 
    # I used mode "r" to read the file 
        for line in file:
            print("hello,",line.rstrip())
  ```

</details>

---
