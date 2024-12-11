
def main():
    x=123
    y=-123
    z=(2**(-32))> -123
    num=reverse(y)
    print(z)

def reverse(num):
    if num>(2**31+1) or num<(-1*(2**32)):
        return 0 
    elif num<0:
        return -1*reverse (-num)
    else:
        return int(str(num)[::-1])


if __name__ == '__main__':
    main()