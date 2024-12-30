name = input("what is your name? ")

with open("names.txt","a",encoding="UTF-8" ) as file:
    file.write(f"{name}\n")
