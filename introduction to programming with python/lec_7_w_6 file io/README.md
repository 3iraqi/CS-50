# FILE   I / O

<hr>

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

<hr>

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

<hr>

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

<hr>

<details>
  <summary>read an existing file</summary>

```python
    
    
    

```

</details>

<hr>
