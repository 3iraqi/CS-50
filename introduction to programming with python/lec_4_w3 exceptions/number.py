def main():
    y=get_int1();
    print(f"Y is {y-1}")     









def ex1():
    while True:
        try:
            x=int(input("What's X?"))
        except ValueError:
            print("X is not an Integer")
        else:        
            break
             
    print(f"X is {x}")
   
   
def get_int():
    while True:
        try:
            x=int(input("What's X? "))
        except ValueError:
            print("X is not an Integer")
        else:        
            return x

def get_int1():
    while True:
        try:
           return int(input("What's X? "))
        except ValueError:
            print("X is not an Integer")
        
            


main()