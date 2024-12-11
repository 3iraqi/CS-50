
def main():
    x=123
    y=-123
    # z=(2**(-32)) > -123
    num=reverse(y)
    print(y)

def reverse(num):
    if num>((2**31)+1) or -1*num>(2**32):
        return 0 
    elif num<0:
        return -reverse(-num)
    else:
        return int(str(num)[::-1])


if __name__ == '__main__':
    main()