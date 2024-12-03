def main():
    a=add_first(3)
    result=a(4)
    print(result)    
    
def add_first(a):
    def add_second(b):
        return a+b
    return add_second




if __name__ == "__main__":
    main()