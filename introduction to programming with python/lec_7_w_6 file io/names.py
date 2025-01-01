with open("names.txt",mode="r",encoding="UTF-8" ) as file:
    # I used mode "r" to read the file
    for line in file:
        print("hello,",line.rstrip())
