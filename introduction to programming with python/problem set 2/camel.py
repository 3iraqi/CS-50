
word=input("camelCase: ")
print("snake_case: ",end="")

for char in word:
   print(f"_{char.lower()}",end="") if char.isupper() else print(char,end="")
   